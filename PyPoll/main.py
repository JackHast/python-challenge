import os
import csv

# Creating path to election data
election_data = os.path.join("Resources", "election_data.csv")

#Intialising variables used in for loop
Stats = {} # Dictionary of candidates and number of votes received
Total_Votes = 0
Votes = 0
Candidates=[]

# Reading csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    # Looping through rows of csv file
    for row in csvreader:
        Total_Votes+=1
        Next_Candidate=row[2]
        # For first row initialising key in dictionary stats 
        if Total_Votes==1:
            Candidate=row[2]
            Stats[Candidate]=0
            Candidates.append(Candidate)
        # Adding vote to key value each time row[2]==Candidate
        if Next_Candidate==Candidate:  
           Stats[Candidate]+=1
        # Otherwise, if the value for row[2] is in Candidates add vote to key value of Candidate or create key in Stats for Candidate   
        else:
            if Next_Candidate in Candidates:
               Candidate=Next_Candidate
               Stats[Candidate]+=1
            else:
                Candidate=Next_Candidate
                Stats[Candidate]=1
                Candidates.append(Candidate)
    
    # Calculating percentage of votes each candidate got
    Percent_Cand1 = round(100*Stats[Candidates[0]]/Total_Votes,3)
    Percent_Cand2 = round(100*Stats[Candidates[1]]/Total_Votes,3)
    Percent_Cand3 = round(100*Stats[Candidates[2]]/Total_Votes,3)
    Winner = max(Stats, key=Stats.get)

    #Printing results to terminal
    print("")
    print("Election Results")
    print("")
    print("--------------------------------")
    print("")
    print("Total Votes: " + str(Total_Votes))
    print("")
    print("--------------------------------")
    print("")
    print(Candidates[0] + ": " + str(Percent_Cand1) + "%" + " (" + str(Stats[Candidates[0]]) + ")")
    print("")
    print(Candidates[1] + ": " + str(Percent_Cand2) + "%" + " (" + str(Stats[Candidates[1]]) + ")")
    print("")
    print(Candidates[2] + ": " + str(Percent_Cand3) + "%" + " (" + str(Stats[Candidates[2]]) + ")")
    print("")
    print("--------------------------------")
    print("")
    print("Winner: " + Winner)
    print("")
    print("--------------------------------")


#Exporting txt file with results

output = os.path.join("analysis","Analysis.txt")

with open(output, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow("")
    writer.writerow(["Election Results "])
    writer.writerow("")
    writer.writerow(["--------------------------------"])
    writer.writerow("")
    writer.writerow(["Total Votes: " + str(Total_Votes)])
    writer.writerow("")
    writer.writerow(["--------------------------------"])
    writer.writerow("")
    writer.writerow([Candidates[0] + ": " + str(Percent_Cand1) + "%" + " (" + str(Stats[Candidates[0]]) + ")"])
    writer.writerow("")
    writer.writerow([Candidates[1] + ": " + str(Percent_Cand2) + "%" + " (" + str(Stats[Candidates[1]]) + ")"])
    writer.writerow("")
    writer.writerow([Candidates[2] + ": " + str(Percent_Cand3) + "%" + " (" + str(Stats[Candidates[2]]) + ")"])
    writer.writerow("")
    writer.writerow(["--------------------------------"])
    writer.writerow("")
    writer.writerow(["Winner: " + Winner])
    writer.writerow("")
    writer.writerow(["--------------------------------"])