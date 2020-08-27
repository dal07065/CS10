# Lina Kang
# 1072568
# Lab 4 - This contains several different programs with different functions

# Question 1

def isBRICS()->None:
    '''Determines if the user input belongs in BRICS'''
    try:
        BRICS = ("Brazil", "Russia", "India", "China", "Sri Lanka")
        country = input("Enter the name of country: ")
        num = BRICS.index(country)
        print(country + " is a member of BRICS")
    except ValueError:
        print(country + " is not a member of BRICS")


def main():
    
    isBRICS()


if __name__ == "__main__":
    main()

##Output with 5 test cases
##
##Test Case 1.
##
##Enter the name of country: Pakistan
##Pakistan is not a member of BRICS

##Test Case 2.
##
##Enter the name of country: India
##India is a member of BRICS

##Test Case 3.
##
##Enter the name of country: Brazil
##Brazilis a member of BRICS

##Test Case 4.
##
##Enter the name of country: BrazilRussia
##BrazilRussia is not a member of BRICS

##Test Case 5.
##Enter the name of country: 2304
##2304 is not a member of BRICS

# Question 2

def makeList()->(list):
    '''Creates a list of numbers from 1 to 10'''
    numbers = []
    for x in range(10):
        numbers.append(x+1)

    return numbers

def delEven(numbers:list)->(list):
    '''Deletes even numbers from the list'''
    for e in range(2, 10, 2):
        numbers.remove(e)

    return numbers


def main():

    originalList = makeList()
    print("Original List -", originalList)
    newList      = delEven(originalList)
    print("List after deleting even numbers:", newList)


if __name__ == "__main__":
    main()

##Output with only 1 test case
##
## Test Case 1.
##    
##Original List - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##List after deleting even numbers: [1, 3, 5, 7, 9, 10]

# Question 3

def createList(numbers:list)->None:
    '''Creates a list of numbers'''
    temp = int(input("Input data (-1 to Quit): "))
    while temp != -1:
        numbers.append(temp)
        temp = int(input("Input data (-1 to Quit): "))
    print()
    

def removeDuplicates(numbers:list)->None:
    '''Deletes even numbers from the list'''
    # counters for while loops (for loops don't seem to change its boundaries even if the variable changes)
    x = 0
    y = 1
    
    # iterates through the list (as it keeps changing)
    while x < len(numbers):
        duplicate = numbers[x]
        
        # with the numbers[x], find its duplicates and delete them
        while y < len(numbers):
            if duplicate == numbers[y]:
                del numbers[y]
            else:
                # you don't need to increment y if an element is deleted - hence the "else"
                y+=1
        x+=1
        y=x+1


def main():

    originalList = []
    createList(originalList)
    print("Original List -", originalList)
    removeDuplicates(originalList)
    print("List after removing duplicates:", originalList)


if __name__ == "__main__":
    main()


##Output with 5 test cases
##
##Test Case 1.
##    
##Input data (-1 to Quit): 1
##Input data (-1 to Quit): 2
##Input data (-1 to Quit): 6
##Input data (-1 to Quit): 2
##Input data (-1 to Quit): 6
##Input data (-1 to Quit): 1
##Input data (-1 to Quit): -1
##
##Original List - [1, 2, 6, 2, 6, 1]
##List after removing duplicates: [1, 2, 6]
##
##Test Case 2.
##
##Input data (-1 to Quit): 1
##Input data (-1 to Quit): 2
##Input data (-1 to Quit): 3
##Input data (-1 to Quit): 4
##Input data (-1 to Quit): 1
##Input data (-1 to Quit): 2
##Input data (-1 to Quit): 3
##Input data (-1 to Quit): 4
##Input data (-1 to Quit): -1
##
##Original List - [1, 2, 3, 4, 1, 2, 3, 4]
##List after removing duplicates: [1, 2, 3, 4]
##
##Test Case 3.
##
##Input data (-1 to Quit): 0
##Input data (-1 to Quit): 0
##Input data (-1 to Quit): 0
##Input data (-1 to Quit): 0
##Input data (-1 to Quit): -1
##
##Original List - [0, 0, 0, 0]
##List after removing duplicates: [0]
##
##Test Case 4.
##
##Input data (-1 to Quit): 1
##Input data (-1 to Quit): 2
##Input data (-1 to Quit): 3
##Input data (-1 to Quit): 1
##Input data (-1 to Quit): 2
##Input data (-1 to Quit): 3
##Input data (-1 to Quit): 2
##Input data (-1 to Quit): 3
##Input data (-1 to Quit): 1
##Input data (-1 to Quit): -1
##
##Original List - [1, 2, 3, 1, 2, 3, 2, 3, 1]
##List after removing duplicates: [1, 2, 3]
##
##Test Case 5.
##
##Input data (-1 to Quit): 11
##Input data (-1 to Quit): 22
##Input data (-1 to Quit): 33
##Input data (-1 to Quit): 44
##Input data (-1 to Quit): 11
##Input data (-1 to Quit): 22
##Input data (-1 to Quit): 33
##Input data (-1 to Quit): 44
##Input data (-1 to Quit): -1
##
##Original List - [11, 22, 33, 44, 11, 22, 33, 44]
##List after removing duplicates: [11, 22, 33, 44]
##
##Test Case Extra
##
##Input data (-1 to Quit): -1
##
##Original List - []
##List after removing duplicates: []

# Question 4

import random

SIZE = 10

def createTuples(numbers:list)->None:
    '''Creates a tuple of random numbers'''
    for x in range(SIZE):
        temp = random.randint(-SIZE,SIZE)
        numbers.append(temp)
    tupl = tuple(numbers)
    print("Original Tuple -", tupl)


def removeNegatives(numbers:list)->None:
    '''Deletes even numbers from the list'''
    x=0
    # deletes all the negative numbers
    while x < len(numbers):
        if numbers[x] < 0:
            del numbers[x]
        else:
            x+=1


def removeDuplicates(numbers:list)->None:
    '''Deletes even numbers from the list'''
    # counters for while loops (for loops don't seem to change its boundaries even if the variable changes)
    x = 0
    y = 1
    # iterates through the list (as it keeps changing)
    while x < len(numbers):
        duplicate = numbers[x]
        # with the numbers[x], find its duplicates and delete them
        while y < len(numbers):
            if duplicate == numbers[y]:
                del numbers[y]
            else:
                # you don't need to increment y if an element is deleted - hence the "else"
                y+=1
        x+=1
        y=x+1
    return numbers
    

def sortDescending(numbers:list)->None:
    '''Sorts the list in descending order'''
    numbers.sort()
    numbers.reverse()
    tupl = tuple(numbers)
    print("New Tuple with Positive numbers :", tupl)
    

def main():
    '''Calls the above functions and prints'''
    numbers = []
    createTuples(numbers)
    removeNegatives(numbers)
    removeDuplicates(numbers)
    sortDescending(numbers)


if __name__ == "__main__":
    main()

##Output with 5 test cases

##Test Case 1.
##    
##Original Tuple - (2, 2, 7, -9, -9, -2, 5, 6, -1, 9)
##New Tuple with Positive numbers : (9, 7, 6, 5, 2)

##Test Case 2.
##
##Original Tuple - (10, 0, 0, 1, 3, -8, -8, -2, 3, 6)
##New Tuple with Positive numbers : (10, 6, 3, 1, 0)

##Test Case 3.
##
##Original Tuple - (9, 10, -1, -1, 2, -9, -5, -9, 8, 9)
##New Tuple with Positive numbers : (10, 9, 8, 2)

##Test Case 4.
##
##Original Tuple - (-7, -2, -9, 0, -1, 7, -9, 4, 6, -1)
##New Tuple with Positive numbers : (7, 6, 4, 0)

##Test Case 5.
##
##Original Tuple - (6, 4, 8, 2, 9, 9, 6, 2, 0, 5)
##New Tuple with Positive numbers : (9, 8, 6, 5, 4, 2, 0)


# Question 5

import random

SIZE = 10

def readValues(numbers:list)->None:
    '''Reads in a series of floats by the user into a list'''
    try:
        print("Please enter values, Q to quit: ")
        temp = input("")
        while temp != 'Q':
            numbers.append(temp)
            temp = input("")
    except ValueError:
        print("\n")


def findLargest(numbers:list)->(float):
    '''Pass the list into the function and find largest'''
    largest=numbers[0]
    # deletes all the negative numbers
    for x in range(1, len(numbers), 1):
        if float(numbers[x]) > float(largest):
            largest = numbers[x]

    return largest


def display(numbers:list, largest:float)->None:
    '''Display the list and highlight the largest'''

    print("Here are the numbers in the list")

    for x in numbers:
        print(x, end ='')
        if x == largest:
            print(" <== this is the largest number", end='')
        print()
        
    return numbers
    

def main():
    '''Calls the above functions and prints'''
    numbers = []
    readValues(numbers)
    print('\n')
    if len(numbers) != 0:
        largest = findLargest(numbers)
        display(numbers, largest)
    else:
        print("Nothing has been entered.")

if __name__ == "__main__":
    main()

##Output with 5 test cases

##Test Case 1.
##    
##Please enter values, Q to quit: 
##34
##56.7
##4
##9
##76.9
##55.4
##Q
##
##
##Here are the numbers in the list
##34
##56.7
##4
##9
##76.9 <== this is the largest number
##55.4

##Test Case 2.
##
##Please enter values, Q to quit: 
##Q
##
##
##Nothing has been entered.

##Test Case 3.
##
##Please enter values, Q to quit: 
##1.1111111
##1.2
##Q
##
##
##Here are the numbers in the list
##1.1111111
##1.2 <== this is the largest number

##Test Case 4.
##
##Please enter values, Q to quit: 
##1
##2
##3
##0
##Q
##
##
##Here are the numbers in the list
##1
##2
##3 <== this is the largest number
##0

##Test Case 5.
##
##Please enter values, Q to quit: 
##23.999
##23.000
##50
##-10
##Q
##
##
##Here are the numbers in the list
##23.999
##23.000
##50 <== this is the largest number
##-10

# Question 6

def are_anagrams(word1:str, word2:str)->None:
    '''Determines if the two words are anagrams'''
    set1 = set(word1)
    set2 = set(word2)

    if set1 == set2:
        print("The words",word1,"and",word2,"are anagrams.")
    else:
        print("The words",word1,"and",word2,"are NOT anagrams.")
    

def main():
    
    valid_input_bool = False
    while not valid_input_bool:
        try:
            print("Anagram test")
            word = input("Enter two words separated by a space : ")
            word1, word2 = word.split()
            valid_input_bool = True
            are_anagrams(word1, word2)

        except ValueError:
            print("Bad Input")


if __name__ == "__main__":
    main()

##Output with 5 test cases
##
##Test Case 1.
##
##Anagram test
##Enter two words separated by a space : fred
##Bad Input
##Enter two words separated by a space : fred joe mary
##Bad Input
##Enter two words separated by a space : cinema iceman
##The words cinema and iceman are anagrams.

##Test Case 2.
##
##Anagram test
##Enter two words separated by a space : cinema icetruck
##The words cinema and icetruck are NOT anagrams.

##Test Case 3.
##
##Anagram test
##Enter two words separated by a space : cinema
##Bad Input
##Enter two words separated by a space : cinema cinem
##The words cinema and cinem are NOT anagrams.

##Test Case 4.
##
##Anagram test
##Enter two words separated by a space : iceman cinema
##The words iceman and cinema are anagrams.

##Test Case 5.
##
##Anagram test
##Enter two words separated by a space : cinema iceman cinema
##Bad Input
##Enter two words separated by a space : iceman
##Bad Input
##Enter two words separated by a space : ice
##Bad Input
##Enter two words separated by a space : ice ice
##The words ice and ice are anagrams.


# Question 7

# a.
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

setA = set1 ^ set2
print("a.", setA)

# b.
setB1 = set1 - set2 - set3
setB2 = set2 - set1 - set3
setB3 = set3 - set2 - set1

setB = setB1 | setB2 | setB3
print("b.", setB)

# c.
setC = (set1 & set2) | (set1 & set3) | (set2 & set3)
print("c.", setC)

# d.
import random

setListD = []
while len(setListD) <= 20:
    tempD = random.randint(1,25)
    if tempD not in set1:
        setListD.append(tempD)
setD = set(setListD)
print("d.", setD)

# e.
setListE = []
while len(setListE) <= 20:
    tempE = random.randint(1,25)
    if tempE not in set1 and tempE not in set2 and tempE not in set3:
        setListE.append(tempE)
setE = set(setListE)
print("e.", setE)

# f.
setListF = []
while len(setListF) <= 20:
    tempF = random.randint(1,25)
    if not(tempF in set1 and tempF in set2 and tempF in set3):
        setListF.append(tempF)

setF = set(setListF)
print("f.", setF)

##Output with 5 test cases
##
##Test Case 1.
##a. {1, 3, 5, 6, 8}
##b. {17, 3, 6, 8, 9, 13}
##c. {1, 2, 4, 5}
##d. {6, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25}
##e. {7, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25}
##f. {2, 3, 9, 10, 11, 12, 15, 16, 21, 23, 24, 25}

##Test Case 2.
##a. {1, 3, 5, 6, 8}
##b. {17, 3, 6, 8, 9, 13}
##c. {1, 2, 4, 5}
##d. {8, 9, 11, 13, 14, 15, 17, 19, 20, 21, 23, 24, 25}
##e. {10, 11, 12, 14, 15, 16, 20, 23, 24, 25}
##f. {2, 4, 6, 7, 10, 11, 13, 14, 15, 16, 18, 20, 21, 22, 23, 25}

##Test Case 3.
##a. {1, 3, 5, 6, 8}
##b. {17, 3, 6, 8, 9, 13}
##c. {1, 2, 4, 5}
##d. {6, 7, 9, 10, 11, 13, 14, 15, 17, 21, 22, 23, 24}
##e. {7, 10, 14, 15, 16, 18, 20, 21, 22, 23, 24, 25}
##f. {1, 3, 4, 6, 7, 8, 11, 12, 13, 16, 17, 18, 22, 23, 24}

##Test Case 4.
##a. {1, 3, 5, 6, 8}
##b. {17, 3, 6, 8, 9, 13}
##c. {1, 2, 4, 5}
##d. {8, 9, 10, 12, 16, 17, 19, 22, 23, 24, 25}
##e. {10, 11, 12, 14, 16, 19, 20, 21, 22, 23, 24, 25}
##f. {2, 4, 5, 6, 7, 8, 9, 11, 14, 17, 19, 21, 22, 24}

##Test Case 5.
##a. {1, 3, 5, 6, 8}
##b. {17, 3, 6, 8, 9, 13}
##c. {1, 2, 4, 5}
##d. {8, 9, 10, 15, 17, 18, 19, 22, 23, 24, 25}
##e. {7, 10, 11, 12, 15, 16, 18, 19, 20, 21, 22, 24}
##f. {1, 2, 3, 7, 9, 13, 14, 15, 16, 17, 18, 19, 21}

