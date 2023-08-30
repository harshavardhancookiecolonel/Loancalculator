import math

print("Enter the loan principal: \n")
loan_principal = int(input())
print('''What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment: ''')


choice = input()

if choice == 'm':
    print("Enter monthly payment: ")
    payment = int(input())
    month = math.ceil(loan_principal / payment)
    if month == 1:
        print()
        print("it will take" + str(month) + "month to clear the loan")
    else:
        print()
        print("it will take " + str(month) + " months to clear the loan")
elif choice == "p":
    print("enter the number of months: ")
    month = int(input())
    payment = math.ceil(loan_principal / month)
    last_payment = loan_principal - (month - 1) * payment
    if payment == last_payment:
        print()
        print("your monthly payment = " + str(payment))
    else:
        print()
        print("your monthly payment = " + str(payment) + " and the last_payment = " + str(last_payment))
    

