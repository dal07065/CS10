# Lina Kang
# 1072568
# HW 03 PS 1 - Stock Transaction Program

# receive input from user regarding the stocks
def userInput()->(str, int, float, float, float):
    name = input("Enter Stock name: ")
    shares = int(input("Enter Number of shares: "))
    purchasePrice = float(input("Enter Purchase price: "))
    sellingPrice = float(input("Enter Selling Price: "))
    commission = float(input("Enter Commission: "))
    print()

    return name, shares, purchasePrice, sellingPrice, commission


# calculate the amount paid and sold for the stock, broker commission, and the profit 
def calculate(shares:int, purchasePrice:float, sellingPrice:float, commission: float)->(float, float, float, float, float):
    stockPaid = shares * purchasePrice
    commissionBought = stockPaid * commission
    stockSold = shares * sellingPrice
    commissionSold = stockSold * commission

    moneyleft = (stockSold - commissionSold) - (stockPaid + commissionBought) 

    return stockPaid, commissionBought, stockSold, commissionSold, moneyleft


# output the calculated data from calculate function
def display(name:str, stockPaid:float, commissionBought:float, stockSold:float, commissionSold:float, moneyLeft:float)->None:
    print("Stock Name: ", name)
    print()
    print("Amount paid for the stock:       $ ", format(stockPaid, '10,.2f'), sep='')
    print("Commission paid on the purchase: $ ", format(commissionBought, '10,.2f'), sep='')
    print("Amount the stock sold for:       $ ", format(stockSold, '10,.2f'), sep='')
    print("Commission paid on the sale:     $ ", format(commissionSold, '10,.2f'), sep='')
    print("Profit(or loss if negative):     $ ", format(moneyLeft, '10,.2f'), sep='')


def main():
    # number of loops to run according to the number of transactions 
    sentinel = input("Would you like to make a transaction? (Y/N): ")
    print()
    print("*************************")
    
    while sentinel == 'y' or sentinel == 'Y':
        # call function userInput, calculate, and display within this loop for every transaction
        
        name, shares, purchasePrice, sellingPrice, commission = userInput()
        print()
        stockPaid, commissionBought, stockSold, commissionSold, moneyLeft = calculate(shares, purchasePrice, sellingPrice, commission)
        display(name, stockPaid, commissionBought, stockSold, commissionSold, moneyLeft)

        print()
        sentinel = input("Would you like to make another transaction? (Y/N): ")
        print()
        print("*************************")    


if __name__=="__main__":
    main()

## Test Case 1.
##
##Would you like to make a transaction? (Y/N): y
##
##*************************
##Enter Stock name: Kaplack Inc.
##Enter Number of shares: 10000
##Enter Purchase price: 33.92
##Enter Selling Price: 35.92
##Enter Commission: 0.04
##
##
##Stock Name:  Kaplack Inc.
##
##Amount paid for the stock:       $ 339,200.00
##Commission paid on the purchase: $  13,568.00
##Amount the stock sold for:       $ 359,200.00
##Commission paid on the sale:     $  14,368.00
##Profit(or loss if negative):     $  -7,936.00
##
##Would you like to make another transaction? (Y/N): y
##
##*************************
##Enter Stock name: Monsters Inc
##Enter Number of shares: 2000
##Enter Purchase price: 45.92
##Enter Selling Price: 53.20
##Enter Commission: 0.03
##
##
##Stock Name:  Monsters Inc
##
##Amount paid for the stock:       $  91,840.00
##Commission paid on the purchase: $   2,755.20
##Amount the stock sold for:       $ 106,400.00
##Commission paid on the sale:     $   3,192.00
##Profit(or loss if negative):     $   8,612.80
##
##Would you like to make another transaction? (Y/N): y
##
##*************************
##Enter Stock name: Bottles Corp
##Enter Number of shares: 3000
##Enter Purchase price: 23.94
##Enter Selling Price: 19.99
##Enter Commission: 0.045
##
##
##Stock Name:  Bottles Corp
##
##Amount paid for the stock:       $  71,820.00
##Commission paid on the purchase: $   3,231.90
##Amount the stock sold for:       $  59,970.00
##Commission paid on the sale:     $   2,698.65
##Profit(or loss if negative):     $ -17,780.55
##
##Would you like to make another transaction? (Y/N): y
##
##*************************
##Enter Stock name: Wheat TinTins
##Enter Number of shares: 2048
##Enter Purchase price: 12.80
##Enter Selling Price: 25.50
##Enter Commission: 0.08
##
##
##Stock Name:  Wheat TinTins
##
##Amount paid for the stock:       $  26,214.40
##Commission paid on the purchase: $   2,097.15
##Amount the stock sold for:       $  52,224.00
##Commission paid on the sale:     $   4,177.92
##Profit(or loss if negative):     $  19,734.53
##
##Would you like to make another transaction? (Y/N): y
##
##*************************
##Enter Stock name: Jacobson Inc.
##Enter Number of shares: 12345
##Enter Purchase price: 7.98
##Enter Selling Price: 10.11
##Enter Commission: 0.012
##
##
##Stock Name:  Jacobson Inc.
##
##Amount paid for the stock:       $  98,513.10
##Commission paid on the purchase: $   1,182.16
##Amount the stock sold for:       $ 124,807.95
##Commission paid on the sale:     $   1,497.70
##Profit(or loss if negative):     $  23,615.00
##
##Would you like to make another transaction? (Y/N): n
##
##*************************
##
## Test Case 2.
##
##Would you like to make a transaction? (Y/N): y
##
##*************************
##Enter Stock name: Lenovo Group LTD
##Enter Number of shares: 8000
##Enter Purchase price: 0.5075
##Enter Selling Price: 0.8023
##Enter Commission: 0.02
##
##
##Stock Name:  Lenovo Group LTD
##
##Amount paid for the stock:       $   4,060.00
##Commission paid on the purchase: $      81.20
##Amount the stock sold for:       $   6,418.40
##Commission paid on the sale:     $     128.37
##Profit(or loss if negative):     $   2,148.83
##
##Would you like to make another transaction? (Y/N): y
##
##*************************
##Enter Stock name: Netflix Inc
##Enter Number of shares: 4300
##Enter Purchase price: 32.93
##Enter Selling Price: 37.92
##Enter Commission: 0.06
##
##
##Stock Name:  Netflix Inc
##
##Amount paid for the stock:       $ 141,599.00
##Commission paid on the purchase: $   8,495.94
##Amount the stock sold for:       $ 163,056.00
##Commission paid on the sale:     $   9,783.36
##Profit(or loss if negative):     $   3,177.70
##
##Would you like to make another transaction? (Y/N): n
##
##*************************
##
## Test Case 3.
##
##Would you like to make a transaction? (Y/N): y
##
##*************************
##Enter Stock name: HP Inc
##Enter Number of shares: 2300
##Enter Purchase price: 14.23
##Enter Selling Price: 12.12
##Enter Commission: 0.04
##
##
##Stock Name:  HP Inc
##
##Amount paid for the stock:       $  32,729.00
##Commission paid on the purchase: $   1,309.16
##Amount the stock sold for:       $  27,876.00
##Commission paid on the sale:     $   1,115.04
##Profit(or loss if negative):     $  -7,277.20
##
##Would you like to make another transaction? (Y/N): n
##
##*************************
##
## Test Case 4.
##
##Would you like to make a transaction? (Y/N): y
##
##*************************
##Enter Stock name: Awesome Company
##Enter Number of shares: 6000
##Enter Purchase price: 93.23
##Enter Selling Price: 86.23
##Enter Commission: 0.02
##
##
##Stock Name:  Awesome Company
##
##Amount paid for the stock:       $ 559,380.00
##Commission paid on the purchase: $  11,187.60
##Amount the stock sold for:       $ 517,380.00
##Commission paid on the sale:     $  10,347.60
##Profit(or loss if negative):     $ -63,535.20
##
##Would you like to make another transaction? (Y/N): y
##
##*************************
##Enter Stock name: Awesome Company Jr.
##Enter Number of shares: 300
##Enter Purchase price: 86.23
##Enter Selling Price: 120.34
##Enter Commission: 0.01
##
##
##Stock Name:  Awesome Company Jr.
##
##Amount paid for the stock:       $  25,869.00
##Commission paid on the purchase: $     258.69
##Amount the stock sold for:       $  36,102.00
##Commission paid on the sale:     $     361.02
##Profit(or loss if negative):     $   9,613.29
##
##Would you like to make another transaction? (Y/N): y
##
##*************************
##Enter Stock name: Awesome Company Jr. Jr.
##Enter Number of shares: 1200
##Enter Purchase price: 12.34
##Enter Selling Price: 12.53
##Enter Commission: 0.04
##
##
##Stock Name:  Awesome Company Jr. Jr.
##
##Amount paid for the stock:       $  14,808.00
##Commission paid on the purchase: $     592.32
##Amount the stock sold for:       $  15,036.00
##Commission paid on the sale:     $     601.44
##Profit(or loss if negative):     $    -965.76
##
##Would you like to make another transaction? (Y/N): n
##
##*************************
##
## Test Case 5.
##
##Would you like to make a transaction? (Y/N): n
##
##*************************
