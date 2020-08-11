import urllib.request  
import re
import bs4 as bs  
import nltk
import heapq 
import matplotlib.pyplot as plt
import os 
import sys
from os import walk
from baseline_nltk import *

nltk.download('punkt')
nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
sum_length=4

def main(root_path):
    all_file_names=get_filenames(True)
    all_articles=read_text(all_file_names,root_path,testing_flag=False)

    summaries=set_summaries(all_articles,stop_words,sum_length)
    print(len(summaries))
    write_files(all_file_names,summaries)

if __name__ == '__main__':
    main('bbc_news_corpus/Articles/')