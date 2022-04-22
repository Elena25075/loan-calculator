import argparse
import math

def differentiated_payments():
    interest = args.interest / 12 / 100
    m = 1
    t = 1
    count = 0
    for i in range(args.periods):
        part1 = args.principal / args.periods
        part2 = args.principal - ((args.principal * (m - 1)) / args.periods)
        part3 = interest * part2
        diff = math.ceil(part1 + part3)
        m += 1
        print(f"Month {t}: {diff}")
        t += 1
        count += diff

    print(f"Overpayment = {count - args.principal}")

def annuity_payment():
    i = args.interest / (12 * 100)
    part1 = i * math.pow((1 + i), args.periods)
    part2 = math.pow((1 + i), args.periods) - 1
    part3 = part1 / part2
    a = args.principal * part3
    a = math.ceil(a)
    print(f"Your monthly payment = {a}!")
    print(f"Overpayment = {a * args.periods - args.principal}")

def loan_principal():
    i = args.interest / (12 * 100)
    part1 = i * math.pow((1 + i), args.periods)
    part2 = math.pow((1 + i), args.periods) - 1
    part3 = part1 / part2
    p = args.payment / part3
    print('Your loan principal = ' '%.0f' % p)
    overpay = math.ceil(args.payment * args.periods - p)
    print(f"Overpayment = {overpay}")

def number_of_payments():
    i = args.interest / (12 * 100)
    n = math.log((args.payment / (args.payment - i * args.principal)), (1 + i))
    n = math.ceil(n)
    if n % 12 == 0:
        year = n / 12
        if year == 1:
            year = int(year)
            print(f'It will take {year} year to repay this loan!')
        elif year > 1:
            year = int(year)
            print(f'It will take {year} years to repay this loan!')
    if n % 12 > 0:
        year = n // 12
        month = n - (year * 12)
        if month == 1 and year == 1:
            year = int(year)
            month = int(month)
            print(f"It will take {year} year and {month} month to repay this loan!")
        else:
            year = int(year)
            month = int(month)
            print(f"It will take {year} years and {month} months to repay this loan!")
    over = args.payment * n - args.principal
    print(f'Overpayment = {over}')

parser = argparse.ArgumentParser(description="This is Loan Calculator")
parser.add_argument('-t', '--type', type=str)
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()
alist = []

for arg in vars(args):
    if getattr(args, arg) is not None:
        alist.append(getattr(args, arg))
alist2 = []
for i in range(1, len(alist)):
    alist[i] = float(alist[i])
    alist2.append(alist[i])
    a = sum(i < 0 for i in alist2)
    if a > 0:
        print('Incorrect operator')


if args.type == 'diff':
    if args.principal and args.periods and args.type and args.interest:
        differentiated_payments()
    else:
        print('Incorrect parameters')
elif args.type == 'annuity':
    if args.principal and args.periods and args.interest:
        annuity_payment()
    elif args.payment and args.periods and args.interest:
        loan_principal()
    elif args.principal and args.payment and args.interest:
        number_of_payments()
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
