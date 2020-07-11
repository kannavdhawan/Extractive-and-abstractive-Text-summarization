import urllib.request  
import re
import bs4 as bs  
import nltk
import heapq 
import matplotlib.pyplot as plt
import os 
import sys
from os import walk
import itertools
import pandas as pd 

nltk.download('punkt')
nltk.download('stopwords')

stop_words = nltk.corpus.stopwords.words('english')
sum_length=5
print("Reading files..")
def files_read(path):
    _, _, filenames = next(walk(path), (None, None, []))
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
all_file_names=get_filenames(True)

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
print("preprocessing..")
count=0
summaries=[]
for topic in all_articles:
    sum_per_topic=[]
    # processed_article=[]
    for article in topic:
        temp_text_lower= article.lower()
        # clean_text = re.sub(r'\[[0-9]*\]',' ',temp_text_lower)
        # clean_text = re.sub(r'(\n+)','.',temp_text_lower)
        clean_text = re.sub(r'[^a-zA-Z0-9.%,\']', ' ', temp_text_lower)  
        clean_text = re.sub(r'\s+',' ',clean_text)
        clean_text=re.sub(r"(?<=\D)\.(?=\S)", ". ", clean_text)
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
print("writing summaries..")
for i in range(len(summaries)):
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
        if not os.path.exists(os.path.join("Nltk_summaries/",topic)):
            os.makedirs(os.path.join("Nltk_summaries/",topic))
        with open(os.path.join("Nltk_summaries/",topic,n_file),'w') as f:
            f.write(n_summ)
            f.close()

# prec, acc


def precision_unigrams(ref_sum_list,hyp_sum_list):
    
    precision=[]
    recall=[]
    for ref,hyp in zip(ref_sum_list,hyp_sum_list):
        recall_temp=[]
        precision_temp=[]
        for r,h in zip(ref,hyp):            
            r=nltk.word_tokenize(r)
            h=nltk.word_tokenize(h)
            overlap=0
            for i in h:
                if i in r:
                    overlap+=1
            precision_temp.append(overlap/len(h))
            recall_temp.append(overlap/len(r))
        precision.append(precision_temp)
        recall.append(recall_temp)
    return precision,recall


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
                f.close()
                if testing_flag==False or testing_flag==True:
                    soup=bs.BeautifulSoup(data,'lxml')
                    text = ""
                    for paragraph in soup.find_all('p'):
                        text += paragraph.text
                    data=text
            art_per_topic.append(data)
            # print(True)
        all_articles.append(art_per_topic)
    return all_articles
ref_sum_list=read_text(all_file_names,'bbc_news_corpus/Summaries/',testing_flag=True)

precision,recall=precision_unigrams(ref_sum_list,summaries)
print("Average precision of Business summaries: ",sum(precision[0][:])/len(precision[0][:]))
print("Average recall of Business summaries: ",sum(recall[0][:])/len(recall[0][:]))

print("Average precision of ENtertainment summaries: ",sum(precision[1][:])/len(precision[1][:]))
print("Average recall of ENtertainment summaries: ",sum(recall[1][:])/len(recall[1][:]))

print("Average precision of Politics summaries: ",sum(precision[2][:])/len(precision[2][:]))
print("Average recall of Politics summaries: ",sum(recall[2][:])/len(recall[2][:]))

print("Average precision of Sports summaries: ",sum(precision[3][:])/len(precision[3][:]))
print("Average recall of Sports summaries: ",sum(recall[3][:])/len(recall[3][:]))

print("Average precision of Tech summaries: ",sum(precision[4][:])/len(precision[4][:]))
print("Average recall of Tech summaries: ",sum(recall[4][:])/len(recall[4][:]))

from rouge import FilesRouge

def rouge_fpr(all_file_names,ref_summary_path,hyp_summary_path):
    files_rouge = FilesRouge()
    scores=[]
    count=0

    for ref,hyp in zip(all_file_names,all_file_names):
        if count==0:
            topic="business/"
        elif count==1:
            topic="entertainment/"
        elif count==2:
            topic="politics/"
        elif count==3:
            topic="sport/"
        elif count==4:
            topic="tech/"
        count+=1
        tmp=[]
        for r,h in zip(ref,hyp):
            
            tmp.append(files_rouge.get_scores(os.path.join(ref_summary_path,topic,r),os.path.join(hyp_summary_path,topic,h),avg=True))
        scores.append(tmp)
        
    return scores
scores=rouge_fpr(all_file_names,'bbc_news_corpus/Summaries/','Nltk_summaries/')
print("Rouge score")
print(scores[0][0])


# creating dataframe 

precision_df=pd.DataFrame((_ for _ in itertools.zip_longest(*precision)), columns=['Business', 'Entertainment', 'Politics','Sport','Tech'])
recall_df=pd.DataFrame((_ for _ in itertools.zip_longest(*recall)), columns=['Business', 'Entertainment', 'Politics','Sport','Tech'])
precision_df.to_csv("precision_df.csv")
recall_df.to_csv("recall_df.csv")

#saving scores
import pickle

with open('list_scores.pkl', 'wb') as f:  
    pickle.dump(scores,f)
