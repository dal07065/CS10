def userInput()->(list):
    
    num = []

    answer = 'Y'
    
    while answer.upper() == "Y":
        score = int(input("Enter a test score: "))
        num.append(score)
        print("Do you want to add another score?")
        answer = input("y = yes, anything else = no: ")
        print()

    return num


def calcAvg(num:list)->(float):

    lowest = num[0]
    sum = 0

    for x in range(1, len(num), 1):
        temp = num[x]
        if(temp < lowest):
            lowest = temp

    num.remove(lowest)

    for x in range(len(num)):
        sum = sum + num[x]

    avg = float(sum / len(num))

    return avg


def main():
    numbers = userInput()
    average = calcAvg(numbers)

    print("The average, with the lowest score dropped is:", average)

if __name__ == "__main__":
    main()
        

    
