import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 
import os 
precision_df=pd.read_csv("precision_df.csv").iloc[:,1:]
recall_df=pd.read_csv("recall_df.csv").iloc[:,1:]
print("Precision")
print(precision_df.head())
print("Recall")
print(recall_df.head())
y=pd.DataFrame(np.arange(precision_df.shape[0]))
print(y)
# plt.plot(precision_df)
# sns.lineplot(precision_df.Business,y)
# plt.show()
# plt.savefig("business_precision.png")


fig, axs = plt.subplots(3,2)
    
for i in ['Business', 'Entertainment', 'Politics','Sport','Tech']:

    if i=='Business':
        axs[0,0].plot(precision_df[[i]])
        axs[0,0].grid()
        axs[0,0].set_title('Business Summaries')

    if i=='Entertainment':
        axs[0,1].plot(precision_df[[i]])
        axs[0,1].grid()
        axs[0,1].set_title('Enetertainment Summaries')

    if i=='Politics':
        axs[1,0].plot(precision_df[[i]])
        axs[1,0].grid()
        axs[1,0].set_title('Politics Summaries')

    if i=='Sport':
        axs[1,1].plot(precision_df[[i]])
        axs[1,1].grid()
        axs[1,1].set_title('Sport Summaries')

    if i=='Tech':
        axs[2,0].plot(precision_df[[i]])
        axs[2,0].grid()
        axs[2,0].set_title('Tech Summaries')
        
plt.suptitle('Nltk Precision')
plt.tight_layout(rect=[0, 0, 1, 0.95])

# plot_path=os.path.join("Plots/")
# if not os.path.exists(plot_path):
    # os.makedirs(plot_path)

fig.savefig(os.path.join("Precision_nltk.png"))            

