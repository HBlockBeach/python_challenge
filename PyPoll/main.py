import os
import csv


csvpath = os.path.join('..','..','CWR-CLE-DATA-PT-01-2020-U-C', '03-Python','Homework03','Instructions', 'PyPoll/Resources','election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    voterid = []
    county = []
    candidate = []

    for row in csvreader:
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    total_votes = len(voterid)

    candidates = []

    for row in candidate: 
        if row not in candidates:
            candidates.append(row)

    khanc = 0
    correyc=0
    lic=0
    otoolc=0

    counts=[]

    for row in candidate:
        if row == "Khan":
            khanc=khanc+1
        elif row == "Correy":
            correyc=correyc+1
        elif row =="Li":
            lic=lic+1
        else: 
            otoolc= otoolc+1
    counts.append(khanc)
    counts.append(correyc)
    counts.append(lic)
    counts.append(otoolc)


    candidate_percentage = [format(khanc/total_votes,".2%"),format(correyc/total_votes,".2%"),format(lic/total_votes,".2%"),format(otoolc/total_votes,".2%")]


    

    print("Election Results/n")
    print("---------------------")
    print("Total Votes: ", total_votes)
    print("---------------------")
    print(candidates[0]+":",candidate_percentage[0], "(" + str(counts[0]) + ")")
    print(candidates[1]+":",candidate_percentage[1],  "(" + str(counts[1]) + ")")
    print(candidates[2]+":",candidate_percentage[2],  "(" + str(counts[2]) + ")")
    print(candidates[3]+":",candidate_percentage[3],  "(" + str(counts[3]) + ")")
    print("---------------------")
    print("The Winner is: Khan")
    print("---------------------")




 
