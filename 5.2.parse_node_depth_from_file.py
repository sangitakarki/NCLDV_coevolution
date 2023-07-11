import os
import sys

dicts = {}
lista = []
#filename = "/projects/Aylward_Lab/sangita/third_project/Pfam_all_files_2/clade_depth/clade_depth_output/IF4E.txt"
#filename = "/projects/Aylward_Lab/sangita/third_project/Pfam_all_files_2/IF4E_tree_depth.txt"
filename = "/projects/Aylward_Lab/sangita/third_project/Pfam_all_files_2/ercc4.5depth.txt"


for line  in open(filename):
    if line.startswith("Root"):
        pass
    else:
        line = line.strip().split(" ")
        #print(line)
        node = line[1]
        depth = line[2]
        dicts[node] = depth


for line in open("1.list_nodes.txt"):
    line = line.strip()
    lista.append(line)


sys.stdout = open('ercc4_depthfinal.txt','wt')
for k in lista:
    if k in dicts:
        print(k, dicts[k])
    else:
        print(k)
#############################################
