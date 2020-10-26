import csv
from lxml import etree
from pathlib import Path

# Path to file of XML to validate
xml_folder = Path("../21550417-10-02_errors")

parser = etree.XMLParser()

errors_dir = xml_folder / (str(xml_folder.stem) + "_ERRORS.csv")

p = xml_folder.glob('*.xml')

with open(errors_dir, "w") as csvfile:
    field_names = ["filepath","row","column", "error_level","domain_name","type_name","error_message"]
    csv_writer = csv.writer(csvfile, delimiter=",")
    csv_writer.writerow(field_names)
    for xml_doc in p:
        print(xml_doc)
        try:
            etree.parse(str(xml_doc), parser)
        except etree.XMLSyntaxError as e:
            log = e.error_log
            for entry in log:
                if str(entry.filename) == str(xml_doc):
                    print("same")
                    csv_writer.writerow(str(entry).split(":", 6))
            pass

