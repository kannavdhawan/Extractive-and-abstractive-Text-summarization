import bs4 as bs  
import re
import nltk
import heapq 
nltk.download('punkt')
nltk.download('stopwords')

                                                            with open('../input/bbc-news-summary/BBC News Summary/News Articles/business/001.txt') as f:
                                                                article = f.read()
# print(article_text)
# print("Data pull done")
article = re.sub(r'\[[0-9]*\]', ' ', article)  
article_text = re.sub(r'\s+', ' ', article)  
# print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")

formatted_article_text = re.sub('[^a-zA-Z.]', ' ', article_text )  
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
# print(type(formatted_article_text))
# print(formatted_article_text)
sentence_list = nltk.sent_tokenize(formatted_article_text)  
print(sentence_list)
stopwords = nltk.corpus.stopwords.words('english')

print("Text pre-processing pull done")
word_frequencies = {}  
for word in nltk.word_tokenize(formatted_article_text):  
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():  
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

print("Word Frequencies determined")

sentence_scores = {}  
for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

summary_sentences = heapq.nlargest(10, sentence_scores, key=sentence_scores.get)

print("J**********************************************L")
print(summary_sentences)
print("=================================SUMMARY==============================")
summary = ' '.join(summary_sentences)  
with open('001so.txt','w') as g:
    g.write(summary)
print(summary)