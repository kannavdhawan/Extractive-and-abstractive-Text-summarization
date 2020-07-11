# import pandas as pd
# prec=pd.read_csv("Data_files/precision_nltk.csv").iloc[:,1:]
# print(prec.head())
# print(prec[['Business']])
import bs4 as bs 
import os 
import nltk 
nltk.download('punkt')

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
print(len(nltk.sent_tokenize(data)))
print(nltk.sent_tokenize(data))
    