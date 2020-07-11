import os 
from os import walk 
import bs4 as bs
import re 
import nltk 
import heapq

def files_read(path):
    print("Reading files..")
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

def main():
    pass

if __name__=='__main__':
    main()

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

def set_summaries(all_articles,stop_words,sum_length):

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
            clean_text=re.sub(r"(?<=\D)\.(?=\S)", ". ", clean_text)  # Adding spaces after each sentence completion i.e. after '.'

            
            
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
            
            # clean_text=re.sub(r'\w+\\.\w+','\n',clean_text)
            sentences= nltk.sent_tokenize(clean_text)
            
            # print(len(sentences))
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
            if not os.path.exists(os.path.join("Nltk_summaries/",topic)):
                os.makedirs(os.path.join("Nltk_summaries/",topic))
            with open(os.path.join("Nltk_summaries/",topic,n_file),'w') as f:
                f.write(n_summ)
                f.close()