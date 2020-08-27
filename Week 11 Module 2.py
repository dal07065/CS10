def main():
    
    print("Enter 5 numbers: ")

    numbers = []

    for x in range(5):
        temp = int(input(""))
        numbers.append(temp*10)

    

    for x in range(4, -1, -1):
        print(float(numbers[x]), end =" ")

if __name__ == "__main__":
    main()
    
