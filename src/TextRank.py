import os 
from os import walk 
import bs4 as bs
import re 
import nltk 
from gensim.summarization import summarize
from gensim.summarization import keywords


import urllib.request  
import re
import bs4 as bs  
import nltk
import heapq 
import matplotlib.pyplot as plt
import os 
import sys
from os import walk

nltk.download('punkt')
nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')

print("import * read l 1w")

def files_read(path):
    print(f"Reading {path} files..")
    _, _, filenames = next(walk(path), (None, None, []))   # walk --> (current_path, directories in current_path, files in current_path).
    filenames.sort()
    files_per_topic=filenames
    return files_per_topic

def get_filenames(get_files=True):
    if True:
        all_file_names=[]
        for topic in ['business','entertainment','politics','sport','tech']:
            filenames=files_read(os.path.join('bbc_news_corpus/Articles/',topic))
            all_file_names.append(filenames)
    return all_file_names

def read_text(all_file_names,root_path,testing_flag):
    all_articles=[]
    for i in range(len(all_file_names)):
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
            with open(os.path.join(root_path,topic,j),'rb') as f:                   #converted into bytes because of non ascii 
                data=f.read() 
                # print(len(nltk.sent_tokenize(data)))
                f.close()
                if testing_flag==False or testing_flag==True:
                    soup=bs.BeautifulSoup(data,'lxml')
                    text = ""
                    for paragraph in soup.find_all('p'):
                        text += paragraph.text
                    data=text
            # # print(data)
            # print(len(nltk.sent_tokenize(data)))
            # print(nltk.sent_tokenize(data))
                
            # break
        
            # print(len(nltk.sent_tokenize(data)))
            art_per_topic.append(data)
            # print(True)
        all_articles.append(art_per_topic)
    return all_articles

def set_summaries(all_articles,stop_words):

    print("preprocessing..")
    count=0
    summaries=[]
    for topic in all_articles:
        sum_per_topic=[]
        for article in topic:
            temp_text_lower= article.lower()
            clean_text = re.sub(r'[^a-zA-Z0-9.%,\']', ' ', temp_text_lower)  
            clean_text = re.sub(r'\s+',' ',clean_text)
            clean_text=re.sub(r"(?<=\D)\.(?=\S)", ". ", clean_text)  # Adding spaces after each sentence completion i.e. after '.'

            temp=summarize(clean_text,ratio=0.4)
            temp=temp.split("\n")
            
            temp1= ''.join(temp)
            sum_per_topic.append(temp1)
        summaries.append(sum_per_topic)
    return summaries

def write_files(all_file_names,summaries):
    print("writing summaries..")
    for i in range(len(summaries)):
        print(i)
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
        for n_file,n_summ in zip(all_file_names[i],summaries[i]):
            if not os.path.exists(os.path.join("TextRank_summaries/",topic)):
                os.makedirs(os.path.join("TextRank_summaries/",topic))
            with open(os.path.join("TextRank_summaries/",topic,n_file),'w') as f:
                f.write(n_summ)
                f.close()

def main(root_path):
    all_file_names=get_filenames(True)
    all_articles=read_text(all_file_names,root_path,testing_flag=False)

    summaries=set_summaries(all_articles,stop_words)
    print(len(summaries))
    write_files(all_file_names,summaries)

if __name__ == '__main__':
    main('bbc_news_corpus/Articles/')