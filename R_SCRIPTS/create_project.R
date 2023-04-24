## SCRIPT FOR CREATING A PROJECT AND GETTING THE RIGHT FILES THERE ##

#Loading required packages
library(usethis)
library(rstudioapi)

#Choosing directory to put the project folder in
print("Choose directory to put project folder in")
project_dir <- selectDirectory(caption = "Choose directory to put project folder in", path = getwd())
project_name <- readline("Choose name of project: ")
project_path <- paste0(project_dir, "/", project_name, sep = "")

#Choosing directory to copy the script files from
print("Choose directory to copy script files from")
from_dir <- selectDirectory(caption = "Choose directory to copy script files from", path = getwd())
to_dir <- paste0(project_dir, "/", project_name, sep = "")
list_of_files <- list.files(from_dir)

#Creating a new project
create_project(path = project_path)

#Creating folders in project folder
dir.create(paste0(project_path, "/Scripts/"))
dir.create(paste0(project_path, "/Output/"))
dir.create(paste0(project_path, "/Output/Data/"))
dir.create(paste0(project_path, "/Output/Plots/"))
dir.create(paste0(project_path, "/Raw_data/"))
dir.create(paste0(project_path, "/Raw_data/Unmerged_data/"))
dir.create(paste0(project_path, "/Raw_data/Merged_data/"))

#Copying script files to the new project directory
for (i in 1:length(list_of_files)) {
  file.copy(from = paste0(from_dir, "/", list_of_files[i], sep = ""), to = paste0(to_dir, "/Scripts/"))
}
