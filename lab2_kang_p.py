# Lina Kang
# 1072568
# This program details the solutions to the questions on Lab 02

## Question 1

eligibleAge = 18

age = int(input("Enter the age: "))

if age < eligibleAge:
    eligibleAge -= age
    print("You have to wait for another", eligibleAge, " to cast your vote.")
else:
    print("You are eligible to vote!")

## Question 2

number = int(input("Enter any number: "))

if number%2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

## Question 3

character = input("Enter any character: ")

if character == 65:
    print(character, " is a vowel!")
elif character == 69:
    print(character, " is a vowel!")
elif character == 73:
    print(character, " is a vowel!")
elif character == 79:
    print(character, " is a vowel!")
elif character == 85:
    print(character, " is a vowel!")
elif character == 97:
    print(character, " is a vowel!")
elif character == 101:
    print(character, " is a vowel!")
elif character == 105:
    print(character, " is a vowel!")
elif character == 111:
    print(character, " is a vowel!")
elif character == 117:
    print(character, " is a vowel!")
else:
    print(character, " is not a vowel!")

## Question 4

character = input("Enter any character: ")

if character < 65:
    print("A number was entered")
elif character < 91:
    print("Uppercase character was entered")
else:
    print("Lowercase character was entered")

## Question 5

stars = int(input("How many stars do you want? "))

i = 0

while i < stars:
    print("*", sep='', end ='')
    i = i + 1

## Question 6

taxFactor = 0.0065

print("Enter the property lot number or enter -999 to end")
lot = int(input("Enter the lot number: "))

while lot != -999:
    value = int(input("Enter property value: "))

    tax = value * taxFactor

    print("Property tax: $", format(tax, ',.2f'), sep = '')

    print("Enter the property lot number or enter -999 to end")
    lot = int(input("Enter the lot number: "))

## Question 7
    
markup = 2.5

choice = 'y'

while choice == 'y':
    
    wholesale = float(input("Enter the item's wholesale cost: "))

    if wholesale > 0:
        retail = wholesale * markup
        print("Retail price is $", format(retail, ',.2f'), sep = '')
        choice = input("Do you have another item? (Enter y for yes): ")
    else:
        print("ERROR: the cost cannot be negative: ")

## Question 8

for num in range(5):
    print("Barzinger!")

## Question 9

sum = 0
num = int(input("How many numbers do you want to add? "))

for i in range(num):
    number = int(input("Enter number", i, ": "))
    sum += number

print("The total is", format(sum, ",.f"))

## Question 10

factor = 0.6214

kph = 60
mph = 0

print("KPH     MPH     ")
print("----------------")

for num in range(8):
    mph = kph * factor
    print(format(kph, '3,d'), format(mph, '8,.1f'))
    kph += 10

##Test Case 1.
##
##KPH     MPH     
##----------------
## 60     37.3
## 70     43.5
## 80     49.7
## 90     55.9
##100     62.1
##110     68.4
##120     74.6
##130     80.8
  



    
        
