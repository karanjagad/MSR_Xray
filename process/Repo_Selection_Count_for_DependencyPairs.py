# -*- coding: utf-8 -*-


import pandas as pd
import os

dependency_pairs={}
directory = ("./") #Swtict to directory /output/repositories_selected/
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
           f=open(file, 'r')
           #  perform calculation
           df=pd.read_csv(file)
           pair=file.split('.csv')[0]
           sel_repo=df[df.columns[0]].count()
           dependency_pairs[pair]=sel_repo
           f.close()
          
output_df=pd.DataFrame.from_dict(dependency_pairs,orient='index',columns=['Sel.'])
