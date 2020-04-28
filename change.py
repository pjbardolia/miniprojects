whole_no = []    

def multiplier(d,q):
    if d == 25:
        whole_no.append(q * 25)
    elif d == 10:
        whole_no.append(q * 10)
    elif d == 5:
        whole_no.append(q * 5)
    elif d == 1:
        whole_no.append(q * 1)

def get_input(question):
    while True:
        try:
            return float(input(question))
        except:
            print('Please enter an integer')

def main(): #wrapper function
    denomination = [25,10,5,1]
    string = ['Quarters','Dimes','Nickles','Pennies']
    counts = []
    
    cost_of_item = get_input('Enter the cost of the item : ')
    money_given = get_input('Enter the money given by customer : ')
    
    tender_change = round(money_given - cost_of_item,2) #tender_change is the total change we have to give back to the customer
    print(tender_change)
 
    #I have splited the value of the change by converting it into a string and then spliting it with 'dot'
    splited_results = str(tender_change).split('.')
    #since results of a split are in form of list, we have to access list using index method and assigning value to parameter
    dollars = int(splited_results[0]) # value before decimal is dollar
    cents = int(splited_results[1]) # value after decimal is cents
    
    for d in denomination:
        quotient = cents//d
        counts.append(quotient) # this gives qutoient or no of quarters or dimes or nickles or penny
        cents = cents % d # this gives reminder or amount left after dividing using denomination
        multiplier(d,quotient)
        #################End of for loop
    
    for a,b,c in zip(counts, string, whole_no ):
        print(f'{a} {b}: {c} Cents')

if __name__ == '__main__':
    main()