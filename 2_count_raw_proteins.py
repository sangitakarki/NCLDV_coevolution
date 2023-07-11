import numpy as np
import pandas as pd
from tqdm.notebook import tqdm
import pickle

f = open("parsed_protein_from_first_code.txt", "r")

head = True
data = []
count = 0

for line in tqdm(f):

    if head == True:
        header = line.strip().split("\t")
        # print (header)
        head = False
        continue
    line_list = line.strip().split("\t")
    protein = line_list[0]
    # print (protein)
    hits = line_list[1]
    hit_list = hits.split(";")
    # print (hit_list)
    for i in range(len(hit_list)):
        data.append([protein, hit_list[i]])
# print(data)
df = pd.DataFrame(data, columns=["proteins", "hits"])
df.head()
hits = df["hits"].to_list()
sf = pd.Series(hits).value_counts()

df = pd.DataFrame({'Protein':sf.index, 'count':sf.values}) #changing series to df. as we cannot output series on its own

#df.to_csv("/groups/Aylward_Lab/sangita/third_project/Pfam_all_files/pfamdomain_proteins_count/asgardonlypfamdom_protein_count_updated.txt", sep=' ', index=False, header=False)
