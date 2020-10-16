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