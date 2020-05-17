def characteristics_message(argument):
    switcher = { 
        1: "1: Success", 
        11: "11: Solid Success", 
        111: "111: Discoverer, Loves to Invent new things",
        1111: "1111: Research, Ruled by Sun",
        2: "2: Lethargic and moody",
        22: "22: Loves to stay alone",
        3: "3: Lucky active good in communication",
        333: "333: Imaginative and creative",
        4: "4: Organized systametic and practical",
        44: "44: Over-Practical",
        444:"444: Very disicplined",
        5: "5: Emotionally Balanced and Strong",
        55: "55: Strong Will Power, Young by heart and romantic",
        555: "555: Over romantic and have high expectations from people",
        6: "6: Love home & Famiy, Good relations, good relation with parents & children, good at giving and making a decision & social",
        66: "66: Hurdles with children, Talented, too much possessive, media and success",
        666: "666: Helpful, Negative thoughts for children, always worried and a great artist",
        7: "7: Emotional setback in relation, no trust and weak relationship",
        77: "77: Easily trust people and disappointment in love, disturbed married life, spiritualism, after 45-50 becomes very religious, good astrologer, healing profession like doctor",
        777: "777: Multiple setack, research oriented, love his own way, good numerologist",
        8: "8: Discipline, organized, systematic, stubborn, think big, trust own self, believe in work struggle, hardwork",
        88: "88: Intense, slow success, too much discipline, can do anything, achieves goals, delay in success",
        888: "888: Exaggerate situations, extreme struggle",
        9: "9: Towards humanity, caring, social care and sharp brains",
        99: "99: Sharp brains, superiority complex, criticize people, egoistic",
        999: "999: Loose opportunities, ups and downs in relationship, takes unneccessary risks, adventurous, very helpful and caring",
        438: "438: Politician and powerful man",
        276: "276: Quick thinker, sportsman, someone who takes risks",
        492: "492: Engineer, god gifted prodigy",
        357: "357: Emotional, Good Education and successful",
        816: "816: Practical, more detail work, success",
        258: "258: Real estate yog",
        456: "456: Amrit yog",
        48: "48: Works in law sector",
    } 
    return switcher.get(argument,f"{argument}: Sorry we do not have anything related to this number")

class PrintMessage:
    def __init__(self,theBoard):
        self.theBoard = theBoard
        self.listOfGhar = [0,4,3,8,2,7,6,4,9,2,3,5,7,8,1,6,2,5,8,4,5,6]
        
    def displayResult(self):
        
        for item in self.theBoard:
            if item == ' ':
                pass
            else:        
                print(characteristics_message(int(item)))
        
        i = 1
        #slicing the list from 1 to 3, 3 to 6 interval
        while i < len(self.listOfGhar):
            finalList = self.listOfGhar[i:i+3]
            
            #concatinating the three elements of a list in order to send message to function characteristics
            message = ''.join(str(v) for v in finalList)
            #checking each of the ghar in the self.listOfGhar and checking if they are empty or not
            
            if not [x for x in (self.theBoard[finalList[0]],self.theBoard[finalList[1]],self.theBoard[finalList[2]]) if x is " "]:
                print(characteristics_message(int(message)))
            else:
                pass
        
            i = i + 3
        