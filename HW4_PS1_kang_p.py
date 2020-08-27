# Lina Kang
# 1072568
# HW 4 - This program involves a collection of functions that will perform
# a certain operation on a single given list of integers.

#  Program to test functions a to j.
# 
# Define constant variables. 
ONE_TEN = [10, 9, 8, 7, 6, 6, 7, 8, 9, 10]


def swapFirstLast(data:list)->None:
    '''Swap first and last element'''
    temp = data[0]
    data[0] = data[len(data)-1]
    data[len(data)-1] = temp

    
def shiftRight(data:list)->None:
    '''Shift everything to the right and move last to first'''
    last = data[len(data)-1]
    for x in range(len(data)-1, 0, -1):
        data[x] = data[x-1]
    data[0] = last


def replaceEven(data:list)->None:
    '''Replace all even elements with zeros'''
    for x in range(len(data)):
        if data[x]%2 == 0:
            data[x] = 0


def replaceNeighbors(data:list)->None:
    '''Replace each element by larger of its two neighrbors'''
    for x in range(1, len(data)-1, 1):
        if data[x-1] < data[x+1]:
            data[x] = data[x+1]
        else:
            data[x] = data[x-1]


def removeMiddle(data:list)->None:
    '''Removes the middle elements'''
    if len(data)%2 == 0:
        middle = int(len(data)/2)-1
        data.remove(data[middle])
        data.remove(data[middle])
    else:
        middle = int(len(data)/2) + 1
        data.remove(data[middle])


def evenToFront(data:list)->None:
    '''Move all the even element to the front'''
    lastEven = -1
    for x in range(len(data)):
        tempX = data[x]
        if tempX%2 == 0:
            y = x
            while y > lastEven+1:
                tempY = data[y-1]
                data[y] = tempY
                data[y-1] = tempX
                y-=1
            lastEven = y
            
        
def secondLargest(data:list)->(int):
    '''Returns the second largest element in the list'''
    listSorted = list(data)
    listSorted.sort()
    # Remove all duplicates
    x = 0
    y = 1
    while x < len(listSorted):
        duplicate = listSorted[x]
        while y < len(listSorted):
            if duplicate == listSorted[y]:
                del listSorted[y]
            else:
                y+=1
        x+=1
        y=x+1
    second = listSorted[len(listSorted)-2]

    return second
        
    
def isIncreasing(data:list)->(bool):
    for x in range(len(data)-1):
        if data[x] > data[x+1]:
            return False
        
    return True


def hasAdjacentDuplicate(data:list)->(bool):
    '''Returns true if there are any adjacent duplicates'''
    for x in range(len(data)-1):
        if data[x] == data[x+1]:
            return True
        
    return False
            

def hasDuplicate(data:list)->(bool):
    '''Returns true if there are any duplicates'''
    # Same algorithm from lab4
    x = 0
    y = 1
    while x < len(data):
        duplicate = data[x]
        while y < len(data):
            if duplicate == data[y]:
                return True
            else:
                y+=1
        x+=1
        y=x+1
    return False

    
def main() : 
   print("The original data for all functions is: ", ONE_TEN)
   
   #   a.   Demonstrate swapping the first and last element. 
   data = list(ONE_TEN) 
   swapFirstLast(data) 
   print("After swapping first and last: ", data)
   
   #   b.   Demonstrate shifting to the right. 
   data = list(ONE_TEN) 
   shiftRight(data) 
   print("After shifting right: ", data)
   
   #   c.   Demonstrate replacing even elements with zero. 
   data = list(ONE_TEN) 
   replaceEven(data) 
   print("After replacing even elements: ", data)
   
   #   d.   Demonstrate replacing values with the larger of their neighbors. 
   data = list(ONE_TEN) 
   replaceNeighbors(data) 
   print("After replacing with neighbors: ", data)
   
   #   e.   Demonstrate removing the middle element. 
   data = list(ONE_TEN) 
   removeMiddle(data) 
   print("After removing the middle element(s): ", data)
   
   #   f.   Demonstrate moving even elements to the front of the list. 
   data = list(ONE_TEN) 
   evenToFront(data) 
   print("After moving even elements: ", data)
   
   #   g.   Demonstrate finding the second largest value. 
   print("The second largest value is: ", secondLargest(ONE_TEN))
   
   #   h.   Demonstrate testing if the list is in increasing order. 
   print("The list is in increasing order: ", isIncreasing(ONE_TEN))
   
   #   i.   Demonstrate testing if the list contains adjacent duplicates. 
   print("The list has adjacent duplicates: ", hasAdjacentDuplicate(ONE_TEN))
   
   #   j.   Demonstrate testing if the list contains duplicates. 
   print("The list has duplicates: ", hasDuplicate(ONE_TEN))
   
main() 


##Output with 5 test cases
##
##Test Case 1.
##
##The original data for all functions is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##After swapping first and last:  [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
##After shifting right:  [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
##After replacing even elements:  [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
##After replacing with neighbors:  [1, 3, 4, 5, 6, 7, 8, 9, 10, 10]
##After removing the middle element(s):  [1, 2, 3, 4, 7, 8, 9, 10]
##After moving even elements:  [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
##The second largest value is:  9
##The list is in increasing order:  True
##The list has adjacent duplicates:  False
##The list has duplicates:  False

##Test Case 2.
##
##The original data for all functions is:  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
##After swapping first and last:  [103, 20, 10, 14, 54, 16, 75, 38, 79, 12]
##After shifting right:  [103, 12, 20, 10, 14, 54, 16, 75, 38, 79]
##After replacing even elements:  [0, 0, 0, 0, 0, 0, 75, 0, 79, 103]
##After replacing with neighbors:  [12, 12, 14, 54, 54, 75, 75, 79, 103, 103]
##After removing the middle element(s):  [12, 20, 10, 14, 75, 38, 79, 103]
##After moving even elements:  [12, 20, 10, 14, 54, 16, 38, 75, 79, 103]
##The second largest value is:  79
##The list is in increasing order:  False
##The list has adjacent duplicates:  False
##The list has duplicates:  False

##Test Case 3.
##
##The original data for all functions is:  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
##After swapping first and last:  [1, 9, 8, 7, 6, 5, 4, 3, 2, 10]
##After shifting right:  [1, 10, 9, 8, 7, 6, 5, 4, 3, 2]
##After replacing even elements:  [0, 9, 0, 7, 0, 5, 0, 3, 0, 1]
##After replacing with neighbors:  [10, 10, 10, 10, 10, 10, 10, 10, 10, 1]
##After removing the middle element(s):  [10, 9, 8, 7, 4, 3, 2, 1]
##After moving even elements:  [10, 8, 6, 4, 2, 9, 7, 5, 3, 1]
##The second largest value is:  9
##The list is in increasing order:  False
##The list has adjacent duplicates:  False
##The list has duplicates:  False

##Test Case 4.
##
##The original data for all functions is:  [10, 9, 8, 7, 6, 6, 7, 8, 9, 10]
##After swapping first and last:  [10, 9, 8, 7, 6, 6, 7, 8, 9, 10]
##After shifting right:  [10, 10, 9, 8, 7, 6, 6, 7, 8, 9]
##After replacing even elements:  [0, 9, 0, 7, 0, 0, 7, 0, 9, 0]
##After replacing with neighbors:  [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
##After removing the middle element(s):  [10, 9, 8, 7, 7, 8, 9, 10]
##After moving even elements:  [10, 8, 6, 6, 8, 10, 9, 7, 7, 9]
##The second largest value is:  9
##The list is in increasing order:  False
##The list has adjacent duplicates:  True
##The list has duplicates:  True

#Test Case 5.
##
##The original data for all functions is:  [1, 4, 9, 16, 25]
##After swapping first and last:  [25, 4, 9, 16, 1]
##After shifting right:  [25, 1, 4, 9, 16]
##After replacing even elements:  [1, 0, 9, 0, 25]
##After replacing with neighbors:  [1, 9, 16, 25, 25]
##After removing the middle element(s):  [1, 4, 9, 25]
##After moving even elements:  [4, 16, 1, 9, 25]
##The second largest value is:  16
##The list is in increasing order:  True
##The list has adjacent duplicates:  False
##The list has duplicates:  False
