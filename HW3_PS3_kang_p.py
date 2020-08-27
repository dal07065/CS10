# Lina Kang
# 1072568
# HW 03 PS 3 - Credit Card Validity Program

def main():
    loop = int(input("How many credit card numbers would you like to check?: "))
    print()

    for num in range(loop):
        #user will input the credit card number as a string
        creditCard = input("Enter a credit card number as a long integer: ")
               
        #call the function isValid() and print whether the credit card number is valid or not valid
        validity = isValid(creditCard)

        if validity == True:
            print(creditCard, "is valid.")
            print()
        else:
            print(creditCard, "is invalid.")
            print()
            


# Return true if the card number is valid 
def isValid(number:str)->(bool):

    validity = False;

    length = len(number)
    
    if number.startswith('4') or number.startswith('5') or number.startswith('37') or number.startswith('6'):
        
        if length >= 13 and length <= 16:
            
            # calculate the sum of even index numbers and the sum of odd index numbers
            evenSum = sumOfDoubleEvenPlace(number)
            oddSum = sumOfOddPlace(number)
            
            sum = evenSum + oddSum

            # if total sum is divisible by 10, the number is valid. Otherwise, invalid.
            if sum%10 == 0:
                validity = True;
                
    return validity;


# Return the sum of even place digits from right to left
def sumOfDoubleEvenPlace(number:str)->(int):
    
    sum = 0
    
    # check every other number from Right to left starting from second to last number
    for num in range(len(number)-2,-2,-2):
        temp = int(number[num])
        temp = temp * 2
        temp = getDigit(temp)
        sum = sum + temp
        
    return sum


# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number:str)->(int):
    
    digit = number
    
    if number/10 >= 1:
        tenth = int(number/10)
        oneth = number - (10*tenth)
        digit = tenth + oneth
        
    return digit


# Return the sum of the odd place digits
def sumOfOddPlace(number:str):
    sum = 0
    
    # check every other number from right to left starting from the very last number
    for num in range(len(number)-1,0,-2):
        sum = sum + int(number[num])
        
    return sum


if __name__ == "__main__":
    main()

## Test Case 1.
##    
##How many credit card numbers would you like to check?: 2
##
##Enter a credit card number as a long integer: 4388576018402626
##4388576018402626 is invalid.
##
##Enter a credit card number as a long integer: 4388576018410707
##4388576018410707 is valid.
##
## Test Case 2.
##
##How many credit card numbers would you like to check?: 4
##
##Enter a credit card number as a long integer: 5574236957371433
##5574236957371433 is valid.
##
##Enter a credit card number as a long integer: 5574235324830527
##5574235324830527 is valid.
##
##Enter a credit card number as a long integer: 5574235604250701
##5574235604250701 is valid.
##
##Enter a credit card number as a long integer: 349357305673562
##349357305673562 is invalid.
##
## Test Case 3.
##
##How many credit card numbers would you like to check?: 5
##
##Enter a credit card number as a long integer: 379865015741677
##379865015741677 is invalid.
##
##Enter a credit card number as a long integer: 379865015741777
##379865015741777 is valid.
##
##Enter a credit card number as a long integer: 6011009644571734
##6011009644571734 is valid.
##
##Enter a credit card number as a long integer: 6011387576415074
##6011387576415074 is valid.
##
##Enter a credit card number as a long integer: 6011200172735672
##6011200172735672 is valid.
##
## Test Case 4.
##
##How many credit card numbers would you like to check?: 3
##
##Enter a credit card number as a long integer: -1
##-1 is invalid.
##
##Enter a credit card number as a long integer: 0
##0 is invalid.
##
##Enter a credit card number as a long integer: 3785352
##3785352 is invalid.
##
## Test Case 5.
##
##How many credit card numbers would you like to check?: 3
##
##Enter a credit card number as a long integer: 4047414013514575
##4047414013514575 is valid.
##
##Enter a credit card number as a long integer: 4047414013514573
##4047414013514573 is invalid.
##
##Enter a credit card number as a long integer: 4047414013514574
##4047414013514574 is invalid.
##
## Test Case 6.
##
##How many credit card numbers would you like to check?: 5
##
##Enter a credit card number as a long integer: 378535260094162
##378535260094262 is valid.
##
##Enter a credit card number as a long integer: 378535260094262
##378535260094262 is invalid.
##
##Enter a credit card number as a long integer: 373488824050575
##373488824050575 is invalid.
##
##Enter a credit card number as a long integer: 6389053584842576
##6389053584842576 is valid.
##
##Enter a credit card number as a long integer: 6390859400858357
##6390859400858357 is valid.
##
## Test Case 7.
##
##How many credit card numbers would you like to check?: 1
##
##Enter a credit card number as a long integer: 5532144029320878
##5532144029320878 is valid.
##
## Test Case 8.
##
##How many credit card numbers would you like to check?: 2
##
##Enter a credit card number as a long integer: 6390859400858359
##6390859400858359 is invalid.
##
##Enter a credit card number as a long integer: 6387141811488149
##6387141811488149 is valid.
##
## Test Case 9.
##
##How many credit card numbers would you like to check?: 2
##
##Enter a credit card number as a long integer: 5018454520130053
##5018454520130053 is valid.
##
##Enter a credit card number as a long integer: 4485590548542055
##4485590548542055 is valid.
##

