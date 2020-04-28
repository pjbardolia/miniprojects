def cal_kg_to_pound(q):
    kgs = int(input(q))
    pound = round(kgs * 2.205,2)
    return (kgs,pound)

def cal_pound_to_kgs(q):
    pound = int(input(q))
    kgs = round(pound / 2.205,2)
    return (pound,kgs)

def check_validation(get_input):
    try:
        if get_input == 1:
            return 'Enter Kg to convert it to pound'
        else:
            return 'Enter Pound to be converted to kgs'
    except ValueError: 
        print('Kindly enter a number')

def mass_options():#wrapper function
    get_input = int(input('Select 1 for kg to pound, select 2 for pound to kg'))
    
    question = check_validation(get_input)
    
    if get_input == 1:
        kg_value,final_value = cal_kg_to_pound(question)
        print(f'{kg_value} kgs = {final_value} pound')
    else:
        pound_value,final_value = cal_pound_to_kgs(question)
        print(f'{pound_value} pound = {final_value} kgs')