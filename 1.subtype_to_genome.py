import numpy as np
import os
from matplotlib import pyplot as plt
import pandas as pd
from tqdm import tqdm
from collections import Counter
from Bio import SeqIO
#import pickle

folder_path = "/groups/Aylward_Lab/sangita/third_project/eukaryotes/reduced_euk_proteins/"
subtype_to_genome = {}

for file in tqdm(os.listdir(folder_path)):
    file_suffix = file.split(".")[0]
    
    for record in tqdm(SeqIO.parse(os.path.join(folder_path, file), "fasta")):
        
        subtype = record.id.split(".")[0]
        subtype_to_genome[subtype] = file_suffix


with open('subtype_to_genome.pickle', 'wb') as f:
    pickle.dump(subtype_to_genome, f, protocol=pickle.HIGHEST_PROTOCOL)