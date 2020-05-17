from functions.displayboard import display_board
from functions.birth import Birthdate
from functions.messageprint import PrintMessage


def main():#wrapper function
    while True:
        mylist = []
        digitbydigitList = []
        date_String = ''

        i=1

        birthdate = input('Enter birthdate in dd-mm-yyy format : ')
        day,month,year = birthdate.split('-')

        #a loop is run to append day, month and year to the string
        while i<=3:
            if i == 1:
                date_String += day
                i += 1
            elif i == 2:
                date_String += month
                i += 1
            else:
                date_String += year
                i += 1


        mylist.append(day)
        mylist.append(month)
        mylist.append(year)

        birth_date = Birthdate(day,month,year)
        sum_of_initial_date = birth_date.SumOfDates() #only initial date
        
        #sum of total date
        n = birth_date.TotalSumofDate(mylist)
        totalSumOfDate = str(sum([int(d) for d in str(n)]))
        
        board = birth_date.UpdateTestBoardList(sum_of_initial_date, totalSumOfDate, date_String)
        display_board(board)
        
        characteristics = PrintMessage(board)
        characteristics.displayResult()
        #print(message)
        
        yes_no = input('Do you wish to continue? press y or n : ')
        if yes_no.lower() == 'y':
            continue
        else:
            break

if __name__ == '__main__':
    main()