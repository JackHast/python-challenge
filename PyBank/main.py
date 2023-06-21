import os
import csv

#Creating path to csv file
budget_data = os.path.join("Resources", "budget_data.csv")

#Intialising variables used in for loop
Total_Months = 0
Total = 0
Changes = 0
Dates = []
last_month = 0
Diff = []

# Reading csv file 
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    # Looping through rows in csv file
    for row in csvreader:
        Total += float(row[1])
        col_2=float(row[1]) #Current months change in profits
        if Total_Months>0:
            Diff.append(col_2-last_month) #Diff stores the differences in profit gain/loss between consecutive months
            Changes+=col_2-last_month
            Dates.append(row[0]) #Stores all dates 
        last_month = col_2 #Holds previous month's change in profits
        Total_Months+=1

    #Determining average change and the greatest increase/decrease in profits along with date
    Average_Change=round(Changes/(Total_Months-1),2)
    Greatest_Inc = int(max(Diff))
    Date_Inc = Dates[Diff.index(Greatest_Inc)]
    Greatest_Dec = int(min(Diff))
    Date_Dec = Dates[Diff.index(Greatest_Dec)]
    
    #printing results to terminal
    print("")
    print("Financial Analysis")
    print("")
    print("--------------------------------")
    print("")
    print("Total Months: " + str(Total_Months))
    print("")
    print("Total: " + "$" + str(int(Total)))
    print("")
    print("Average Change: " + "$" + str(Average_Change))
    print("")
    print("Greatest Increase in Profits: " + Date_Inc + " ($" + str(Greatest_Inc) + ")")
    print("")
    print("Greatest Decrease in Profits: " + Date_Dec + " ($" + str(Greatest_Dec) + ")")
    print("")

#Exporting results as txt file

output = os.path.join("analysis","Analysis.txt")

with open(output, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow("")
    writer.writerow(["Financial Analysis"])
    writer.writerow("")
    writer.writerow(["--------------------------------"])
    writer.writerow("")
    writer.writerow(["Total Months: " + str(Total_Months)])
    writer.writerow("")
    writer.writerow(["Total: " + "$" + str(int(Total))])
    writer.writerow("")
    writer.writerow(["Average Change: " + "$" + str(Average_Change)])
    writer.writerow("")
    writer.writerow(["Greatest Increase in Profits: " + Date_Inc + " ($" + str(Greatest_Inc) + ")"])
    writer.writerow("")
    writer.writerow(["Greatest Decrease in Profits: " + Date_Dec + " ($" + str(Greatest_Dec) + ")"])

