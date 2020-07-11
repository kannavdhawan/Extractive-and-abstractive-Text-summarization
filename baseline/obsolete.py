# import pandas as pd
# prec=pd.read_csv("Data_files/precision_nltk.csv").iloc[:,1:]
# print(prec.head())
# print(prec[['Business']])
# import bs4 as bs 
# import os 
# import nltk 
# nltk.download('punkt')
# import re 

# with open(os.path.join("bbc_news_corpus/Summaries/business/001.txt"),'rb') as f:                   #converted into bytes because of non ascii 
#     data=f.read() 
#     # print(len(nltk.sent_tokenize(data)))
#     f.close()
#     soup=bs.BeautifulSoup(data,'lxml')
#     text = ""
#     for paragraph in soup.find_all('p'):
#         text += paragraph.text
#         data=text
# print(data)
# data = re.sub(r'[^a-zA-Z0-9.%,\']', ' ', data) 

# data=re.sub(r"(?<=\D)\.(?=\S)", ". ", data)


# # data=re.sub('\w\\.\w','\n',data)
# print(data)
# # print(len(data))
# print(nltk.sent_tokenize(data))
# print(len(nltk.sent_tokenize(data)))



"""
sent_tokenize: tokenizes when there is a space after full stop.
"""
# import nltk
# sentence_data= "TimeWarner said fourth quarter sales rose 2% to $11.1bn from $10.9bn. For the full-year, TimeWarner posted a profit of $3.36bn, up 27% from its 2003 performance, while revenues grew 6.4% to $42.09bn."
# nltk_tokens= nltk.sent_tokenize(sentence_data)
# print(nltk_tokens)

"""
Adding space after the full stop. 
"""
# import re

# s = "Text.Text2.Text3."
# result = re.sub(r"(?<=\D)\.(?=\S)", ". ", s)
# print(result)