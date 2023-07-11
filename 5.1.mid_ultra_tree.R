##clade_Depth##

library(ape)
library(phytools)

files <- list.files(pattern = "\\.nwk$" )
# set the output directory
output_dir <- "/clade_depth"

# loop over the list of file names and read each nwk file
for (file in files) {
  # print the name of the current file
  print(paste("Processing file:", file))
  
  # read the file as a phylogenetic tree object
  tree <- read.tree(file)
  
  #midpoint.roottree
  treee = midpoint.root(tree)
  
  # make the tree ultrametric
  ultrametric_tree <- chronos(treee)
  
  # construct the path to the output file
  output_file <- file.path(output_dir, paste0("ultrametric_", basename(file)))
  # write the ultrametric tree to the output file
  write.tree(ultrametric_tree, file = output_file)
  
 
}

## write the ultrametric tree to a new file
##output_file <- paste0("ummm_", file)
##write.tree(ultrametric_tree, file = output_file)
