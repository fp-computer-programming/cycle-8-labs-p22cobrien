# Author: CMOB 12/3/2021

def sum():
    total = 0
    while True:
        number = input("Please enter a number: ")
        if number == "-1":
            break
        else:
            total += int(number)
            print("The sum of all the numbers is {0}".format(total))


sum()
