import rouge_scores
import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 

def generate_imgs(precision_path,recall_path):

    precision_df=pd.read_csv(precision_path).iloc[:,1:]
    recall_df=pd.read_csv(recall_path).iloc[:,1:]
    print("Precision")
    print(precision_df.head())
    print("Recall")
    print(recall_df.head())
    y=pd.DataFrame(np.arange(precision_df.shape[0]))
    # precisions~
    for i in 
    plt.plot(precision_df)
    
    plt.savefig("business_precision.png")


def main(ref_summary_path,hyp_summary_path):
    precision,recall,scores=rouge_scores.main(ref_summary_path,hyp_summary_path)
    
    #unigram
    precision_df=pd.DataFrame((_ for _ in itertools.zip_longest(*precision)), columns=['Business', 'Entertainment', 'Politics','Sport','Tech'])
    recall_df=pd.DataFrame((_ for _ in itertools.zip_longest(*recall)), columns=['Business', 'Entertainment', 'Politics','Sport','Tech'])
    precision_path=os.path.join('Data_files/','precision_df.csv')
    recall_path=os.path.join('Data_files/','recall_df.csv')
    if not os.path.exists(os.path.join("Data_files/")):
        os.makedirs(os.path.join("Data_files/"))
    
    precision_df.to_csv(precision_path)
    recall_df.to_csv(recall_path)
    
    generate_imgs(precision_path,recall_path)

if __name__=='__main__':
    main('bbc_news_corpus/Summaries/','Nltk_summaries/')
