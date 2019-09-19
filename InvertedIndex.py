import os
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from os import listdir
from os.path import isfile, join

unique_file=-1
unique_term=0
unique_terms=0
unique_term_II=0
temp_file=-1
array=[]
Tokens=[]
Stem_Tokens=[]
Term_ids=[]
file_array=[]
ps = PorterStemmer()
res = []
dict={}
Terms={}
TermCount={}

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
stopfile= open(r"C:\Users\umers\OneDrive\Desktop\corpus\stoplist (1).txt","r")
stpwords = stopfile.read()
stop_words = str(stpwords)
stop_words = stop_words.splitlines()
stopfile.close()

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
            if l.isalpha():
                array.append(l)

    for item in array:
        Tokens.append(item.lower())
    flag = 1
    values = 0

    for item in range(Tokens.__len__()):
        if flag == 1:
            if values > 0:
                item = item - values
        if flag == 0:
            item = item - values
            flag = 1
        for element in stop_words:
            if element == Tokens[item]:
                Tokens.remove(Tokens[item])
                values = values + 1
                flag = 0
                break

    for item in Tokens:
        Stem_Tokens.append(ps.stem(item))

    file = ''
    filename = str(f1)
    for i in range(78, 102):
        file = file + filename[i]


    for x in Stem_Tokens:
        if x not in res:
            TermCount[x]=1
            res.append(x)
        elif x in res:
            TermCount[x]=TermCount[x]+1

    for i in res:
        if i=='http':
            res.remove(i)

    file = str(unique_file+1) + "/" + file
    file_array.append(file)

    for i in res:
        Term_ids.append (i)
        if i not in dict:
            dict[i] = []
            dict[i].append((unique_file + 1,unique_term_II+1))
        elif unique_file != temp_file:
            dict[i].append((unique_file + 1,unique_term_II+1))
        unique_term_II=unique_term_II+1
    unique_term_II=0
    temp_file = unique_file
    unique_file = unique_file + 1
    array = []
    Tokens = []
    Stem_Tokens = []
    res = []
    f1.close()


print('out')
final_terms=[]


for x in Term_ids:
    if x not in final_terms:
        final_terms.append(x)
    elif x in final_terms:
        TermCount[x]=TermCount[x]+1



f=open(r"C:\Users\umers\OneDrive\Desktop\corpus\docids.txt","x",encoding='utf-8')
for item in file_array:
    f.write(item + "\n" )

f.close()

f=open(r"C:\Users\umers\OneDrive\Desktop\corpus\TermIds.txt","x",encoding='utf-8')
for item in final_terms:
    f.write(str(unique_term) + "/" + item + '\n')
    unique_term=unique_term+1

f.close()

f=open(r"C:\Users\umers\OneDrive\Desktop\corpus\term_index.txt","x",encoding='utf-8')
for key,value in dict.items():
    f.write((str(unique_terms) +" "+str (TermCount[key]) +" "+ str(dict[key].__len__())+" "+str(value) + os.linesep))
    Terms[key]=unique_terms
    unique_terms=unique_terms+1

f.close()

while(1):
    x=input("Enter the term you want to Search: ")
    print("Listing for Term: " + x)
    stemmed=ps.stem(x)
    print("TERMID: "+ str(Terms[stemmed]))
    print("Number of documents containing term: " + str(dict[stemmed].__len__()))
    print("Term frequency in corpus: "+ str(TermCount[stemmed]))
    print(os.linesep)

