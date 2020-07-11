
# Wikipedia scraper
import bs4 as bs  
import urllib.request  
import re
import nltk
import heapq 
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
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
clean_text = re.sub('[^a-zA-Z0-9.]', ' ', clean_text )  
# clean_text = re.sub(r'\d',' ',clean_text)
clean_text = re.sub(r'\s+',' ',clean_text)
sentences = nltk.sent_tokenize(clean_text)
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
# print(word_count)

# Create and generate a word cloud image:
wordcloud = WordCloud().generate_from_frequencies(word_count)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig('word_count.png')

#sentence scoring
sent_score=dict()
for sent in sentences:      #['I am kannav dhawan','I am kannavdhawan']
    tokens_per_sent=nltk.word_tokenize(sent)    #['I','am','kannav','dhawan']
    for word in tokens_per_sent: #I
        if word in word_count.keys():#
            if sent not in sent_score:
                sent_score[sent]=word_count[word]
            else:
                sent_score[sent]+=word_count[word] #
top_sent= heapq.nlargest(3,sent_score,key=sent_score.get)
summary = ' '.join(top_sent) 
print(summary)