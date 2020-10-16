  #Sign your name:________________

'''
 1. Make the following program work.
   '''
'''
     print("This program takes three numbers and returns the sum.")
     total = 0

     for i in range(3):
         x = input("Enter a number: ")
         total = total + x
     print("The total is:", x)
 '''

print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = int(input("Enter a number: "))
    total = total + x
print("The total is:", total)

'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
'''
num = 0
while num <= 100:
    print(num)
'''

for i in range(0, 101, 2):
    print(i)

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''

num = 10
while num >=0:
    print(num)
    num -= 1
print("Blast off!")

'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''

import random
num = random.randint(1, 10)
print(num)

'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''

ttl = 0
pstv = 0
eqlz = 0
ngtv = 0

for i in range(7):
    qstn = int(input("input a number:"))
    ttl += qstn
    if qstn > 0:
        pstv += 1
    elif qstn < 0:
        ngtv += 1
    else:
        eqlz += 1
print("The final count is", ttl)
print("You put", pstv, "positive numbers")
print("You put", ngtv, "negative numbers")
print("You put", eqlz, "numbers equal to zero")