from functions.TempFunctions import print_options, get_input, temp_converter
from functions.VolumeFunctions import cal_volume

def main():#wrapper function
    conversion_option = int(input('What type of unit conversion you want\n 1. Temperature \n 2. Volume \n 3. Mass '))
    if conversion_option == 1:
        options = print_options
        options()
        
        selected_option = get_input('Kindly enter your option :')
        converter = temp_converter
        converter(selected_option)
    elif conversion_option == 2:
        radius = int(input('Enter radius : '))
        height = int(input('Enter height : '))
    
        volume = cal_volume(radius,height)
        print(round(volume,2))
        
    else:
        print('Mass')
    #this is for temperature
        

if __name__ == '__main__':
    main()

