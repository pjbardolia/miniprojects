def temp_converter(option):
    
    if option == 1:
        degreeCelcius = float(input('Enter the value in degree celcius : '))
        degreeFarheniet = degreeCelcius * 1.8 + 32
        print(f'The value of {degreeCelcius}C is converted to {degreeFarheniet}F')
    
    elif option == 2:
        degreeFarheniet = float(input('Enter the value in farhaneit : '))
        degreeCelcius = (degreeFarheniet - 32)/1.8 
        print(f'The value of {degreeFarheniet}F is converted to {degreeCelcius}C')
    
    elif option == 3:
        celcius = float(input('Enter the value of degree celcius : '))
        kelvin = celcius + 273.15
        print(f'The value of {celcius}C is converted to {kelvin}K')
    
    elif option == 4:
        kelvin = float(input('Enter the value of kelvin : '))
        degree = kelvin - 273.15
        print(f'The valueof {kelvin}K is Converted to {degree}C')
    
    elif option == 5:
        kelvin = float(input('Enter the value of kelvin : '))
        farheniet = (kelvin * 1.8) - 459.6
        print(f'The value of {kelvin}K is converted to {farheniet}F')
    
    elif option == 6:
        farheniet = float(input('Enter the value of farheniet : '))
        kelvin = (farheniet + 459.67)* 0.55
        print(f'The value of {farheniet}F is converted to {kelvin}K')

def get_input(question):
    while True:
        try:
            return int(input(question))
        except ValueError:
            print('Kindly enter an integer')


def print_options():
    print('1. To convert from degree celcius to farhaneit ')
    print('2. To convert from farhaneit to degree celcius')
    print('3. To convert from degree celcius to kelvin')
    print('4. To convert from kelvin to degree celcius')
    print('5. To convert from kelvin to farhaneit')
    print('6. To convert from farhaneit to kelvin')