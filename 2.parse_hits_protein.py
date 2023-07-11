import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from tqdm.notebook import tqdm
from collections import Counter
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


####1. Working with all_euk_pfamout.txt file, splitting by ; and putting in different lines

#df_domain = pd.read_csv("final_reduced_euk_proteins.parsed", header=None) ##pfamout.txt file
#df_domain = pd.read_csv("all_complete_NCLDV_proteins.parsed", header=None)
#df_domain = pd.read_csv("merged_bac_familyreps.parsed", header=None)
df_domain = pd.read_csv("all_asgard_proteins_updated.parsed", header=None)
#df_domain = pd.read_csv("cured_merged_arconly_familyreps.parsed", header=None)
#df_domain = pd.read_csv("all_complete_Mirus_proteins.parsed", header=None)



df_domain = pd.DataFrame(df_domain[0].str.split('\t').tolist(),
                      columns=['id', 'values', 'scores'])
##df_euk.head()

idxs = []
values = []
scores = []

for row in df_domain.iterrows():
    idx = row[1].values[0]
    value = row[1].values[1]
    score = row[1].values[2]

    for item, value in zip(value.split(";"), score.split(";")):
        idxs.append(idx)
        values.append(item)
        scores.append(value)

df_domain_new = pd.DataFrame({"id": idxs, "values": values, "scores": scores})
#print (df_domain_new)

###2. Working with euk_sign_protein files that are only shared (asgard, GV and euk)
### not interested in ESPs present only in euk

###IMP#### df_esp = pd.read_csv("ESPs_example.txt", sep = "\t")
df_esp = pd.read_csv("ESPs.tsv", sep = "\t")
#df_esp.head()
values_cols_df_esp = list(df_esp["Proteins"].values)

new_df = df_domain_new[df_domain_new["values"].isin(values_cols_df_esp)]

hit_protein_dict = new_df.groupby("values")["id"].apply(list).to_dict()
########
dict_id_seq = {}

for record in SeqIO.parse("all_asgard_proteins_updated.faa", "fasta"):
#for record in SeqIO.parse("all_complete_reduced70_asg.faa", "fasta"):
#for record in SeqIO.parse("merged_bac_familyreps.faa", "fasta"):
#for record in SeqIO.parse("class_rep_261_all_complete.faa", "fasta"):
#for record in SeqIO.parse("bac_phylum_121_all_complete.faa", "fasta"):
#for record in SeqIO.parse("all_complete_NCLDV_proteins.faa", "fasta"):
#for record in SeqIO.parse("all_reduced343_ncldv.faa", "fasta"):
#for record in SeqIO.parse("cured_merged_arc_familyreps.faa", "fasta"):
#for record in SeqIO.parse("all_complete_reduced_euk.faa", "fasta"):
#for record in SeqIO.parse("all_55_reduced_euk.faa", "fasta"):
#for record in SeqIO.parse("all_87_reduced_euk.faa", "fasta"):
#for record in SeqIO.parse("all_complete_Mirus_proteins.faa", "fasta"):

  dict_id_seq[record.id] = record.seq
#dict_id_seq

complete_protein_seq = {}

for key, value in  hit_protein_dict.items():
  complete_protein_seq[key] = []
  for protein in value:
    try:
        complete_protein_seq[key].append(f'>{protein} \n{dict_id_seq[protein]}')
    except:
        continue


for key, value in complete_protein_seq.items():
  f= open(f"{key}_asg_hits_pfam.txt","w+")
  for seq in value:
    f.write(seq + "\n")
  f.close()
