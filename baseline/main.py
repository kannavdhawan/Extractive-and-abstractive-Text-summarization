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
sum_length=5 

def main():
    all_file_names=get_filenames(True)
    all_articles=read_articles(all_file_names)
    sumamries=get_summaries(all_articles,stop_words,sum_length)
    write_files(all_file_names,summaries)

    # print(all_file_names)


if __name__ == '__main__':
    main()