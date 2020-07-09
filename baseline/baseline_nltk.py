import urllib.request  
import re
import bs4 as bs  
# remove \n check results by printing everything.
import nltk
import heapq 
import matplotlib.pyplot as plt
import os 
import sys
from os import walk
nltk.download('punkt')
nltk.download('stopwords')

stop_words = nltk.corpus.stopwords.words('english')
sum_length=5
def files_read(path):
    # files_per_topic=[]
    _, _, filenames = next(walk(path), (None, None, []))
    filenames.sort()
    files_per_topic=filenames
    return files_per_topic

all_file_names=[]
for topic in ['business','entertainment','politics','sport','tech']:
    filenames=files_read(os.path.join('bbc_news_corpus/Articles/',topic))
    all_file_names.append(filenames)

all_articles=[]
for i in range(len(all_file_names)):
    # print(i)
    art_per_topic=[]
    if i==0:
        topic='business/'
    elif i==1:
        topic='entertainment/'
    elif i==2:
        topic='politics/'
    elif i==3:
        topic='sport/'
    elif i==4:
        topic='tech/'
    for j in all_file_names[i]:
        with open(os.path.join('bbc_news_corpus/Articles/',topic,j),'rb') as f:                   #converted into bytes because of non ascii 
            data=f.read() 
            f.close()
            soup=bs.BeautifulSoup(data,'lxml')
            text = ""
            for paragraph in soup.find_all('p'):
                text += paragraph.text
        art_per_topic.append(text)
        # print(True)
    all_articles.append(art_per_topic)

count=0
summaries=[]
for topic in all_articles:
    sum_per_topic=[]
    # processed_article=[]
    for article in topic:
        temp_text_lower= article.lower()
        # clean_text = re.sub(r'\[[0-9]*\]',' ',temp_text_lower)
        # clean_text = re.sub(r'(\n+)','.',temp_text_lower)
        clean_text = re.sub('[^a-zA-Z0-9.]', ' ', temp_text_lower )  
        clean_text = re.sub(r'\s+',' ',clean_text)
        
        sentences= nltk.sent_tokenize(clean_text)
        
        word_count=dict()
        tokenized_words=nltk.word_tokenize(clean_text)
        for word in tokenized_words:
            if word not in stop_words:
                if word not in word_count.keys():
                    word_count[word]=1
                else:
                    word_count[word]+=1
        maximum=max(word_count.values())
        for word in word_count.keys():
            word_count[word]=word_count[word]/maximum

        sent_score=dict()
        for sent in sentences:      
            tokens_per_sent=nltk.word_tokenize(sent)   
            for word in tokens_per_sent: 
                if word in word_count.keys():
                    if sent not in sent_score:
                        sent_score[sent]=word_count[word]
                    else:
                        sent_score[sent]+=word_count[word] 
        top_sent= heapq.nlargest(sum_length,sent_score,key=sent_score.get)
        summary = ' '.join(top_sent) 
        sum_per_topic.append(summary)
    summaries.append(sum_per_topic)
for i in range(len(summaries)):
    # print(i)
    art_per_topic=[]
    if i==0:
        topic='business/'
    elif i==1:
        topic='entertainment/'
    elif i==2:
        topic='politics/'
    elif i==3:
        topic='sport/'
    elif i==4:
        topic='tech/'

    for summ in topic:
        with open(os.path.join("Nltk_summaries/",topic,)
        
        # if count<1:
        #     print(summary)
        #     count+=1

