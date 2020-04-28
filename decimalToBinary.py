def get_input(question):
    while True:
        try:
            return int(input(question))
        except ValueError:
            print('Enter an Integer')

def generate_squares(no):
    square = 0
    mylist = []
    
    while True:
        mylist.append(2 ** square)
        square += 1
        if (2 ** square) > no:
            return mylist
            break
        else:
            continue

def methodToFindNos(no,newlist = []):
    nosUsedToachieveBinary = []
    for x in newlist:
        if no >= x:
            no = no - x
            nosUsedToachieveBinary.append(x)
        else:
            continue
    return nosUsedToachieveBinary

def main(): # wrapper function
    used_nos = [] #defining a list of numbers used to reach nearer to entered decimal
    BinaryNo = [] #defining a list to add binary number
    theNumber = get_input('Enter a decimal: ') #asking to enter a decimal using get_input method
    used_nos = generate_squares(theNumber) #calling a function to get list of square for number 2 nearer to decimal
    used_nos.sort(reverse = True) #sorting the list from higher to lower
    resultantList = methodToFindNos(theNumber,used_nos) #calling a function which is used to find binary no after subtraction
    
    if theNumber == sum(resultantList): 
        for item in used_nos:
            if item in resultantList:
                BinaryNo.append(1)
            else:
                BinaryNo.append(0)
    print(f'Binary equivalent of {theNumber} is : {BinaryNo}')

if __name__ == '__main__':
    main()