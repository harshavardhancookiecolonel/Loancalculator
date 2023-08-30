import math

print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal: ''')

choice = input()

if choice == "a":
    print("Enter loan principal: ")
    P = int(input())
    print("Enter number of periods: ")
    n = int(input())
    print("Enter loan interest: ")
    i = float(input())
    Li = float(i / (12 * 100))
    A = math.ceil(P * (Li * pow((1 + Li), n)) / (pow((1 + Li), n) - 1)) 
    print("Your monthly payments = " + str(A) + "!")
elif choice == "n":
    P = int(input("Enter the loan principal:\n"))
    A = int(input("Enter the monthly payment:\n"))
    i = float(input("Enter the loan interest:\n"))
    Li = float(i / (12 * 100))
    x = A / (A - Li * P)  
    n = math.ceil(math.log(x, 1 + Li))
    years = n // 12
    months = n % 12
    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif years == 1:
        print(f"It will take 1 year and {months} months to repay this loan!")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")
elif choice == "p":
    print("Enter the annuity payment: ")
    A = float(input())
    print("Enter number of periods: ")
    n = int(input())
    print("Enter the loan interest: ")
    i = float(input())
    Li = float(i / (12 * 100))
    P = math.ceil(A / ((Li * math.pow((1 + Li), n)) / (math.pow((1 + Li), n) - 1))) 
    print("Your loan principal = " + str(P))
