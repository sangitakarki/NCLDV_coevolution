import os
import sys

dicts = {}
lista = []

filename = "protein_depth.txt"

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
