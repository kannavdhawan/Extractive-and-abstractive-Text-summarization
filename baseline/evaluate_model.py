import rouge_scores
import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 
import itertools
import pickle 
def generate_imgs(precision_path,recall_path):

    precision_df=pd.read_csv(precision_path).iloc[:,1:]
    recall_df=pd.read_csv(recall_path).iloc[:,1:]
    print("Precision")
    print(precision_df.head())
    print("Recall")
    print(recall_df.head())
    y=pd.DataFrame(np.arange(precision_df.shape[0]))

    for metric_str,metric_ob in zip(["Precision","Recall"],[precision_df,recall_df]):
    # precisions
        fig, axs = plt.subplots(3,2)
        for i in ['Business', 'Entertainment', 'Politics','Sport','Tech']:

            if i=='Business':
                axs[0,0].plot(metric_ob[[i]])
                axs[0,0].grid()
                axs[0,0].set_title('Business Summaries')

            if i=='Entertainment':
                axs[0,1].plot(metric_ob[[i]])
                axs[0,1].grid()
                axs[0,1].set_title('Entertainment Summaries')

            if i=='Politics':
                axs[1,0].plot(metric_ob[[i]])
                axs[1,0].grid()
                axs[1,0].set_title('Politics Summaries')

            if i=='Sport':
                axs[1,1].plot(metric_ob[[i]])
                axs[1,1].grid()
                axs[1,1].set_title('Sport Summaries')

            if i=='Tech':
                axs[2,0].plot(metric_ob[[i]])
                axs[2,0].grid()
                axs[2,0].set_title('Tech Summaries')
        if metric_str=="Precision":
            plt.suptitle('Nltk Precision')
        else:
            plt.suptitle('Nltk Recall')
        plt.tight_layout(rect=[0, 0, 1, 0.95])

        plot_path=os.path.join("Plots/")
        if not os.path.exists(plot_path):
            os.makedirs(plot_path)
        if metric_str=="Precision":
            fig.savefig(os.path.join("Plots/","Precision_nltk.png"))            
        else:
            fig.savefig(os.path.join("Plots/","Recall_nltk.png"))
        
        # plt.show()

def scores_calc(rouge,metric,scores):
    outer_list=[]
    for topic in scores:
        inner_list=[]
        for article in topic:
            f1_tmp=article[rouge][metric]
            inner_list.append(f1_tmp)   
        outer_list.append(inner_list)
    return outer_list

def average_rouge(itr):
    metric_common=[]
    for i in range(5):
        temp=sum(itr[i])/len(itr[i])
        metric_common.append(temp)
    return metric_common

def calculate_mean_score_plots(score):
    """
    Input scores from Rouge 
    Returns:
            Mean of Precision and for Rouge-1, Rouge-2 and Rouge-L 
            Mean of Recall for Rouge-1, Rouge-2 and Rouge-L
            Mean of F-1 Score for Rouge-1, Rouge-2 and Rouge-L
    """
    with open(os.path.join("Data_files/","list_scores.pkl"),'rb') as f:
        scores=pickle.load(f)
    #Rouge-1
    f1_r1=scores_calc('rouge-1','f',scores)
    p_r1=scores_calc('rouge-1','p',scores)
    r_r1=scores_calc('rouge-1','r',scores)
    #Rouge-2
    f1_r2=scores_calc('rouge-2','f',scores)
    p_r2=scores_calc('rouge-2','p',scores)
    r_r2=scores_calc('rouge-2','r',scores)
    #Rouge-L
    f1_rL=scores_calc('rouge-l','f',scores)
    p_rL=scores_calc('rouge-l','p',scores)
    r_rL=scores_calc('rouge-l','r',scores)

    """
    Appending the mean for all the topics in single list. 
    """
    #Rouge-1
    f_r1_avg_all_topics=average_rouge(f1_r1)
    p_r1_avg_all_topics=average_rouge(p_r1)
    r_r1_avg_all_topics=average_rouge(r_r1)
    #Rouge-2
    f_r2_avg_all_topics=average_rouge(f1_r2)
    p_r2_avg_all_topics=average_rouge(p_r2)
    r_r2_avg_all_topics=average_rouge(r_r2)
    #Rouge-L
    f_rL_avg_all_topics=average_rouge(f1_rL)
    p_rL_avg_all_topics=average_rouge(p_rL)
    r_rL_avg_all_topics=average_rouge(r_rL)

    """
    Creating dataframe 
    """

    rouge_list=['Rouge 1', 'Rouge 2', 'Rouge L']

    f_score=pd.DataFrame([f_r1_avg_all_topics,f_r2_avg_all_topics,f_rL_avg_all_topics],columns=['Business',\
        'Entertainment','Politics','Sport','Tech'])
    f_score.index = rouge_list
    print(f_score)

    p_score=pd.DataFrame([p_r1_avg_all_topics,p_r2_avg_all_topics,p_rL_avg_all_topics],columns=['Business',\
        'Entertainment','Politics','Sport','Tech'])
    p_score.index = rouge_list
    print(p_score)
    r_score=pd.DataFrame([r_r1_avg_all_topics,r_r2_avg_all_topics,r_rL_avg_all_topics],columns=['Business',\
        'Entertainment','Politics','Sport','Tech'])
    r_score.index = rouge_list
    print(r_score)

    """
    Generating plots for f-score, p-score and r-score with metric Rouge-1, Rouge-2 and Rouge-L for all of the topics.
    """
    score_type=zip([f_score,p_score,r_score],["F","P","R"])
    for metric,metric_str in score_type:
        plt.close()
        fig1,axs=plt.subplots(1)
        axs.plot([0,1,2,3,4],metric.iloc[0,:],'b',label='Rouge-1')
        axs.plot([0,1,2,3,4],metric.iloc[1,:],'r',label='Rouge-2')
        axs.plot([0,1,2,3,4],metric.iloc[2,:],'g',label='Rouge-L')
        axs.legend()
        title=metric_str+"-Score for Rouge-1, Rouge-2 and Rouge-L"
        axs.set_title(title)
        plt.xlabel("Summarized Topics")
        plt.ylabel("Scores")
        axs.set_xticks([0,1,2,3,4])
        axs.set_xticklabels(["Business","Entertainment","Politics","Sports","Tech"])
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        fig1.savefig(os.path.join("Plots/",metric_str,'_score.png'))



def main(ref_summary_path,hyp_summary_path):
    precision,recall,scores=rouge_scores.main(ref_summary_path,hyp_summary_path)
    with open(os.path.join("Data_files/","list_scores.pkl"),'wb') as f: 
        pickle.dump(scores,f)
    #unigram
    precision_df=pd.DataFrame((_ for _ in itertools.zip_longest(*precision)), columns=['Business', 'Entertainment', 'Politics','Sport','Tech'])
    recall_df=pd.DataFrame((_ for _ in itertools.zip_longest(*recall)), columns=['Business', 'Entertainment', 'Politics','Sport','Tech'])
   
    precision_path=os.path.join('Data_files/','precision_nltk.csv')
    recall_path=os.path.join('Data_files/','recall_nltk.csv')
    if not os.path.exists(os.path.join("Data_files/")):
        os.makedirs(os.path.join("Data_files/"))
    
    precision_df.to_csv(precision_path)
    recall_df.to_csv(recall_path)
    
    generate_imgs(precision_path,recall_path)

    calculate_mean_score_plots(scores)

if __name__=='__main__':
    main('bbc_news_corpus/Summaries/','Nltk_summaries/')