def get_input(question):
    """Read user input until it's not an integer and return it."""
    while True:
        try:
            return int(input(question))
        except ValueError: 
            print('The value you entered is not integer')

#get_input is a function defined to take in various variable and check whether value entered is an integer or not
#let user enter no of months he wants for loan repayment
no_of_month = get_input('Enter no of months you want for loan repayment: ')

#let user decide what interest rate he wants for the loan
interest = get_input('Enter interest rate you want for the loan: ')

#let user enter principal amount he wants for loan
principal_amt = get_input('Enter principal amount you want in loan:')
argument = 0.0

#now the most important part, formula to calculate mortgage EMI is as follows
# D = (1+i) ** n - 1/i *((1+i) ** n)
#where D is a discount factor
# to get montly repayment amount just divide principal amount with D
# M = principal amount / D

monthly_interest_rate = round(interest * .01/12,5)
argument = 1+monthly_interest_rate

D = round(((argument**no_of_month-1)/(monthly_interest_rate * (argument ** no_of_month))),2)

monthly_mortgage = round(principal_amt/D,2)
total_amount_payable = monthly_mortgage * 24 
interest_amount = round(total_amount_payable - principal_amt,2)

print(f'Your monthly mortgage will come upto: {monthly_mortgage}')
print(f'Total amount payable: {total_amount_payable}')
print(f'Total interest amount: {interest_amount}')