balance = 1200
annualInterestRate = 0.2
MinimumFixedMonthlyPayment = 0
Month = 0
MonthlyInterestRate = (annualInterestRate) / 12.0
FinalBalance = 0

while FinalBalance > 0:
    
    MinimumFixedMonthlyPayment += 10 
        
    while Month < 12:

            MonthlyUnpaidBalance = (balance) - (MinimumFixedMonthlyPayment)

            UpdatedBalanceEachMonth = (MonthlyUnpaidBalance) + (MonthlyInterestRate * MonthlyUnpaidBalance) 
        
            balance = UpdatedBalanceEachMonth
        
            Month += 1
    
            FinalBalance = balance
         
     
          
    



print 'UpdatedBalanceEachMonth: ' + str (UpdatedBalanceEachMonth)
print 'balance: ' + str (balance)
print 'FinalBalance: ' + str (FinalBalance)

print 'Lowest Payment: ' + str (MinimumFixedMonthlyPayment)