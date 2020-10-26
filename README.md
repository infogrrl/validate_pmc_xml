# validate_pmc_xml
## About
A python script which allows the user to validate all XML documents in a given directory (folder) on the local computer, using the DTD specified in the XML itself.
Output is sent to a file in the input folder unless something else is specified with the --output flag. 


This software was a small professional development project to practice working with XML libraries in Python, and should be considered beta and all outputs should be validated by human experts.

## Usage
You will need to have Python 3.6 or higher installed.

Clone this repository to your local computer.
From the directory containing the .py script, invoke it using the command:

```python validate_pmc_xml.py /PATH/TO/XML/DIRECTORY```

The only required argument is the path to the directory (folder) on your local computer where the batch of XML files is located \[referred to as `xml_folder`\].  It is okay if this folder contains other file types -- the script will ignore them.

By default, the error output will be saved to a CSV file within the specified `xml_folder` directory.  The filename will be the name of the XML directory with `_ERRORS.csv` appended to the end.  There is an additional optional flag you can pass, `--output_dir` which allows you to override this default behavior and tell the computer explicitly where to save the errors CSV file.

```python validate_pmc_xml.py /XML/FOLDER/ --output_dir /home/desktop/errors_date_batch.csv```
