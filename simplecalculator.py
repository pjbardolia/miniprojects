def enter_no(statement):
    while True:
        try:
            return int(input(statement))
        except ValueError:
            print('Kindly enter an integer')

def cal(operation,num1,num2):
    if operation not in '+-/*':
        print('Kindly provide either of + - / *')
    else:
        if operation == '+':
            print(num1 + num2)
        elif operation == '-':
            print(num1 - num2)
        elif operation == '*':
            print(num1 * num2)
        elif operation == '/':
            try:
                print(num1/num2)
            except ZeroDivisionError:
                print('Division by zero is not possible')

def main():
    op = input(
        'What kind of operation would you like to do?\
        \nChoose between " +, -, *, / " : ')
        
    print(f'You have selected : {op}')
    no1 = enter_no('Enter number1 : ')
    no2 = enter_no('Enter number2 : ')
    cal(op,no1,no2)
    
if __name__ == '__main__':
    main()