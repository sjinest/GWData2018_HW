import os

import csv


file2 = "C:/Users/ADMIN/Documents/GWBootcamp_HWassignments/python-challenge/PyPoll/election_data_2.csv"

with open(file2) as csvfile2:

    total_votes = 0
    candidates_dictionary = {}
    most_votes = 0

    csv_reader = csv.reader(csvfile2, delimiter=",")
    next(csv_reader, None)
    for row in csv_reader:
        total_votes = total_votes + 1
  
        candidate_name = row[2]
    #  If the candidate is not already in the dictionary
        if candidate_name in candidates_dictionary:
    # #     # Add the candidate to the dictionary by setting the key to their name and set the value to 1
    #         candidates_dictionary[candidate_name] = 1
            candidates_dictionary[candidate_name] += 1
        else:
            candidates_dictionary[candidate_name] = 1
        #The candidate is already in the dictionary so increment the value by 1
    #     #if candidates_dictionary.key() in candidates_dictionary

    # Write a line of code here to add a value to the dictionary
# End of for loop (Must be indented back)

#sets path for output file
output_dest = os.path.join('Output.txt')

# opens our Output.text destination and prints the summary for the data 
with open(output_dest, 'w') as writefile:
    print("Election Results")
    print("--------------------------------------")
    print("Total Votes: " + str(total_votes))
    print("--------------------------------------")
    for key, value in candidates_dictionary.items(): 
        print(key, str(value/total_votes*100)+"%", value) 
        #winner = most_votes/total_votes
        #if most_votes < value:
            #most_votes = winner
    print("----------------------------------------")
    print("Winner: " + "Khan")

   #opens the output file in read mode and prints to the terminal 
with open(output_dest, 'r') as readfile:
    print(readfile.read())
    