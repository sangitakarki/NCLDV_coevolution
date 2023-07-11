import os
from Bio import SeqIO
from collections import defaultdict
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import AlignIO
from Bio import Phylo

list1 = []
tree_file = "protein_umtree.nwk"
for tree in Phylo.parse(tree_file, "newick"):
    #tree = tree.root_at_midpoint()
    tree_depth = tree.depths(unit_branch_lengths =False)

for k, v in tree_depth.items():
    print(k,v)
