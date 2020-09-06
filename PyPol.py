import csv
import os
# Assign a variable for the file to load and the path.
# Open the data file.
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
    # Write down the names of all the candidates.
    print(election_data)
file_to_save = os.path.join("Analysis", "election_analysis.txt")
with open(file_to_save,'w') as txt_file:
    # Write down the names of all the candidates.
    # Write some data to the file.
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Denver\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Jefferson\n")
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.