# Wikipedia scraper
import bs4 as bs  
import urllib.request  
import re
import nltk
import heapq 
import matplotlib.pyplot as plt
nltk.download('punkt')
nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')

page= urllib.request.urlopen("https://en.wikipedia.org/wiki/Artificial_neural_network").read()
soup= bs.BeautifulSoup(page,'lxml')

text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

text_lower= text.lower()
clean_text = re.sub(r'\[[0-9]*\]',' ',text_lower)            
clean_text = re.sub('[^a-zA-Z.]', ' ', clean_text )  
clean_text = re.sub(r'\d',' ',clean_text)
clean_text = re.sub(r'\s+',' ',clean_text)
sentences = nltk.sent_tokenize(clean_text)
# print("***************************************************************************************************************************")
# print(sentences)


# making the dict for word count and calculating the weighted histogram 
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
print(word_count)


# url_topull = input('Enter t`he Wikipedia URL to pull - ')
# sent_num = int(input('How many sentences long do you want your summary to be? (min recommended =10) '))

# scraped_data = urllib.request.urlopen(url_topull)  
# print(scraped_data)
# article = scraped_data.read()
# print(article)
# parsed_article = bs.BeautifulSoup(article,'lxml')

# paragraphs = parsed_article.find_all('p')

# article_text = ""

# for p in paragraphs:  
#     article_text += p.text

# print("Data pull done")
# article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
# article_text = re.sub(r'\s+', ' ', article_text)  

# formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
# formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

# sentence_list = nltk.sent_tokenize(article_text)  

# stopwords = nltk.corpus.stopwords.words('english')

# print("Text pre-processing pull done")
# word_frequencies = {}  
# for word in nltk.word_tokenize(formatted_article_text):  
#     if word not in stopwords:
#         if word not in word_frequencies.keys():
#             word_frequencies[word] = 1
#         else:
#             word_frequencies[word] += 1

# maximum_frequncy = max(word_frequencies.values())

# for word in word_frequencies.keys():  
#     word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

# print("Word Frequencies determined")

# sentence_scores = {}  
# for sent in sentence_list:  
#     for word in nltk.word_tokenize(sent.lower()):
#         if word in word_frequencies.keys():
#             if len(sent.split(' ')) < 30:
#                 if sent not in sentence_scores.keys():
#                     sentence_scores[sent] = word_frequencies[word]
#                 else:
#                     sentence_scores[sent] += word_frequencies[word]

# summary_sentences = heapq.nlargest(sent_num, sentence_scores, key=sentence_scores.get)

# print("=================================SUMMARY==============================")
# summary = ' '.join(summary_sentences)  
# print(summary) 