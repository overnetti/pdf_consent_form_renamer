# HelloSign Consent Form Renamer

## Introduction
The python script `pdf_consent_form_renamer.py` specifically renames HelloSign consent forms for the USENIX Association in the following format: lastname_firstname.pdf. If there are duplicate last names, the script will begin a counter after the firstname like so: lastname_firstname_1.pdf and continue counting if there are duplicate lastname and firstname combos.

The USENIX Association is an advanced computing systems nonprofit organization, known for organizing conferences and publishing research. Prior one of their monthly conferences throughout the year, hundreds of consent forms need to be signed by speakers and authors of conference presentations. The team receives a deluge of forms on a rolling basis that need to be renamed and tracked in a Google Sheet. Renaming forms can take hundreds of hours throughout the year and this script resolved that workload by turning the process into a minute.

This script may need to be modified for use on different forms or forms from different vendors like DocuSign.

## Need to Know

- Expected execution time: Less than a minute.
- User will need to update the filepath in the script so that the script points to the folder where the forms live.
- In its current state, the user will need to run the script on the terminal.

## Guidelines

#### Execution

1. Create a static folder for the forms on your computer locally.
2. Place the PDFs that need to be renamed into the folder.
3. Create a new folder in the forms folder called "script" and place the `pdf_consent_form_renamer.py` into it.
4. Open the `pdf_consent_form_renamer.py` and update the filepath to point to the folder where the consent forms are located.
5. In the terminal, navigate to the "script" folder and run the script using `python pdf_consent_form_renamer.py` in the terminal.
6. The forms will be renamed in less than a minute.

#### Dependencies for execution

1. Python 3 or higher
2. `pip install fitz`
3. `pip install re`
4. `pip install os`
