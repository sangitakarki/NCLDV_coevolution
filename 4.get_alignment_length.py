from Bio import SeqIO
from collections import defaultdict
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
import os

folder_name = "/new_alignmenst"
file_paths = []

for file_name in os.listdir(folder_name):
    file_paths.append(os.path.join(folder_name, file_name))
#print(file_paths)
    for file in file_paths:
        for aln in AlignIO.parse(file, "fasta"):
           aln = aln.get_alignment_length()
    print(file, aln)
