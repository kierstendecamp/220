principal = eval(input("enter the principal balance: "))
apr = eval(input('enter interest rate: '))
for i in range(10):
    principal = principal * (1 + apr)
    print(principal)
    print("the final balance is", principal)

for i in range(5):
    for j in range(5):
        print(i, j, end='-')
    print()
