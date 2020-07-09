# Wikipedia scraper
import bs4 as bs  
import urllib.request  
import re
import nltk
import heapq 
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import os 
import sys
from os import walk

nltk.download('punkt')
nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')

def files_read(path):
    file_names=[]
    _, _, filenames = next(walk(path), (None, None, []))
    file_names.extend(filenames)
    return file_names

all_files=[]
for topic in ['business','entertainment','politics','sport','tech']:
    filenames=files_read(os.path.join('bbc_news_corpus/Articles/',topic))
    all_files.append(filenames)

all_articles=[]
for i in range(len(all_files)):
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
    for j in all_files[i]:
        with open(os.path.join('bbc_news_corpus/Articles/',topic,j)) as f:
            article_text=f.read()
            


        # f.close()

# page= urllib.request.urlopen("https://en.wikipedia.org/wiki/Artificial_neural_network").read()
# soup= bs.BeautifulSoup(page,'lxml')

# text = ""
# for paragraph in soup.find_all('p'):
#     text += paragraph.text

# text_lower= text.lower()
# clean_text = re.sub(r'\[[0-9]*\]',' ',text_lower)            
# clean_text = re.sub('[^a-zA-Z0-9.]', ' ', clean_text )  
# # clean_text = re.sub(r'\d',' ',clean_text)
# clean_text = re.sub(r'\s+',' ',clean_text)
# sentences = nltk.sent_tokenize(clean_text)
# # making the dict for word count and calculating the weighted histogram 
# word_count=dict()

# tokenized_words=nltk.word_tokenize(clean_text)
# for word in tokenized_words:
#     if word not in stop_words:
#         if word not in word_count.keys():
#             word_count[word]=1
#         else:
#             word_count[word]+=1
# maximum=max(word_count.values())
# for word in word_count.keys():
#     word_count[word]=word_count[word]/maximum
# # print(word_count)

# # Create and generate a word cloud image:
# wordcloud = WordCloud().generate_from_frequencies(word_count)

# # Display the generated image:
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
# plt.savefig('word_count.png')

# #sentence scoring
# sent_score=dict()
# for sent in sentences:      #['I am kannav dhawan','I am kannavdhawan']
#     tokens_per_sent=nltk.word_tokenize(sent)    #['I','am','kannav','dhawan']
#     for word in tokens_per_sent: #I
#         if word in word_count.keys():#
#             if sent not in sent_score:
#                 sent_score[sent]=word_count[word]
#             else:
#                 sent_score[sent]+=word_count[word] #
# top_sent= heapq.nlargest(3,sent_score,key=sent_score.get)
# summary = ' '.join(top_sent) 
# print(summary)