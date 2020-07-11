# import pandas as pd
# prec=pd.read_csv("Data_files/precision_nltk.csv").iloc[:,1:]
# print(prec.head())
# print(prec[['Business']])
import bs4 as bs 
import os 
import nltk 
nltk.download('punkt')
import re 

with open(os.path.join("bbc_news_corpus/Summaries/business/001.txt"),'rb') as f:                   #converted into bytes because of non ascii 
    data=f.read() 
    # print(len(nltk.sent_tokenize(data)))
    f.close()
    soup=bs.BeautifulSoup(data,'lxml')
    text = ""
    for paragraph in soup.find_all('p'):
        text += paragraph.text
        data=text
print(data)
data = re.sub('[^a-zA-Z0-9.]', ' ', data) 
# data=re.sub('\w\\.\w','\n',data)
data=re.split('\D\\.\D', data) 

print(data)
# print(len(data))
# print(len(nltk.sent_tokenize(data)))
# print(nltk.sent_tokenize(data))
    