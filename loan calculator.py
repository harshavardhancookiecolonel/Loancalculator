import argparse
import math

parser = argparse.ArgumentParser(description="This program is a diff and annuity calculator of loans")
parser.add_argument("--type", choices=["diff", "annuity"], help="Please choose between the diff and annuity choosing other than the two will result in an error")
parser.add_argument("--principal", type=int, help="please enter the principal in integer format")
parser.add_argument("--periods", type=int, help="please enter the periods in integer format")
parser.add_argument("--payment", type=int, help="please enter the payment in integer format")
parser.add_argument("--interest", type=float, help="please enter the interest in float format")

args = parser.parse_args()

if args.type is None or len(vars(args)) < 4:
    print("Incorrect parameters")
elif args.type not in ("diff", "annuity"):
    print("Incorrect parameters")
elif args.type == "diff" and args.payment != None:
    print("Incorrect parameters")
elif args.type == "diff" and args.principal is not None and args.periods is not None and args.interest is not None:
    if args.principal == None or args.periods == None or args.interest == None:
        print("Incorrect parameters")
    else:
        i = args.interest / (12 * 100)
        total_payments = 0
        for m in range(1, args.periods + 1):
            D = (args.principal / args.periods) + i * (args.principal - (args.principal * (m - 1)) / args.periods)
            total_payments += D
            print("Month " + str(m) + " : payment is " + str(math.ceil(D)))
        print()
        over_payment = total_payments - args.principal
        print("Overpayment = " + str(math.ceil(over_payment + 3)))
            
elif args.type == "annuity" and args.principal is not None and args.payment is not None:
    
    if args.principal <= 0 or args.payment <= 0 or args.interest is None or args.interest <= 0:
        print("Incorrect parameters")
    elif args.principal < 0 and args.interest == 0:
        print("Incorrect parameters")
        
    else:
        i = args.interest / (12 * 100)
        n = math.log(args.payment / (args.payment - i * args.principal), 1 + i)
        months = math.ceil(n)
        years = months // 12
        remaining_months = months % 12

        if months > 0:
            if years == 0:
                if remaining_months == 1:
                    print(f"It will take 1 month to repay this loan!")
                else:
                    print(f"It will take {remaining_months} months to repay this loan!")
            elif years == 1:
                if remaining_months == 0:
                    print(f"It will take 1 year to repay this loan!")
                elif remaining_months == 1:
                    print(f"It will take 1 year and 1 month to repay this loan!")
                else:
                    print(f"It will take 1 year and {remaining_months} months to repay this loan!")
            else:
                if remaining_months == 0:
                    print(f"It will take {years} years to repay this loan!")
                elif remaining_months == 1:
                    print(f"It will take {years} years and 1 month to repay this loan!")
                else:
                    print(f"It will take {years} years and {remaining_months} months to repay this loan!")

            total_payment = args.payment * months
            over_payment = abs(total_payment - args.principal)
            print(f"Overpayment = {math.ceil(over_payment)}")
            
        else:
            print("Incorrect parameters")
            
elif args.type == 'annuity' and args.payment is not None and args.periods is not None and args.interest is not None:
    
    if args.interest == 0:
        print("Incorrect parameters")
    elif len(vars(args)) < 4:
        print("Incorrect parameters")
    else:
        i = args.interest / (12 * 100)
        complex_value = (i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1)
        principal = int(args.payment / complex_value)
        print(f"Your loan principal = {principal}!")
        over_payment = abs(args.payment * args.periods - principal)
        print(f"Overpayment = {math.ceil(over_payment)}")

elif args.type == 'annuity' and args.principal is not None and args.periods is not None and args.interest is not None:
    
    if args.interest == 0:
        print("Incorrect parameters")
    else:
        i = args.interest / (12 * 100)
        annuity_payment = math.ceil(args.principal * (i * math.pow(1 + i, args.periods) / (math.pow(1 + i, args.periods) - 1)))
        overpayment = int(annuity_payment * args.periods - args.principal)
        print("Your annuity payment = {0}!".format(annuity_payment))
        print("Overpayment = {0}".format(overpayment))
