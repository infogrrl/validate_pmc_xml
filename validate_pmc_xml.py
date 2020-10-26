"""
Allows the user to validate all XML documents in a given directory (folder) on the local computer,
using the DTD specified in the XML itself.
Output is sent to a file in the input folder unless specified with the --output flag.
"""
import argparse
import csv
from lxml import etree
from pathlib import Path


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "xml_folder",
        help="The path to the folder on your computer with the XML to validate."
    )
    parser.add_argument(
        "--output_dir",
        help="A path where an error output file should be created.  If not specified, will by default be placed in the same directory as the source XML."
    )
    return parser.parse_args()


def main():

    args = get_args()

    # Path to folder of XML to validate
    xml_folder = Path(args.xml_folder)
    print(f"Validating XML in '{xml_folder}.'")

    if args.output_dir:
        errors_dir = Path(args.output_dir)
    else:
        errors_dir = xml_folder / (str(xml_folder.stem) + "_ERRORS.csv")
    print(f"Validation errors will be exported to .csv at `{errors_dir}`.")

    parser = etree.XMLParser()
    p = xml_folder.glob('*.xml')
    with open(errors_dir, "w") as csvfile:
        field_names = ["filepath","row","column", "error_level","domain_name","type_name","error_message"]
        csv_writer = csv.writer(csvfile, delimiter=",")
        csv_writer.writerow(field_names)
        for xml_doc in p:
            try:
                etree.parse(str(xml_doc), parser)
            except etree.XMLSyntaxError as e:
                log = e.error_log
                for entry in log:
                    if str(entry.filename) == str(xml_doc):
                        csv_writer.writerow(str(entry).split(":", 6))
                pass


if __name__ == "__main__":
    main()
