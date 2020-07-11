import os
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import seaborn as sns 

# Genrating graphs
precision_path="precision_df.csv"
recall_path="recall_df.csv"
precision_df=pd.read_csv(precision_path).iloc[:,1:]
recall_df=pd.read_csv(recall_path).iloc[:,1:]
# print("Precision")
# print(precision_df.head())
# print("Recall")
# print(recall_df.head())
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


    if metric_str=="Precision":
        fig.savefig(os.path.join("Precision_nltk.png"))            
    else:
        fig.savefig(os.path.join("Recall_nltk.png"))



    
# Loading scores and calculating mean precision and recall 
import pickle 
with open('list_scores.pkl','rb') as f:
    scores=pickle.load(f)

# print(scores[0][0])
def scores_calc(rouge,metric):
    outer_list=[]
    for topic in scores:
        inner_list=[]
        for article in topic:
            f1_tmp=article[rouge][metric]
            inner_list.append(f1_tmp)   
        outer_list.append(inner_list)
    return outer_list

#Rouge-1
f1_r1=scores_calc('rouge-1','f')
p_r1=scores_calc('rouge-1','p')
r_r1=scores_calc('rouge-1','r')
#Rouge-2
f1_r2=scores_calc('rouge-2','f')
p_r2=scores_calc('rouge-2','p')
r_r2=scores_calc('rouge-2','r')
#Rouge-L
f1_rL=scores_calc('rouge-l','f')
p_rL=scores_calc('rouge-l','p')
r_rL=scores_calc('rouge-l','r')

def average_rouge(itr):
    metric_common=[]
    for i in range(5):
        temp=sum(itr[i])/len(itr[i])
        metric_common.append(temp)
    return metric_common

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

plt.close()
fig1,axs=plt.subplots(1)
axs.plot([0,1,2,3,4],f_score.iloc[0,:],'b',label='Rouge-1')
axs.plot([0,1,2,3,4],f_score.iloc[1,:],'r',label='Rouge-2')
axs.plot([0,1,2,3,4],f_score.iloc[2,:],'g',label='Rouge-L')
axs.legend()
axs.set_title("F-Score for Rouge-1, Rouge-2 and Rouge-L")


plt.tight_layout(rect=[0, 0, 1, 0.95])

# sns.lineplot([0,1,2,3,4],f_score.iloc[0,:])
fig1.savefig('f_score.png')



plt.close()
fig2,axs=plt.subplots(1)
axs.plot([0,1,2,3,4],p_score.iloc[0,:],'b',label='Rouge-1')
axs.plot([0,1,2,3,4],p_score.iloc[1,:],'r',label='Rouge-2')
axs.plot([0,1,2,3,4],p_score.iloc[2,:],'g',label='Rouge-L')
axs.legend()
axs.set_title("P-Score for Rouge-1, Rouge-2 and Rouge-L")


plt.tight_layout(rect=[0, 0, 1, 0.95])

# sns.lineplot([0,1,2,3,4],f_score.iloc[0,:])
fig2.savefig('p_score.png')




plt.close()
fig3,axs=plt.subplots(1)
axs.plot([0,1,2,3,4],r_score.iloc[0,:],'b',label='Rouge-1')
axs.plot([0,1,2,3,4],r_score.iloc[1,:],'r',label='Rouge-2')
axs.plot([0,1,2,3,4],r_score.iloc[2,:],'g',label='Rouge-L')
axs.legend()
axs.set_title("R-Score for Rouge-1, Rouge-2 and Rouge-L")


plt.tight_layout(rect=[0, 0, 1, 0.95])

# sns.lineplot([0,1,2,3,4],f_score.iloc[0,:])
fig3.savefig('r_score.png')

