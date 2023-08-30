import fitz
import re
import os
from collections import defaultdict
os.chdir('/PLACE/FILEPATH/HERE/')
nameCounter = defaultdict(list)
lastnameCounter = defaultdict(int)
for filepath in os.listdir():
    if filepath[-4:]!='.pdf':
        continue
    text = ''
    with fitz.open(filepath) as doc:
        for page in doc:
            text+= page.getText()
    fullname = re.findall('\n(.*?)\nDoc ID', text)[-1]
    firstname = fullname.split()[0]
    lastname = fullname.split()[-1]
    nameCounter[(firstname, lastname)].append(filepath)
    lastnameCounter[lastname]+=1
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
