#Taking meter input
class Meter_Input():
    
    def __init__(self):
        pass
    
    def meter_userInput(self):
        try:
            meterInput = int(input("Enter quality meter:"))
            return meterInput     
        except:
            print("You seem to have entered wrong value")

class Clr_Wght():
    
    def __init__(self):
        pass
    
    def clr_userInput(self):
            userInput = input("Enter color name and weight in following format:{color_name:weight,color_name:weight}:")
            return userInput


class Color_Calculation():
    
    def __init__(self,color_rate = [],weight = []):
        self.color_rate = color_rate
        self.weight = weight
        self.total_amount_based_on_weight_of_the_color = []
    
    def multiply(self):
        for x,y in zip(self.color_rate,self.weight):
            self.total_amount_based_on_weight_of_the_color.append(x * y)
        return sum(self.total_amount_based_on_weight_of_the_color)


class Final_Costing():
    
    database_list = []
    
    def __init(self,result):
        self.result = result
    
    def total(self):
        costing_amount = database_list[0] + self.result
        database_list[0] = costing_amount


class Replay():
    def __init__(self):
        pass
    
    def playing(self):
        choice = input("Want to check more costing? Y/N:").lower()
        return choice == 'yes'

class FetchColorRate():
    
    rate = {'brown3bs':397,'bluecb':1870,'bluedbr':577,'blue2rx':3353,'bluebg':3197,'bluegsl':1029,'brown3reln':294,
    		'blackrplus':598,'bluesr':957,'bluemgb':600,'bluebrsl':957,
    		'tblueigl':1903,'nblue3g':411,'orangerl':272,'redf3bs':1018,'redg':1127,'redvioletfbl':1186,'violet3r':752,
    		'violetcbg':961,'yellowm7g':430,'yellowbrown2rfl':276,'darkred2b':328,'gyellowgl':306,'magentac2r':1297,
    		'scarletrr':244,'pinkcy':1000,'pinkrbsf':636,'rubine5b':352,'yellow4gnl':339,'scarletgs':468,'greybrs':327,'nblues2g':548,'yellowcug':518,
    		'whiter':586,'blackemrd':452,'pink5bn':692,'red6b':686,'red2bn':1352,'yellow10gn':1352,'redbs':488,
    		'rbluegr':260,'blackg':376,'redsrs':522,'red3bn':505,'rodhamineb':1479,'violet5bn':217,'yellowgp':315,
    		'rodhaminebn':2968,'greenv':1166,'pblueas':860,'violet2r':1160,'rodhaminebnsf':3176,'orange2gp':272,'maroonv':388,
    		'nblues5r':652,'yellow2r':676,'redrg':958,'brownb':713,'yellow4gn':1167,'yellow2g':787,'greencp':303,
    		'bluegrxf':1932,'greenm':362,
    		'blacksuperior':1724,'yellow7gl':1462,'blue5g':1687,'yellowcgn':1068,
        	'yellow10gef':962,'redj':1446,'red4g':893,'yellowbrown2rc':276,'redvioletxf':1297,'red2b':1156
           }
    
    rate_list = []  
   
    def __init__(self): 
        new_color_split_data = []
    
    def FetchRate(self,colorName=[]):
        for x in colorName:
            if x in self.rate.keys():
                rate_amount = self.rate[x]
                self.rate_list.append(rate_amount)
            else:
                print("The color you seem to have entered does not seem to be with us in database")
                #new_color = input("Enter color name and rate:").lower()
                #new_color_split_data = new_color.split(':')
                #self.rate['new_color_split_data[0]'] = new_color_split_data[1]
                
        return self.rate_list


class SplitData():

    def __init__(self):    
        self.colorname = []
        self.color_quantity = []
    
    def MethodForSpliting(self,string_to_be_split):
        splitted_data = string_to_be_split.split(',')
        
        for x in splitted_data:
            sub_split = x.split(':')
            self.colorname.append(sub_split[0])
            self.color_quantity.append(float(sub_split[1]))
            
        return (self.colorname,self.color_quantity)


class Division():
    
    def __init__(self,meters,total_amount_of_color):
        self.meters = meters
        self.total_amount_of_color = total_amount_of_color
    
    def division_by_meters(self):
        self.resultant_costing = round(self.total_amount_of_color/self.meters,2)
        return self.resultant_costing



toRepeat = Replay()
while True:
    #creating instance for all three class
    meterInput = Meter_Input()
    clrWeight = Clr_Wght()
    fetchcolorrate = FetchColorRate()
    
    #taking user input for meters of cloth
    meters = meterInput.meter_userInput()
    
    #taking user input for name of the color and quantity of color that went into
    clr_weight = clrWeight.clr_userInput()
    
    #creating intance of the class which uses ways of spliting data and creating list of color name and quantity provided by user
    InstanceOfSplitClass = SplitData()
    
    #we are getting list of colorname and its quantity in form of a list  
    (colorname,color_quantity) = InstanceOfSplitClass.MethodForSpliting(clr_weight)
    
    #once we get list of colorname, its time to fetch rate of indvidual colors thereby using it to multiply with quantity
    rate_list = fetchcolorrate.FetchRate(colorname)
    
    colorCalculation = Color_Calculation(rate_list,color_quantity)
    
    total_amount_of_color = round(colorCalculation.multiply(),2)
    5
    divison = Division(meters,total_amount_of_color)
    
    print(divison.division_by_meters())
    
    rate_list.clear()
    
    replay = Replay()
    
    if replay.playing() == True:
        continue
    else:
        break