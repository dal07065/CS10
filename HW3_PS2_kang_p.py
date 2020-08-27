# Lina Kang
# 1072568
# HW 03 PS 2 - Check if a string is a palindrome or not

def isPalindrome(word:str):

    word = word.strip()
    length = len(word)
    ## index of the word to check with last index of the word
    i = 0
    ## sentinel value to indicate if word is palindrome
    boolean = 1

    ## loop that compares first index to last index while the indices changes
    while i < length:
        if word[i] != word[length-1]:
            boolean = 0
            ## terminate the loop as soon as a non-matching pair results
            i=length
        else:
            ## continue the loop
            i = i + 1
            length = length - 1
        
    if boolean == 1:
        print(word, "is a palindrome!")
    else:
        print(word, "is not a palindrome!")
            

def main():
    loop = int(input("How many words do you want to check? "))
    print()

    for num in range(loop):
        print("Enter a String", end='')
        word = input(": ")
        isPalindrome(word)
        print()

if __name__ == "__main__":
    main()

## Test Case 1.
##
##How many words do you want to check? 3
##
##Enter a String: poop
##poop is a palindrome!
##
##Enter a String: nope
##nope is not a palindrome!
##
##Enter a String: dad
##dad is a palindrome!
##
## Test Case 2.
##
##How many words do you want to check? 5
##
##Enter a String: noon
##noon is a palindrome!
##
##Enter a String: print
##print is not a palindrome!
##
##Enter a String: racecar
##racecar is a palindrome!
##
##Enter a String: speed
##speed is not a palindrome!
##
##Enter a String: y
##y is a palindrome!
##
## Test Case 3.
##
##How many words do you want to check? 1
##
##Enter a String: basketball
##basketball is not a palindrome!
##
## Test Case 4.
##
## How many words do you want to check? 0
##
##
## Test Case 5.
##
## How many words do you want to check? 2
##
##Enter a String: you uoy
##you uoy is a palindrome!
##
##Enter a String: water bottle
##water bottle is not a palindrome!
##

