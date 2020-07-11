import rouge_scores
import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 
import itertools
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
def calculate_mean_score(score):
    """
    Input scores from Rouge 
    Returns:
            Mean of Precision and for Rouge-1, Rouge-2 and Rouge-L 
            Mean of Recall for Rouge-1, Rouge-2 and Rouge-L
            Mean of F-1 Score for Rouge-1, Rouge-2 and Rouge-L

    """


def main(ref_summary_path,hyp_summary_path):
    precision,recall,scores=rouge_scores.main(ref_summary_path,hyp_summary_path)
    
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
    calculate_mean_score(scores)

if __name__=='__main__':
    main('bbc_news_corpus/Summaries/','Nltk_summaries/')
