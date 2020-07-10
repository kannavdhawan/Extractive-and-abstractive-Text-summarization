import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
precision_df=pd.read_csv("precision_df.csv").iloc[:,1:]
recall_df=pd.read_csv("recall_df.csv").iloc[:,1:]
print("Precision")
print(precision_df.head())
print("Recall")
print(recall_df.head())
