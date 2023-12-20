#This code was created for USENIX to rename hundreds of consent forms received
#from speakers and authors prior to conferences via HelloSign. The code is specific to
#HelloSign PDFs and would need to be modified for DocuSign or other signing software.

import fitz
import re
import os
from collections import defaultdict
os.chdir('/PLACE/FILEPATH/HERE/') #Update filepath based on where PDFs are placed
nameCounter = defaultdict(list)
lastnameCounter = defaultdict(int) #using int as default value to keep track of duplicate last names
for filepath in os.listdir():
    if filepath[-4:]!='.pdf': #target only PDFs in the folder
        continue
    text = ''
    with fitz.open(filepath) as doc:
        for page in doc:
            text+= page.getText() #get all of the text from the PDF
    fullname = re.findall('\n(.*?)\nDoc ID', text)[-1] #locate fullname on HelloSign consent forms
    firstname = fullname.split()[0] #split name into first and last name variables for formatting
    lastname = fullname.split()[-1]
    nameCounter[(firstname, lastname)].append(filepath) #add the first and last name to nameCounter and lastnameCounter dictionaries
    lastnameCounter[lastname]+=1 #keeping track of occurrences of a specific lastname
for (firstname, lastname), files in nameCounter.items():
    for i, file in enumerate(files):
        if lastnameCounter[lastname]>1 or len(files)>1:
            newfile = lastname.lower()+'_'+firstname.lower()+'_'+str(i+1)+'.pdf' #if there are duplicate lastnames, script will begin a counter and append sequential numbers for each
        else:
            newfile = lastname.lower()+'_'+firstname.lower()+'.pdf' #otherwise will rename all pdfs as lastname_firstname.pdf
        if os.path.exists(newfile): #and if the file already exists, it'll skip the file so it is not deleted
            print(f'File {newfile} already exists! Skipping {firstname} {lastname}')
        else:
            os.rename(file, newfile)
