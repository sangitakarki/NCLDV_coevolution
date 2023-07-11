import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from tqdm.notebook import tqdm
from collections import Counter
df_euk = pd.read_csv("all_euk_pfamout.txt", header=None)
df_euk = pd.DataFrame(df_euk[0].str.split('\t').tolist(),
                                 columns = ['id','values','scores'])
##df_euk.head()

df_bac = pd.read_csv("all_bact_arch.pfamannot.txt", header=None)
df_bac = pd.DataFrame(df_bac[0].str.split('\t').tolist(),
                                 columns = ['id','values','scores'])
##df_bac.head()

idxs = []
values = []
scores = []

for row in df_euk.iterrows():
    idx = row[1].values[0]
    value = row[1].values[1]
    score = row[1].values[2]
    
    for item, value in zip(value.split(";"), score.split(";")):
        idxs.append(idx)
        values.append(item)
        scores.append(value)
               
df_euk_new = pd.DataFrame({"id": idxs, "values": values, "scores": scores})        
##df_euk_new.head()
##len(df_bac)
idxs = []
values = []
scores = []

for index, row in tqdm(df_bac.iterrows()):
    temp_values = row['values'].split(';')
    temp_scores = row['scores'].split(';')
    values += temp_values
    scores += temp_scores
    idxs += [row['id']]*len(temp_values)
    
    
df_bac_new = pd.DataFrame({"id": idxs1, "values": values1, "scores": scores1})
#euk_values_counter = Counter(df_euk_new["values"].values)
#euk_values_counter

genomes = [item.split(".")[0] for item in df_euk_new["id"].values]
df_euk_new["genomes"] = genomes
#df_euk_new.head()
#len(df_euk_new)
#len(set(df_euk_new["values"].values))
N_unique_genomes = len(set(df_euk_new["genomes"].values))
#print(N_unique_genomes)
unique_values = list(set(df_euk_new["values"].values))
frequency_dict_euk = {}
for value in tqdm(unique_values):
    temp_df = df_euk_new[df_euk_new["values"] == value]
    n_unique_genomes = len(set(temp_df["genomes"].values))
    frequency_dict_euk[value] = n_unique_genomes/N_unique_genomes*100

print(frequency_dict_euk)
#
genomes_bac = ["_".join(item.split("_")[:-1]) for item in df_bac_new["id"].values]
df_bac_new["genomes"] = genomes_bac
N_unique_genomes_bac = len(set(df_bac_new["genomes"].values))
unique_values_bac = list(set(df_bac_new["values"].values))
#
frequency_dict_bac = {}
for value in tqdm(unique_values_bac):
    temp_df = df_bac_new[df_bac_new["values"] == value]
    n_unique_genomes_bac = len(set(temp_df["genomes"].values))
    frequency_dict_bac[value] = n_unique_genomes_bac/N_unique_genomes_bac*100

print(frequency_dict_bac)
#
list_euk = []
for key, value in frequency_dict_euk.items():
    if value > 90:
        list_euk.append(key)
#
list_bac = []
for key, value in frequency_dict_bac.items():
    if value < 5:
        list_bac.append(key)
        
list_common = list(set(list_euk) & set(list_bac))
print(list_common)

resulting_list = list(list_common)
resulting_list.extend(x for x in list_euk if x not in resulting_list)
print(resulting_list)
