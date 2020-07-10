from rouge import FilesRouge
import os
from baseline_nltk import files_read,get_filenames,read_text
import nltk
"""
ROUGE-n recall=40% means that 40% of the n-grams in the reference summary are also present in the generated summary.
ROUGE-n precision=40% means that 40% of the n-grams in the generated summary are also present in the reference summary.
ROUGE-n F1-score=40% is more difficult to interpret, like any F1-score.
"""
def precision_unigrams(ref_sum_list,hyp_sum_list):
    
    precision=[]
    recall=[]
    for ref,hyp in zip(ref_sum_list,hyp_sum_list):
        recall_temp=[]
        precision_temp=[]
        for r,h in zip(ref,hyp):            
            r=nltk.word_tokenize(r)
            h=nltk.word_tokenize(h)
            overlap=0
            for i in r:
                if i in h:
                    overlap+=1
            precision_temp.append(overlap/len(h))
            recall_temp.append(overlap/len(r))
        precision.append(precision_temp)
        recall.append(recall_temp)
    return precision,recall

def rouge_fpr(ref_sum_list,gen_sum_list):
    files_rouge = FilesRouge()
    scores=[]
    for ref,gen in zip(ref_sum_list,gen_sum_list):
        tmp=[]
        for r,g in zip(ref,gen):
            tmp.append(files_rouge.get_scores(r,g,avg=True))
        scores.append(tmp)
        print(scores)
        break
    return scores

def main(ref_summary_path,gen_summary_path):
    all_file_names=get_filenames(True)
    """
    For self defined testing..
    """
    ref_sum_list=read_text(all_file_names,ref_summary_path,testing_flag=True)
    hyp_sum_list=read_text(all_file_names,gen_summary_path,testing_flag=True)

    precision,recall=precision_unigrams(ref_sum_list,hyp_sum_list)
    print("Average precision of Business summaries: ",sum(precision[0][:])/len(precision[0][:]))
    print("Average recall of Business summaries: ",sum(recall[0][:])/len(recall[0][:]))

if __name__=='__main__':
    main('bbc_news_corpus/Summaries/','Nltk_summaries/')