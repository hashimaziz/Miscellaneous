from random import randint
import os 

done = False
phone = 763821
generations = 0

def passcode(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

while not done:
    code = (passcode(6))
    print(code)
    generations += 1
    if code == phone:
        print("That took",generations,"generations!")
        done = True
    
