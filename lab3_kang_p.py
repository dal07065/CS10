# Lina Kang
# 1072568
# Lab 3

# Question 1.a.

def texas():
    birds = 5000
    print("Texas has", birds, "birds")

# Question 1.b.

def California():
    birds = 8000
    print("California has", birds, "birds")

# Question 1.c.

def main():
    texas()
    California()

if __name__ == "__main__":
    main()

## Test Case 1.
##
##Texas has 5000 birds
##California has 8000 birds

# Question 2.a.

def show_interest(principal:float, rate:float, periods:int)->None:
    interest = principal * rate * periods
    print("The simple interest will be $", format(interest, ',.2f'), sep='')

# Question 2.b.

def main():
    show_interest(10000.00, 0.01, 10)

if __name__ == "__main__":
    main()

## Test Case 1.
##
##The simple interest will be $1,000.00

# Question 3.a.
# get user input for length and height
def getData()->(float, float):
    length = float(input("Enter the length of the triangle: "))
    height = float(input("Enter the perpendicular height of a triangle: "))
    return length, height

# Question 3.b.
# calculate the triangle area based on received user input
def trigArea(length:float, height:float)->(float):
    area = 0.5 * length * height
    return area

# Question 3.c.
# output the data
def displayData(length:float, height:float, area:float)->None:
    print("The length:", length)
    print("The height:", height)
    print("The calculated area:", area)

# Question 3.d.
def main():
    length, height = getData()
    area = trigArea(length, height)
    displayData(length, height, area)

if __name__ == "__main__":
    main()

## Test Case 1.
##
##Enter the length of the triangle: 5
##Enter the perpendicular height of a triangle: 7
##The length: 5.0
##The height: 7.0
##The calculated area: 17.5
##
## Test Case 2.
##
##Enter the length of the triangle: 3
##Enter the perpendicular height of a triangle: 6
##The length: 3.0
##The height: 6.0
##The calculated area: 9.0
##
## Test Case 3.
##
##Enter the length of the triangle: 14.5
##Enter the perpendicular height of a triangle: 19.2
##The length: 14.5
##The height: 19.2
##The calculated area: 139.2
##
## Test Case 4.
##
##Enter the length of the triangle: 5.67
##Enter the perpendicular height of a triangle: 8.94
##The length: 5.67
##The height: 8.94
##The calculated area: 25.3449
##
## Test Case 5.
##
##Enter the length of the triangle: 2.3
##Enter the perpendicular height of a triangle: 6.7
##The length: 2.3
##The height: 6.7
##The calculated area: 7.704999999999999

# Question 4

# gets the amount monthly sales from user input
def get_sales()->(float):
    sales = float(input("Enter the monthly sales: "))
    return sales

# gets the amount of advanced pay from user input
def get_advancedpay()->(float):
    print("Enter the amount of advanced pay, or")
    print("enter 0 if no advanced pay was given.")
    advpay = float(input("Advanced pay: "))
    return advpay

# calculates the commission rate based on the monthly sales
def determine_comm_rate(sales:float)->(float):
    if sales < 10000.00:
        comm = 0.10
    elif sales < 14999.99:
        comm = 0.12
    elif sales < 17999.99:
        comm = 0.14
    elif sales < 21999.99:
        comm = 0.16
    else:
        comm = 0.18
    return comm

def main():
    sales = get_sales()

    advanced_pay = get_advancedpay()

    comm_rate = determine_comm_rate(sales)

    pay = sales * comm_rate - advanced_pay

    print("the pay is $", format(pay, ',.2f'), sep = '')

    if pay < 0:
        print("The salesperson must reimburse")
        print("The company.")

if __name__ == "__main__":
    main()

## Test Case 1.
##
##Enter the monthly sales: 14550.00
##Enter the amount of advanced pay, or
##enter 0 if no advanced pay was given.
##Advanced pay: 1000.00
##the pay is $746.00
##
## Test Case 2.
##
##Enter the monthly sales: 9500
##Enter the amount of advanced pay, or
##enter 0 if no advanced pay was given.
##Advanced pay: 0
##the pay is $950.00
##
## Test Case 3.
##
##Enter the monthly sales: 12000.00
##Enter the amount of advanced pay, or
##enter 0 if no advanced pay was given.
##Advanced pay: 2000.00
##the pay is $-560.00
##The salesperson must reimburse
##The company.
##
## Test Case 4.
##
##Enter the monthly sales: 12345.00
##Enter the amount of advanced pay, or
##enter 0 if no advanced pay was given.
##Advanced pay: 5000.00
##the pay is $-3,518.60
##The salesperson must reimburse
##The company.
##
## Test Case 5.
##
##Enter the monthly sales: 2400
##Enter the amount of advanced pay, or
##enter 0 if no advanced pay was given.
##Advanced pay: 600
##the pay is $-360.00
##The salesperson must reimburse
##The company.

# Question 5.

def getInitials():
    name = input("Enter your full name: ")
    name_list = name.split()
    initials = ''

    # for every item in the list, extract the first character.
    # Then accumulate all the initial characters into 'initials'
    
    for num in range(len(name_list)):
        temp = name_list[num]
        initials = initials + temp[0] + '.'
        
    print(initials)

def main():
    getInitials()

if __name__ == "__main__":
    main()

##Test Case 1.
##
##Enter your full name: James Tiberias Kirk
##J.T.K.
##
##Test Case 2.
##
##Enter your full name: Lina Kang
##L.K.
##
##Test Case 3.
##
##Enter your full name: Donald Trum[
##D.T.
##
##Test Case 4.
##
##Enter your full name: James
##J.
##
##Test Case 5.
##
##Enter your full name: Super Long Name Right Here
##S.L.N.R.H.

# Question 6.

def string_total(string)->(int):
    sum = 0

    # For each character in the string
    #   - extract one character by one
    #   - cast it to an integer
    #   - add it to the sum
    
    for num in range(len(string)):
        sum = sum + int(string[num])
        
    return sum

def main():
    # Get a string of numbers as input from the user.
    number_string = input('Enter a sequence of digits with nothing separating them: ')

    # Call string_total method, and store the total.
    total = string_total(number_string)

    # Display the total.
    print('The total of the digits in the string you entered is', total)

if __name__ == "__main__":
    main()

##Test Case 1.
##
##Enter a sequence of digits with nothing separating them: 4563
##The total of the digits in the string you entered is 18
##
##Test Case 2.
##
##Enter a sequence of digits with nothing separating them: 1010
##The total of the digits in the string you entered is 2
##
##Test Case 3.
##
##Enter a sequence of digits with nothing separating them: 2
##The total of the digits in the string you entered is 2
##
##Test Case 4.
##
##Enter a sequence of digits with nothing separating them: 0
##The total of the digits in the string you entered is 0
##
##Test Case 5.
##
##Enter a sequence of digits with nothing separating them: 9485678302945
##The total of the digits in the string you entered is 70

