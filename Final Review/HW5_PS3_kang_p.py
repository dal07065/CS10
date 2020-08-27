# Lina Kang
# 1072568
# This program creates a class Loan and exercises the usage of classes and objects

class Loan:
    '''Construct a loan object'''
    def __init__(self, annualInterestRate = 2.5, numberOfYears = 1.0, loanAmount = 1000.0, borrower = " "):
        '''Initializes the Loan class object'''
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
        self.__borrower = borrower


    def getAnnualInterestRate(self):
        '''Returns "annualInterestRate"'''
        return self.__annualInterestRate

    
    def getNumberOfYears(self):
        '''Returns "numberOfYears"'''
        return self.__numberOfYears

    
    def getLoanAmount(self):
        '''Returns "loanAmount"'''
        return self.__loanAmount

    
    def getBorrower(self):
        '''Returns "borrower"'''
        return self.__borrower


    def setAnnualInterestRate(self, change:float):
        '''Changes the value of "annualInterestRate"'''
        self.__annualInterestRate = change

    
    def setNumberOfYears(self, change:float):
        '''Changes the value of "numberOfYears"'''
        self.__numberOfYears = change

    
    def setLoanAmount(self, change:float):
        '''Changes the value of "loanAmount"'''
        self.__loanAmount = change

    
    def setBorrower(self, change:float):
        '''Changes the value of "borrower"'''
        self.__borrower = change


    def getMonthlyPayment(self)->float:
        '''Returns monthlyPayment'''
        if self.__annualInterestRate == 0:
            monthlyPayment = self.__loanAmount / (self.__numberOfYears*12)
            return monthlyPayment
        monthlyInterestRate = self.__annualInterestRate/1200
        monthlyPayment = self.__loanAmount * monthlyInterestRate / (1-(1/(1+monthlyInterestRate)**(self.__numberOfYears*12)))
        
        return monthlyPayment


    def getTotalPayment(self)->float:
        '''Returns totalPayment'''
        totalPayment = self.getMonthlyPayment() * self.__numberOfYears * 12
        
        return totalPayment


def main():
    loan1 = Loan()

    # input
    interestRate = float(input("Enter yearly interest rate: "))
    numYears = float(input("Enter number of years as an integer: "))
    
    while numYears < 1:
        print()
        print("Number of years cannot be less than 1.")
        numYears = float(input("Enter number of years as an integer: "))
        
    loanAmt = float(input("Enter loan amount: "))
    borrower = input("Enter a borrower's name: ")

    # set object data members
    loan1.setAnnualInterestRate(interestRate)
    loan1.setNumberOfYears(numYears)
    loan1.setLoanAmount(loanAmt)
    loan1.setBorrower(borrower)

    # output
    print("The loan is for", loan1.getBorrower())
    print("The monthly payment is", format(loan1.getMonthlyPayment(), ',.2f'))
    print("The total payment is", format(loan1.getTotalPayment(), ',.2f'))

    choice = input("Do you want to change the loan amount? Y for yes or enter to quit ")
    
    if choice == 'Y' or choice == 'y' or choice == 'yes' or choice == 'Yes':
        newLoanAmt = float(input("Enter new loan amount "))
        loan1.setLoanAmount(newLoanAmt)
        print("The loan is for", loan1.getBorrower())
        print("The monthly payment is", format(loan1.getMonthlyPayment(), ',.2f'))
        print("The total payment is", format(loan1.getTotalPayment(), ',.2f'))
                

if __name__ == "__main__":
    main()

## Output with 5 Test Cases
##
## Test Case 1.
##    
##Enter yearly interest rate: 2.5
##Enter number of years as an integer: 5
##Enter loan amount: 1000.00
##Enter a borrower's name: John Jones
##The loan is for John Jones
##The monthly payment is 17.75
##The total payment is 1,064.84
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount 5000
##The loan is for John Jones
##The monthly payment is 88.74
##The total payment is 5,324.21 
##
## Test Case 2.
##
##Enter yearly interest rate: 1
##Enter number of years as an integer: 1
##Enter loan amount: 500
##Enter a borrower's name: Lina Kang
##The loan is for Lina Kang
##The monthly payment is 41.89
##The total payment is 502.71
##Do you want to change the loan amount? Y for yes or enter to quit n
##
## Test Case 3.
##    
##Enter yearly interest rate: 0
##Enter number of years as an integer: 1
##Enter loan amount: 500
##Enter a borrower's name: Lina
##The loan is for Lina
##The monthly payment is 41.67
##The total payment is 500.00
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount 600
##The loan is for Lina
##The monthly payment is 50.00
##The total payment is 600.00
##
## Test Case 4.
##
##Enter yearly interest rate: 10
##Enter number of years as an integer: 0
##
##Number of years cannot be less than 1.
##Enter number of years as an integer: 5
##Enter loan amount: 4500.99
##Enter a borrower's name: Kevin Zhang
##The loan is for Kevin Zhang
##The monthly payment is 95.63
##The total payment is 5,737.96
##Do you want to change the loan amount? Y for yes or enter to quit yes
##Enter new loan amount 4500
##The loan is for Kevin Zhang
##The monthly payment is 95.61
##The total payment is 5,736.70
##
## Test Case 5.
##
##Enter yearly interest rate: 1.5
##Enter number of years as an integer: 3
##Enter loan amount: 0
##Enter a borrower's name: Jim Carrey
##The loan is for Jim Carrey
##The monthly payment is 0.00
##The total payment is 0.00
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount 12345.99
##The loan is for Jim Carrey
##The monthly payment is 350.93
##The total payment is 12,633.57
