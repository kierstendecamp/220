
'''
Kiersten DeCamp
Lab 1
The following code is my work.
'''


annual_interest = (eval(input("What is annual interest rate? "))) / 100


billing_cycle = eval(input("what is the number of days in billing cycle? "))


net_balance = eval(input("what is the net balance ?"))

payment_made = eval(input(" What day was the payment made ?"))

payment_ammount = eval(input("what is the payment ammount ?"))

step_1 = net_balance * billing_cycle

step_2 = payment_ammount * (billing_cycle - payment_made)

step_3 = step_1 - step_2

avg_daily_balance = step_3/ billing_cycle

monthly_interest = round(avg_daily_balance * (annual_interest / 12), 2)

print(monthly_interest)