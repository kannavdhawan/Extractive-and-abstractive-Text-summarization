from rouge import FilesRouge
import os
from baseline_nltk import files_read,get_filenames,read_text
import nltk

nltk.download('punkt')
nltk.download('stopwords')
"""
ROUGE-n recall=40% means that 40% of the n-grams in the reference summary are also present in the generated summary.
ROUGE-n precision=40% means that 40% of the n-grams in the generated summary are also present in the reference summary.
ROUGE-n F1-score=40% is more difficult to interpret, like any F1-score.
"""
def precision_unigrams(ref_sum_list,hyp_sum_list):
    """
        count 539 instance for all the classses in total where the recall is more than 1. 
        Reason being:
        1. Sentences chosen by sentence scoring algorithm are longer than the sentences in real summary.
        2. Static length of summary is chosen. i.e = 4. 
    """
    count_temp=0
    precision=[]
    recall=[]
    for ref,hyp in zip(ref_sum_list,hyp_sum_list):
        recall_temp=[]
        precision_temp=[]
        for r,h in zip(ref,hyp): 
            r=nltk.word_tokenize(r)
            h=nltk.word_tokenize(h)
            if len(r)<len(h):
                count_temp+=1       
            overlap=0
            for i in h:
                if i in r:
                    overlap+=1
            precision_temp.append(overlap/len(h))
            recall_temp.append(overlap/len(r))
        precision.append(precision_temp)
        recall.append(recall_temp)
    print("count",count_temp)
    return precision,recall

def rouge_fpr(all_file_names,ref_summary_path,hyp_summary_path):
    files_rouge = FilesRouge()
    scores=[]
    count=0
    for ref,hyp in zip(all_file_names,all_file_names):
        if count==0:
            topic="business/"
        elif count==1:
            topic="entertainment/"
        elif count==2:
            topic="politics/"
        elif count==3:
            topic="sport/"
        elif count==4:
            topic="tech/"

        count+=1
        tmp=[]
        for r,h in zip(ref,hyp):
            # print(os.path.join(ref_summary_path,topic,r))
            tmp.append(files_rouge.get_scores(os.path.join(ref_summary_path,topic,r),os.path.join(hyp_summary_path,topic,h),avg=True))
        scores.append(tmp)
        
    return scores

def main(ref_summary_path,hyp_summary_path):
    all_file_names=get_filenames(True)
    """
    Self precision and recall..
    Reading the hypothesis summary and the reference summary into list of list.
    """
    ref_sum_list=read_text(all_file_names,ref_summary_path,testing_flag=True)
    hyp_sum_list=read_text(all_file_names,hyp_summary_path,testing_flag=True)

    precision,recall=precision_unigrams(ref_sum_list,hyp_sum_list)
    print("Average precision of Business summaries: ",sum(precision[0][:])/len(precision[0][:]))
    print("Average recall of Business summaries: ",sum(recall[0][:])/len(recall[0][:]))

    print("Average precision of ENtertainment summaries: ",sum(precision[1][:])/len(precision[1][:]))
    print("Average recall of ENtertainment summaries: ",sum(recall[1][:])/len(recall[1][:]))

    print("Average precision of Politics summaries: ",sum(precision[2][:])/len(precision[2][:]))
    print("Average recall of Politics summaries: ",sum(recall[2][:])/len(recall[2][:]))

    print("Average precision of Sports summaries: ",sum(precision[3][:])/len(precision[3][:]))
    print("Average recall of Sports summaries: ",sum(recall[3][:])/len(recall[3][:]))

    print("Average precision of Tech summaries: ",sum(precision[4][:])/len(precision[4][:]))
    print("Average recall of Tech summaries: ",sum(recall[4][:])/len(recall[4][:]))

    """
    rouge_fpr
    """
    print("inside rouge..")
    scores=rouge_fpr(all_file_names,ref_summary_path,hyp_summary_path)
    print("Rouge score Test.. ")
    print(scores[0][0])
    return precision,recall,scores

if __name__=='__main__':
    main('bbc_news_corpus/Summaries/','Nltk_summaries/')