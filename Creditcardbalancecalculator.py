#Problem Set 2, Problem 2: Paying Debt Off in a Year
# Write a program that calculates the minimum fixed monthly payment needed in
# order pay off a credit card balance within 12 months. 
# By a fixed monthly payment, we mean a single number which does not change each month, 
# but instead is a constant amount that will be paid each month.

# Specifications:
# No need for a minimum monthly payment 
# Print out one line the lowest monthly payment that will pay off all debt in under 1 year

#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

balance = 3329
annualInterestRate = 0.2
#Answer for lowest payment should be: 310
numMonths = 0
MonthlyInterestRate = annualInterestRate/12
UpdatedBalance = balance 

#using financial formula for amortization payment
MonthlyPayment = UpdatedBalance * (MonthlyInterestRate*(1+MonthlyInterestRate)**12)/((1+MonthlyInterestRate)**12 - 1)
print('Lowest Payment:' + str(round(MonthlyPayment,-1)))

#using while loops
def payment(balance, MonthlyInterestRate):
    MonthlyPayment = 0
    TotalPaid = 0
    RemainingBalance = balance
    while RemainingBalance >0:
        MonthlyPayment +=10
        numMonths = 0
        UpdatedBalance = balance
        while numMonths <12:
            UnpaidBalance = UpdatedBalance - MonthlyPayment
            UpdatedBalance = UnpaidBalance + (MonthlyInterestRate*UnpaidBalance)
            numMonths +=1
            RemainingBalance = UpdatedBalance
    print('Lowest Payment:' + str(round(MonthlyPayment,-1)))
payment(balance,MonthlyInterestRate)




