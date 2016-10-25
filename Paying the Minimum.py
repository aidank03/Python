balance = 4213
Month = 0

IR = 0.2
annualInterestRate = IR
round (IR, 2)

PR = 0.04
monthlyPaymentRate = PR
round (PR, 2)

AmountPaid = 0

while Month < 12:
    
        monthlyinterestrate = (annualInterestRate)/ 12.0
    
        minimumMonthlyPayment = (monthlyPaymentRate) * (balance)

        monthlyUnpaidBalance = (balance) - (minimumMonthlyPayment)

        UpdatedBalanceeachMonth = (monthlyUnpaidBalance) + (monthlyinterestrate * monthlyUnpaidBalance)
    
        balance = UpdatedBalanceeachMonth
        
        AmountPaid = (AmountPaid) + (minimumMonthlyPayment)

        Month += 1
    
        print 'Month: ' + str (Month) 
        print 'Minimum monthly payment: ' + str (round (minimumMonthlyPayment, 2))
        print 'Remaining balance: ' + str (round (balance, 2))

print 'Total paid: ' + str (round (AmountPaid, 2))
print 'Remaining balance: ' + str (round (balance, 2))