from rouge import FilesRouge
import os
from baseline_nltk import files_read,get_filenames
files_rouge = FilesRouge()
all_file_names=get_filenames(True)
print(all_file_names)
"""
ROUGE-n recall=40% means that 40% of the n-grams in the reference summary are also present in the generated summary.
ROUGE-n precision=40% means that 40% of the n-grams in the generated summary are also present in the reference summary.
ROUGE-n F1-score=40% is more difficult to interpret, like any F1-score.
"""
# scores = files_rouge.get_scores(,os.path.join('bbc_news_corpus/Summaries/business/','001.txt'),avg=True)
# print(scores)
