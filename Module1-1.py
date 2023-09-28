# --- Import Pandas ---
import pandas as pd
#--- Read in dataset ----
df = pd.read_csv('transaction_dataset.csv')
# ---WRITE YOUR CODE FOR TASK 1 ---
df.drop(['product_class','product_size'],axis=1,inplace=True)
df.rename(columns={"tr_id":"transaction_id","p_id":"product_id","c_id":"customer_id", 
                   "tr_date":"transaction_date"},inplace=True)
# --- df.to_csv("cleaned_dataset.csv", index=False)----
df
#--- Inspect data ---
