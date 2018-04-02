import csv

file1 = "C:/Users/ADMIN/Documents/GWBootcamp_HWassignments/python-challenge/PyBank/budget_data_1.csv"

file2 = "C:/Users/ADMIN/Documents/GWBootcamp_HWassignments/python-challenge/PyBank/budget_data2.csv"

with open(file1) as csvfile1:


#  with open(file2) as csvfile2:
#     for i in csvfile2:
#         print(i)
    total_months = 0
    total_revenue = 0
    total_difference = 0
    greatest_increase = 0
    greatest_decrease = 0
    last_month_rev = 0
    greatest_decrease_month = ""
    greatest_increase_month = ""

    csv_reader = csv.reader(csvfile1, delimiter=",")
    next(csv_reader, None)
    for row in csv_reader:
        current_month_rev = int(row[1])
        #counts the number of months in the data
        total_months = total_months + 1
        #this gets the sum of the revenue column in the data     
        total_revenue = total_revenue + current_month_rev
        #the difference variable holds the last 
        difference = last_month_rev - current_month_rev

        #we get the sum of all the differences between each month 
        total_difference = total_difference + abs(difference)

        #this finds the largest profit between any two months 
        if difference > greatest_increase:
            #this updates the new biggest increase   
            greatest_increase = difference 
            greatest_increase_month = row[0]
        #this finds the largest loss between any two months
        if difference < greatest_decrease:
            #we found a bigger loss so keep track of that variable
            greatest_decrease = difference    
            greatest_decrease_month = row[0]
        #updating last number
        last_number = current_month_rev

    print("Financial Analysis")
    print("---------------------------------------------------------")
    print("Total Months: " + str(total_months)) 
    print("Total Revenue: $" + str(total_revenue)) 
    print("Average Revenue Change: $" + str(total_difference/(total_months - 1))) 
    print("Greatest Increase in Revenue: " + greatest_increase_month + " ($"+str(greatest_increase)+")")
    print("Greatest Decrease in Revenue: " + greatest_decrease_month + " ($"+str(greatest_decrease)+")")
    #print total_revenue