import os
import nltk
with open(os.path.join('Nltk_summaries/business/','001.txt')) as f:
    gen_sum=f.read()
    gen_sum=nltk.word_tokenize(gen_sum)
with open(os.path.join('bbc_news_corpus/Summaries/business/','001.txt')) as f:
    real_sum=f.read()
    real_sum=nltk.word_tokenize(real_sum)
# print(gen_sum)
# print(real_sum)
"""
recall: overlap/len(real_sum), TruePositives / (TruePositives+FalseNegatives) denotes all pos in whole dataset. 
precision: overlap/len(gen_sum), true_pos/(true_pos+false_pos) denotes all pos predicted by predictor. 
"""
overlap=0
for i in gen_sum:
    if i in real_sum:
        overlap+=1
print("overlap: ",overlap)
print("len of generated summ: ",len(gen_sum))
print("precision: ",overlap/len(gen_sum))