#This code was created for USENIX to rename hundreds of consent forms received
#from speakers and authors prior to conferences via HelloSign. The code is specific to
#HelloSign PDFs and would need to be modified for DocuSign or other signing software.

import fitz
import re
import os
from collections import defaultdict

#Update the filepath in this field based on where the PDFs are placed
os.chdir('/PLACE/FILEPATH/HERE/') 
nameCounter = defaultdict(list)
lastnameCounter = defaultdict(int) 

#Targets only the PDFs in the folder and opens them to retrieve text.
for filepath in os.listdir():
    if filepath[-4:]!='.pdf': 
        continue
    text = ''
    with fitz.open(filepath) as doc:
        for page in doc:
            text+= page.getText() 

    #Locates full names and splits them into first and last name variables.
    fullname = re.findall('\n(.*?)\nDoc ID', text)[-1] 
    firstname = fullname.split()[0] 
    lastname = fullname.split()[-1]
    
    #Adds the first and last names to dictionaries and keep track of the number of occurences of a duplicate last names.
    nameCounter[(firstname, lastname)].append(filepath) 
    lastnameCounter[lastname]+=1 

#Renames the forms and if there are duplicate last names, begins a counter to append sequential numbers for each.
for (firstname, lastname), files in nameCounter.items():
    for i, file in enumerate(files):
        if lastnameCounter[lastname]>1 or len(files)>1:
            newfile = lastname.lower()+'_'+firstname.lower()+'_'+str(i+1)+'.pdf'
        else:
            newfile = lastname.lower()+'_'+firstname.lower()+'.pdf' 
        if os.path.exists(newfile): 
            print(f'File {newfile} already exists! Skipping {firstname} {lastname}')
        else:
            os.rename(file, newfile)
