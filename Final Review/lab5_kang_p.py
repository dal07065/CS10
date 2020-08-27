# Lina Kang
# 1072568
# This program exercises the skill of dictionary usage

# ------------------------------- #
# Question 1.                     #
# ------------------------------- #

def givenADictionary():
    ''' Outputs the contents of the 'grade' dictionary'''
    grade = {"A":8, "D":3, "B":15, "F":2, "C":6}

    # All the keys
    print("All the keys: ", end = '')
    for key in grade:
        print(key, end = ' ')
    print()

    # All the values
    print("All the values: ", end = '')
    for key in grade:
        print(grade[key], end = ' ')
    print()

    # All the key and value pairs
    print("All the key and value pairs: ", end = '')
    string = "{"
    for key in grade:
        string = string + "\'" + key + "\'" + ":" + str(grade[key]) + ", "
    index = string.rfind(',')
    string = string[:-2]
    string = string + "}"
    print(string)

    # All the key and value pairs in key order
    print("All the key and value pairs in key order: ", end = '')
    string = "{"
    for key in sorted(grade):
        string = string + "\'" + key + "\'" + ":" + str(grade[key]) + ", "
    index = string.rfind(',')
    string = string[:-2]
    string = string + "}"
    print(string)

    # The average value
    print("The average value: ", end='')
    sum = 0.0
    counter = 0
    for key in grade:
        sum = sum + grade[key]
        counter += 1
    avg = sum / counter
    print(format(avg, ',.2f'))
    
givenADictionary()

##Output with 1 Test Case
##
##All the keys: A D B F C 
##All the values: 8 3 15 2 6 
##All the key and value pairs: {'A':8, 'D':3, 'B':15, 'F':2, 'C':6}
##All the key and value pairs in key order: {'A':8, 'B':15, 'C':6, 'D':3, 'F':2}
##The average value: 6.80

# ------------------------------- #
# Question 2.                     #
# ------------------------------- #

def determineRank(years)->str:
    '''Determines the rank based on a year given, using a dictionary'''
    dict = {"1":"Freshman", "2":"Sophomore", "3":"Junior", "4":"Senior"}
    return dict.get(years, "Invalid input")


def main():
    years = input("Enter the number of current year in school (1-4): ")
    years = years.strip()
    rank = determineRank(years)
    print(years + " = " + rank)


if __name__ == "__main__":
    main()

## Output with 5 test cases
##
## Test Case 1.
##    
##Enter the number of current year in school (1-4): 1
##1 = Freshman
##
## Test Case 2.
##    
##Enter the number of current year in school (1-4): 2
##2 = Sophomore
##
## Test Case 3.
##    
##Enter the number of current year in school (1-4): 3
##3 = Junior
##
## Test Case 4.    
##    
##Enter the number of current year in school (1-4): dfsgfsd
##dfsgfsd = Invalid input
##
## Test Case 5.
##    
##Enter the number of current year in school (1-4): 0
##0 = Invalid input

