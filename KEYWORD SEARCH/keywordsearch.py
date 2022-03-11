import pandas as pd
import glob
import os

os.chdir("/Users/emmakeil-vine/Documents/UBC/ECON594/TWINT_ALL/AllTweetsDownloaded/Do_Over/processed/")

k_en = pd.read_csv('fire_en.csv')
k_en_com = k_en.stack().tolist()
k_en_unique = list(dict.fromkeys(k_en_com))
print(k_en_unique)
#df_unique.to_csv("cyclone_ne.csv")

def key_checker_en(tweet):
    if any(word in k_en_com for word in tweet.lower().split()):
        return '1'
    else:
        return '0'

df_en = pd.read_csv('test_keycheck.csv', lineterminator='\n')
df_en['key_en'] = df_en['tweet'].astype(str).apply(key_checker_en)

print(df_en)
