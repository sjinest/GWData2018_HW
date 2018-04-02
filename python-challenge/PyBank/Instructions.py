# Section 1

# Declare a variable that holds some number data
# 1. Total the values in the list_of_numbers and print the sum afterwards. Output should be: 33.
# Hint use a loop.
list_of_numbers = [1, 0, -3, 4, 8, 2, -4, 3, 7, 1, 6, 12, 1, -5]

total = 0 

#for x in list_of_numbers:
    #total = total + x
    #print(total)

# 2. Find and print the average for list_of_numbers. Output should be: 2.
# Hint average is calculated like this: average = sum/(number of items)

#average = total/len(list_of_numbers)
#print(average)


# 3. Count and print the number of times that the number 1 appears in the list_of_numbers. Output should be 3.
# Hint you will need to keep track of the count and an a check to see if the number is a 1.
#count1 = 0
# for x in list_of_numbers:
#     if x == 1:
        #count1 = count1 + 1
        #print(x) 
#print(count1)

# 4. Print the biggest number in list_of_numbers. Output should be: 12.
# Hint you will need to keep track of the biggest number, check to see if the current (in the loop) is bigger and if so update the biggest.
# Hint 2: Initialize your variable to some small number like -100.
# biggest_number = -100
# for x in list_of_numbers:
#     if x > biggest_number:
#         biggest_number = x

# # print(biggest_number) 

# # 5. Print the smallest number in the list_of_number. Output should be: -5
# # Hint see #4 Hint. Initialize your variable to some large number like 100.
# smallest_number = 100
# for x in list_of_numbers:
#     if x < smallest_number:
#         smallest_number = x
#print(smallest_number)
# 6. Print the difference between the biggest and the smallest numbers in the list_of_numbers. Output should be: 17.
# biggest_number = -100
# smallest_number = 100
# for x in list_of_numbers:
#     if x > biggest_number:
#         biggest_number = x
#     if x < smallest_number:
#         smallest_number = x

# difference = (biggest_number - smallest_number)
# print(difference) 
# 7. Print the sum between each number. Ex 1+0=0, 0+(-3)=-3, -3+4=1.. and so forth.
# Hint you will need to store what the last number is. You will also need to update the last number before going into the next iteration in the loop.
# Hint 2: Initialize your variable to None. Check if your variable is not None and if that is the case then compute and print the sum between it and the current number.
# Hint 3: The str function is used to convert a number into a string, Ex: str(134) -> '134'

# sum = 0
# last_number = 0
# for x in list_of_numbers:
#     sum = x + last_number  
#     print (str(last_number) + " + " + str(x) + " = " + str(sum))
#     last_number = x 
#8. Print the largest sum between any two consecutive numbers. (Builds on #7)
# Hint you need to keep track of and update the largest sum. Output should be: 18
# Hint 2: You may want to initialize your variable to None. You can check if a variable is equal to None like this: if var_name is None:
sum = 0
last_number = 0
largest_sum = 0
for x in list_of_numbers:
    sum = x + last_number
    if sum > largest_sum:
        largest_sum = sum  
    print (str(last_number) + " + " + str(x) + " = " + str(sum))
    last_number = x
print(largest_sum)

# Section 2

# Declare a list of lists. Each nested list contains months representing one quarter in a year.
#data = [['JAN', 'FEB', 'MARC'], ['APR', 'MAY', 'JUN'], ['JUL', 'AUG', 'SEP'], ['OCT', 'NOV', 'DEC']]

# 1. Print only the first month of each quarter: Output should be: JAN APR JUL OCT (With each month on a new line)
# Hint 1 use a loop.
# Hint use array syntax to get the first element.
# 2. Print every month in the year using the data. Output should be: JAN FEB .... NOV DEC (With each month on a new line) (Hint you might need more than 1 loop)
# Hint you will need more than one loop.
