import os
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stopfile=open(r"C:\Users\umers\OneDrive\Desktop\Test\stoplist (1).txt","r")
f1=open(r"C:\Users\umers\OneDrive\Desktop\corpus\corpus\clueweb12-0000tw-35-20780","r")
line=f1.readline()
while line:
    if ('<!DOCTYPE html' in line):
        break
    line.strip()
    line=f1.readline()

data=f1.read()


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



filteredText=str(get_text_bs(data))
text = os.linesep.join([s for s in filteredText.splitlines() if s])
text1=str(text)
text1=text1.splitlines()

tokenized_sents = [word_tokenize(i) for i in text1]
for j in tokenized_sents:
    if [] in j:
        tokenized_sents.remove()

array=[]
for k in tokenized_sents:
    for l in k:
        if l.isalnum():
            array.append(l)

Tokens=[]
for item in array:
    Tokens.append(item.lower())

stpwords=stopfile.read()
stop_words=str(stpwords)
stop_words=stop_words.splitlines()

for item in Tokens:
    for element in stop_words:
        if element == item:
            Tokens.remove(item)

ps = PorterStemmer()

Stem_Tokens=[]
for item in Tokens:
    Stem_Tokens.append(ps.stem(item))


