class Birthdate:
    def __init__(self,day=0,month=0,year=0):
        self.day = day
        self.month = month
        self.year = year
        self.digitbydigitList = []
        self.board = [' '] * 10
        self.checkList = ['#','1','2','3','4','5','6','7','8','9']
        
    def __str__(self):
        return '{0},{1},{2}'.format(self.day, self.month, self.year)
    
    def SumOfDates(self):
        sum_of_standalone_date = sum([int(d) for d in self.day])
        
        #checking number of digits after finding the sum of initial birthdate, there might be a case like 29. 
        #where total will be 11 which needs to be further divided list 1+1 = 2
        #hence checking for no of digits
        
        no_of_digits = len(str(abs(sum_of_standalone_date)))
        
        if no_of_digits == 1:
            string_of_birthdate = f'{self.day}-{self.month}-{self.year}'
            return str(sum_of_standalone_date)
        else:
            final_tally = str(sum([int(x) for x in str(sum_of_standalone_date)]))
            return final_tally
            
            
    def TotalSumofDate(self,dateList = []):
        for i in dateList:
            self.digitbydigitList.append(sum([int(j) for j in i]))
    
        sum_total_of_birth_date = sum(self.digitbydigitList)
        return sum_total_of_birth_date
    
    def UpdateTestBoardList(self,initialDate = '' ,totalSumDate = '', stringOfDate = ''):
        for j in stringOfDate:
            if j == '1':
                self.board[1] += '1'
            elif j == '2':
                self.board[2] += '2'
            elif j == '3':
                self.board[3] += '3'
            elif j == '4':
                self.board[4] += '4'
            elif j == '5':
                self.board[5] += '5'
            elif j == '6':
                self.board[6] += '6'
            elif j == '7':
                self.board[7] += '7'
            elif j == '8':
                self.board[8] += '8'
            elif j == '9':
                self.board[9] += '9'
        
        #finalBoard = updatingDateSum(self.board,initialDate,totalSumDate)
            
        if initialDate in self.checkList:
            index = self.checkList[int(initialDate)]
            self.board[int(index)] += initialDate
        
        if totalSumDate in self.checkList:
            index = self.checkList[int(totalSumDate)]
            self.board[int(index)] += totalSumDate
            
        return self.board          
        
