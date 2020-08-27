# Program with functions to load values of a two D array
# main function only

#Check out Week 12 Module 3 for the full explanation of this algorithm

import random

def load()->None:
    '''Receives user input and fills the 2D array'''
    values = []
    ROWS = int(input("Enter the number of rows: "))
    COLS = int(input("Enter the number of collumns: "))
    for x in range(ROWS):
        values.append([])
        for y in range(COLS):
            values[x].append(0)
    print (values)

def main():
    load()

if __name__ == "__main__":
    main()

# my attempt to fill the array with numbers
#
##import random
##
##def load()->None:
##    '''Receives user input and fills the 2D array'''
##    values = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
##    for x in range(3):
##        for y in range(4):
##            values[x][y] = random.randint(1,100)
##    print (values)
##
##def main():
##    load()
##
##if __name__ == "__main__":
##    main()
