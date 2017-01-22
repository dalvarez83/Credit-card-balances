#Problem Set 2, problem 1: Paying the minimum
# Write a program to calculate the credit card balance 
# after one year if a person only pays the minimum monthly payment required 
# by the credit card company each month.

balance = 4213
annualInterestRate = .2
monthlyPaymentRate = .04

MonthlyInterestRate = annualInterestRate/12
numMonths =0
UpdatedBalance = balance
TotalPaid = 0

for i in range(0,12):
   numMonths +=1   
   MinimumPayment = monthlyPaymentRate * UpdatedBalance
   UnpaidBalance = UpdatedBalance - MinimumPayment
   UpdatedBalance = UnpaidBalance + (MonthlyInterestRate * UnpaidBalance)
   print('Month:' + str(numMonths))
   print('Minimum monthly payment:' + str(round(MinimumPayment,2)))
   print('Remaining balance:' + str(round(UpdatedBalance,2)))
   TotalPaid += MinimumPayment              
print('Total paid:' + str(round(TotalPaid,2)))
print('Remaining balance:' + str(round(UpdatedBalance,2)))