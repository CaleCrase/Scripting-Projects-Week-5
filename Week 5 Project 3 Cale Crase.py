"""
Program: Project3 Crase
Author: Cale Crase
Computer Guessing Game
"""

import random
import math
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint (smaller, larger)
count = 0
while True:
    count += 1
    print('%d %d' % (smaller, larger))
    print('The number I choose is:', myNumber)
    choice = input("Is this your number: ")
    if choice == 'yes':
        print("Nice! I got it in", count, "tries!")
        break
    else:
        myNumber = random.randint (smaller, larger)
    if count == 5:
        print("Welp, I lost...")
        break
        

