from random import randint

done = False
phone = 763821
generations = 0

def passcode(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

while not done:
    code = (passcode(6))
    generations += 1
    print(code)
    if code == phone:
        print(code)
        print("That took",generations,"generations!")
        done = True
    
