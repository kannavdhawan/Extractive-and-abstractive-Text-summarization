import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 
precision_df=pd.read_csv("precision_df.csv").iloc[:,1:]
recall_df=pd.read_csv("recall_df.csv").iloc[:,1:]
print("Precision")
print(precision_df.head())
print("Recall")
print(recall_df.head())
y=pd.DataFrame(np.arange(precision_df.shape[0]))
print(y)
plt.plot(precision_df)
# sns.lineplot(precision_df.Business,y)
# plt.show()
plt.savefig("business_precision.png")