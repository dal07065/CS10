# Lina Kang
# 1072568
# This program reads in "tea.txt" file and display it in a formatted manner

def teaRead()->(dict, float, float, float):
    '''Read in 'tea.txt' and transfer the data to a dictionary format'''
    
    infile = open('tea.txt', 'r')
    
    tea = {}
    
    store1_Total = 0
    store2_Total = 0
    store3_Total = 0
    
    for line in infile:
        
        list = []
        index = line.find(':')
        tea_name = line[:index]
        line = line[index+1:]
        
        index = line.find(':')
        store1_Sales = float(line[:index])
        store1_Total = store1_Total + store1_Sales
        line = line[index+1:]
        
        index = line.find(':')
        store2_Sales = float(line[:index])
        store2_Total = store2_Total + store2_Sales
        line = line[index+1:]
        
        index = line.find(':')
        store3_Sales = float(line[:index])
        store3_Total = store3_Total + store3_Sales
        line = line[index+1:]
        
        totalValue = store1_Sales + store2_Sales + store3_Sales
        
        list.append(store1_Sales)
        list.append(store2_Sales)
        list.append(store3_Sales)
        list.append(totalValue)
        
        tea[tea_name] = list
        
    infile.close()
    
    return tea, store1_Total, store2_Total, store3_Total


def displayDict(dictionary:dict, total_1:float, total_2:float, total_3:float)->None:
    '''Display the information read from teaRead()'''
    for key in sorted(dictionary):
        
        blankSpace = 10 - len(key)
        
        print("%-10s" % (key), end='')
        
        store1 = (dictionary[key])[0]
        store2 = (dictionary[key])[1]
        store3 = (dictionary[key])[2]
        total = (dictionary[key])[3]
        
        print(format(store1, '10.2f'), format(store2, '10.2f'), format(store3, '10.2f'), format(total, '10.2f'), )

    print("%-9s" % (' '), format(total_1, '10.2f'), format(total_2, '10.2f'), format(total_3, '10.2f'))
    

def main():
    tea, store1_Total, store2_Total, store3_Total = teaRead()
    displayDict(tea, store1_Total, store2_Total, store3_Total)


if __name__ == "__main__":
    main()

##Output
##
##Ceylon       6700.10    5012.45    6011.00   17723.55
##Earl Grey   10225.25    9025.00    9505.00   28755.25
##Green Tea    8580.00    7201.25    8900.00   24681.25
##Jasmine      9285.15    8276.10    8705.00   26266.25
##Mint Tea     7901.25    4267.00    7056.50   19224.75
##            42691.75   33781.80   40177.50
