# Author: CMOB 12/2/2021

def sum_to(n):
    total = 0
    for x in range(n+1):
        total += x
    return total


num = input("Please input an integer: ")

result = sum_to(int(num))
print(result)
