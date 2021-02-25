import os
import pandas as pd
data_path = pd.read_csv("demographics_DARPA_TIMIT.csv")
df1 = data_path[['Unnamed: 0']]
demographic_list = df1['Unnamed: 0'] 

wht_count = 0
blk_count = 0
other_count = 0

for subject in demographic_list:
    if (subject.strip() == "WHT"):
        wht_count = wht_count + 1
    elif(subject.strip() == "BLK"):
        blk_count = blk_count + 1
    else:
        other_count = other_count + 1
        
print(wht_count, blk_count, other_count)
