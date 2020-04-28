def get_input(question):
    return int(input(question))

def get_squares(digits):
    mylist = []
    i = 0

    while i < digits:
        mylist.append(2 ** i)
        i += 1

    return mylist


def main():
    binaryNoList = []
    FinalDecimal = []

    theNumber = get_input('Enter a binary number in either 1 or 0 : ')

    binaryNo = theNumber
    #count no of digits in binary
    count = 0

    while(theNumber > 0):
        theNumber = theNumber // 10
        count = count + 1
    '''
    End of counting digits
    '''    
    lengthOfBinary = count
    listOfSquares = get_squares(lengthOfBinary)
    #passing number of digits into a function called get_squares() so as to generate list of squares upto number of digits in the number
    
    #arranging list of square from highest to lowest 
    listOfSquares.sort(reverse=True)

    #now I am generating the list of digits out of binary number
    binaryNoList = [int(x) for x in str(binaryNo)]

    
    FinalDecimal = [num1*num2 for num1,num2 in zip(listOfSquares,binaryNoList)]


    Decimal = sum(FinalDecimal)
    print('Thus, Decimal is:')
    print(Decimal)


 #wrapper function


if __name__ == '__main__':
    main()