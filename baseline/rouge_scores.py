from rouge import FilesRouge
import os
files_rouge = FilesRouge()

"""
ROUGE-n recall=40% means that 40% of the n-grams in the reference summary are also present in the generated summary.
ROUGE-n precision=40% means that 40% of the n-grams in the generated summary are also present in the reference summary.
ROUGE-n F1-score=40% is more difficult to interpret, like any F1-score.
"""
scores = files_rouge.get_scores(os.path.join('Nltk_summaries/business/','001.txt'),os.path.join('bbc_news_corpus/Summaries/business/','001.txt'),avg=True)
print(scores)
