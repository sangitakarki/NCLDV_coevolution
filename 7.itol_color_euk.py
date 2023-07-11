from Bio import SeqIO
from tqdm.notebook import tqdm
import os

####conda activate Py37 ######
#euk_taxa = "/groups/Aylward_Lab/sangita/third_project/Pfam_all_files/pfam_domain_trees/itol_color_script_files/euk_taxa.txt"
folder_allcomplete = "/projects/Aylward_Lab/sangita/third_project/Pfam_all_files/pfam_domain_trees/itol_color_script_files/all_complete_faa"
folder_protein = "/projects/Aylward_Lab/sangita/third_project/Pfam_all_files/pfam_domain_trees/itol_color_script_files/gene_tree_review"
#itol_colorstrip_header = "/groups/Aylward_Lab/sangita/third_project/Pfam_all_files/pfam_domain_trees/itol_color_script_files/topoiso5_colorstrip.txt"

file_paths = []
for file_name in os.listdir(folder_allcomplete):
    file_paths.append(os.path.join(folder_allcomplete, file_name))
#print(file_paths)

file_to_group = {
    '/projects/Aylward_Lab/sangita/third_project/Pfam_all_files/pfam_domain_trees/itol_color_script_files/all_complete_faa/all_asgard_proteins_updated.faa': "Asgard archaea",
    "/projects/Aylward_Lab/sangita/third_project/Pfam_all_files/pfam_domain_trees/itol_color_script_files/all_complete_faa/all_complete_NCLDV_proteins.faa" :"Giant Virus",
    '/projects/Aylward_Lab/sangita/third_project/Pfam_all_files/pfam_domain_trees/itol_color_script_files/all_complete_faa/all_complete_reduced_euk.faa' : "Eukaryote",
    '/projects/Aylward_Lab/sangita/third_project/Pfam_all_files/pfam_domain_trees/itol_color_script_files/all_complete_faa/cured_merged_arc_familyreps.faa': "Archaea",
    '/projects/Aylward_Lab/sangita/third_project/Pfam_all_files/pfam_domain_trees/itol_color_script_files/all_complete_faa/merged_bac_familyreps.faa' : "Bacteria"
}
#
#
def protein_to_file_name(file_paths, file_to_group):
    proteintogroup_dict = {}
    for file_name in tqdm(file_paths):
        for record in tqdm(SeqIO.parse(file_name, "fasta")):
            proteintogroup_dict[record.id] = file_to_group[file_name]

    return proteintogroup_dict

protein_to_group_dict = protein_to_file_name(file_paths, file_to_group)


protein_paths = []
for protein_name in os.listdir(folder_protein):
    protein_paths.append(os.path.join(folder_protein, protein_name))
#print(protein_paths)
#
# euktaxadict = {}
# for line in open(euk_taxa):
#         line = line.strip().split("\t")
#         #print(line)
#         genomeid = line[0]
#         taxa = line[1]
#         euktaxadict[genomeid] = taxa
# #print(euktaxadict)
#
#
for merged_file in protein_paths:
    allfile_dict = {}
    eukonlydict = {}
    euklist = []
    for record in tqdm(SeqIO.parse(merged_file, "fasta")):
        if record.id in protein_to_group_dict:
            allfile_dict[record.id] = protein_to_group_dict[record.id]
    # print(allfile_dict)
#
#     for key, value in allfile_dict.items():
#         if value == "Eukaryotes":
#             euklist.append(key)
#     # print(euklist)
#
#     for protein in euklist:
#         genome = protein.strip().split(".")[0]
#         # print(genome)
#         if genome in euktaxadict.keys():
#             eukonlydict[protein] = euktaxadict[genome]
#         else:
#             eukonlydict[protein] = "Protists"
#
#     # print(eukonlydict)
#     allfile_dict.update(eukonlydict)

    for key, value in allfile_dict.items():
        f = open(f"{merged_file}_color_notdividingeuk.txt", "a")
        if value == 'Archaea':
            f.write(key + "\t" + "#a6cee3" + "\t" + value + "\n")
        elif value == 'Asgard archaea':
            f.write(key + "\t" + "#1f78b4" + "\t" + value + "\n")
        elif value == 'Bacteria':
            f.write(key + "\t" + "#6a3d9a" + "\t" + value + "\n")
        elif value == 'Eukaryote':
            f.write(key + "\t" + "#33a02c" + "\t" + value + "\n")
        elif value == 'Giant Virus':
            f.write(key + "\t" + "#e31a1c" + "\t" + value + "\n")
        else:
            f.write( "error while parsing" + "\n")
        f.close()

