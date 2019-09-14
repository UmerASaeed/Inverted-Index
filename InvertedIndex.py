import os
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import uuid
from os import listdir
from os.path import isfile, join
import glob

unique_file=-1
unique_term=-1
array=[]
Tokens=[]
Stem_Tokens=[]
Term_ids=[]
file_array=[]
ps = PorterStemmer()

def get_text_bs(html):
    tree = BeautifulSoup(html, 'lxml')

    body = tree.body
    if body is None:
        return None

    for tag in body.select('script'):
        tag.decompose()
    for tag in body.select('style'):
        tag.decompose()

    text = body.get_text(separator='\n')
    return text

mypath="C:\\Users\\umers\\OneDrive\\Desktop\\corpus\\corpus"

filenames = onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

f=open(mypath + "\\" + filenames[0])


stopfile= open(r"C:\Users\umers\OneDrive\Desktop\corpus\stoplist (1).txt","r")
stpwords = stopfile.read()
stop_words = str(stpwords)
stop_words = stop_words.splitlines()

for files in filenames:
    f1 = open(mypath + "\\" + files, "r",errors='ignore')
    line = f1.readline()
    while line:
        if ('<!DOCTYPE html' in line):
            break
        line.strip()
        line = f1.readline()

    data = f1.read()

    filteredText = str(get_text_bs(data))
    text = os.linesep.join([s for s in filteredText.splitlines() if s])
    text1 = str(text)
    text1 = text1.splitlines()

    tokenized_sents = [word_tokenize(i) for i in text1]
    for j in tokenized_sents:
        if [] in j:
            tokenized_sents.remove()

    for k in tokenized_sents:
        for l in k:
            if l.isalnum():
                array.append(l)

    for item in array:
        Tokens.append(item.lower())


    for item in Tokens:
        for element in stop_words:
            if element == item:
                Tokens.remove(item)

    for item in Tokens:
        Stem_Tokens.append(ps.stem(item))

    file = ''
    filename = str(f1)
    for i in range(78, 102):
        file = file + filename[i]

    file = str(unique_file + 1) + "/" + file
    unique_file=unique_file+1
    file_array.append(file)

    for i in Stem_Tokens:
        Term_ids.append(str(unique_term + 1) + '/' + i)
        unique_term = unique_term + 1
    array = []
    Tokens = []
    Stem_Tokens = []

f=open(r"C:\Users\umers\OneDrive\Desktop\corpus\TermIds.txt","x",encoding='utf-8',errors='ignore')
for item in Term_ids:
    f.write(item + "\n" )



