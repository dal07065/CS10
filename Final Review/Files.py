def writeFile():

    string = "Blueberries Strawberries Blackberries Raspberries " + \
             "Bosenberries Gozenberries Fravernberries"
    listString = string.split()
    print(listString)
    setOne = set(listString)
    
    #setOne = {'Blueberries', 'Strawberries', 'Blackberries', 'Raspberries'}

    outfile = open('Pancakes.txt', 'w')
    #outfile.close()
    
    #outfile = open(r'c:\users\lina\desktop\philosophers.txt', 'a')

    for string in setOne:
        outfile.write(string)
        outfile.write('\n')

    outfile.close()


def readFile():
    infile = open('Pancakes.txt', 'r')
    fileContents = infile.read()
    infile.close()
    print(fileContents)

def readFileByLine():
    infile = open('Pancakes.txt', 'r')
    line1 = infile.readline()
    line1 = line1.rstrip('\n')
    infile.close()
    print(line1)

def threeFriends():
    print('Enter the names of three friends.')
    one = input('Friend #1: ')
    two = input('Friend #2: ')
    three = input('Friend #3: ')

    outFile = open('friends.txt', 'w')
    outFile.write('My three friends are\n')
    outFile.write(one + '\n')
    outFile.write(two + '\n')
    outFile.write(three + '\n')

    outFile.close()
    print('The names were written to friends.txt')

def threeFriendsRead():
    infile = open('friends.txt', 'r')

    firstFriend = infile.readline()

    secondFriend = infile.readline()

    thirdWheel = infile.readline()

    print(firstFriend + secondFriend + thirdWheel.rstrip('\n'))

days = 0

def filesWithNumbers():
    global days

    print('filesWithNumbers\n' + 'Mark two' + '_and_three')
    
    days = int(input("For how many days do you have sales? "))

    sales = []

    for n in range(days):
        #print("Enter the sales for day #", n+1, sep='', end='')
        temp = input("Enter the sales for day #"+ str(n+1)+ ": ")
        sales.append(temp)

    outfile = open('sales.txt', 'w')
    
    for n in range(days):
        temp = 'Day #' + str(n+1) + ": " + sales[n] + '\n'
        outfile.write(temp)
    print()
    
    outfile.close()

    print("Data written to sales.txt\n")

def filesWithNumbersTwo():
    global days
    print('filesWithNumbersTwo\n')

    totalSales = 0
    sales = []

    infile = open('sales.txt', 'r')

    print('Reading...')
    for num in range(days):
        temp = infile.readline()
        index = temp.find(':')
        temp = temp[index+2:]
        temp = temp.rstrip('\n')
        sales.append(temp)
        print(temp)
        totalSales = totalSales + int(temp)

    infile.close()

    outfile = open('salesRead.txt', 'w')

    print('Writing...')
    for num in range(days):
        outfile.write(sales[num] + '\n')
    outfile.write('\nTotal Sales: $' + str(totalSales))
    print()
    print('Done!')
    outfile.close()

def eof_practice():

    ofile = open('Animals.txt', 'w')
    ofile.write('Crocodiles\n')
    ofile.write('Giraffes\n')
    ofile.write('Zebras\n')
    ofile.write('Lions\n')
    ofile.write('Sharks\n')

    ofile.close()

    ifile = open('Animals.txt', 'r')
##    line = ifile.readline()
##
##    print("In whileloop...")
##    while line != '':
##        print(line, end='')
##        line = ifile.readline()
        
    print("In for loop...")
    for l in ifile:
        print(l, end='')
        
    ifile.close()

def writeNumbersToFile():
    list = [1,2,3,4,5]

    outfile = open('Numbers.txt', 'w')

    for num in list:
        outfile.write(str(num)+'\n')
    outfile.close()

def readNumbersFromFile():

    infile = open('Numbers.txt', 'r')

    list = infile.readlines()

    for num in range(len(list)):
        list[num] = int(list[num])

    print(list)

def main():
    #writeFile()
    #readFile()
    #readFileByLine()
    #threeFriends()
    #threeFriendsRead()
    #filesWithNumbers()
    #filesWithNumbersTwo()
    #eof_practice()
    writeNumbersToFile()
    readNumbersFromFile()
    
if __name__ == "__main__":
    main()
