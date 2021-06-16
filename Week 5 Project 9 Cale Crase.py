"""
Program: Project9 Crase
Author: Cale Crase
Random Average Numbers
"""

theSum = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    average = theSum / number
    data = input("Enter a number or just enter to quit: ")
print("The sum is", theSum, "and the average is", average)
        

