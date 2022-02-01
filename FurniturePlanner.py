from collections import Counter
import copy
import random


class glob:
    FplatT = 18
    BplatT = 3
    Dfornir = 'RAL9001'
    Operations = ['CUT', 'TAPE', 'DRILL', 'PAINT', 'STORE', 'PACK']

class Plate:

    def __init__(self,height,width,thickness, type, name=''):
        self.height = height
        self.width = width
        self.thickness = thickness
        self.area = self.height * self.width
        self.name = name
        self.type = type
        self.material = ''
        self.covering = glob.Dfornir
        self.edgesTaped = [0,0,0,0]
        self.toDrill = False
        self.isDrilled = False
        self.numOfHoles = 0
        self.code = ''
        self.Sid = '' 
        self.id = str(self.height)+'x'+str(self.width)+'x'+str(self.thickness)+'_'+str(self.type)
        self.Sdim= ''
        if self.height >= self.width:
            self.Sid = self.id
            self.Sdim=str(self.height)+'x'+str(self.width)+'x'+str(self.thickness)
        else:
            self.Sid = str(self.width)+'x'+str(self.height)+'x'+str(self.thickness)+'_'+str(self.type)
            self.Sdim = str(self.width)+'x'+str(self.height)+'x'+str(self.thickness)
    
    def TapeSum(self):
        return sum(self.edgesTaped)
    

    def PrintPlate(self):
        print (self.name, self.thickness, "mm  : ", self.height, "mm x ", self.width, "mm")
        

class Accesory:
    True

class Corpus:

    BackOffset = 5
    FrontOffset = 2

    def __init__(self,h,w,d, DownMiddleUp, Function,  isCorner: bool, FullTopWall: bool,NumOrKitchenware=''):
        self.plates =[]
        self.accesories = []
        self.height = h
        self.width = w
        self.depth = d
        self.DownMiddleUp = DownMiddleUp
        self.Function = Function
        self.NumOrKitchenware = NumOrKitchenware
        self.isCorner = isCorner
        self.FullTopWall = FullTopWall
        #Plate.edges = [height,width,height,width]
        self.Back = Plate(h-2*self.BackOffset,w-2*self.BackOffset,glob.BplatT,'back')
        self.Back.name = 'Plecy'
        self.plates.append(self.Back)

        self.Lwall = Plate (h,d,glob.FplatT,'wall')
        self.Lwall.name = 'Sciana lewa'
        self.Lwall.edgesTaped = [h,d,0,d]
        PlanDrilling (self.Lwall)
        self.plates.append (self.Lwall)
        self.Rwall = Plate (h,d,glob.FplatT,'wall')
        self.Rwall.name = 'Sciana prawa'
        self.Rwall.edgesTaped = [0,d,h,d]
        PlanDrilling (self.Rwall)
        self.plates.append (self.Rwall)

        self.Bwall = Plate (w-2*glob.FplatT,d,glob.FplatT,'wreath')
        self.Bwall.name = 'Wieniec dolny'
        self.Bwall.edgesTaped = [w-2*glob.FplatT,0,0,0]
        self.plates.append (self.Bwall)

        if FullTopWall:
            self.Twall = Plate (w-2*glob.FplatT,d,glob.FplatT,'wreath')
            self.Twall.name = 'Wieniec gorny'
            self.Twall.edgesTaped = [w-2*glob.FplatT,0,0,0]
            self.plates.append (self.Twall)
        else:
            self.Twall1 = Plate (w-2*glob.FplatT,100,glob.FplatT,'wreath')
            self.Twall1.name = 'Wieniec gorny 1'
            self.Twall1.edgesTaped = [w-2*glob.FplatT,0,w-2*glob.FplatT,0]
            self.plates.append (self.Twall1)
            self.Twall2 = Plate (w-2*glob.FplatT,100,glob.FplatT,'wreath')
            self.Twall2.name = 'Wieniec gorny 2'
            self.Twall2.edgesTaped = [w-2*glob.FplatT,0,w-2*glob.FplatT,0]
            self.plates.append (self.Twall2)

        self.Front = Plate(h-2*self.FrontOffset,w-2*self.FrontOffset,glob.FplatT, 'front')
        self.Front.name = 'Front'
        self.plates.append(self.Front) 

        if DownMiddleUp == "down":
            self.accesories.append ("4 x nogi")
            if isCorner:
                self.Cwall = Plate (h,d+5,glob.FplatT,'wall')
                self.Cwall.name = 'Sciana narozna'
                self.plates.append (self.Cwall)


        elif DownMiddleUp == "up":
            self.accesories.append ("2 x wieszak")
            if isCorner:
                self.Cback = Plate (h,w-d-glob.FplatT,glob.FplatT,'wall')
                self.Cback.name = 'Plecy narozne'
                self.Cback.edgesTaped = [0,w-d-glob.FplatT,0,w-d-glob.FplatT]
                #drill
                self.plates.append (self.Cback)
                self.Cwall = Plate (h,d,glob.FplatT,'wall')
                self.Cwall.name = 'Sciana narozna'
                self.Cwall.edgesTaped = [h,d,0,d]
                #drill
                self.plates.append (self.Cwall)
                self.CBwall = Plate (w-d-glob.FplatT,d,glob.FplatT,'wreath')
                self.CBwall.name = 'Wieniec narozny dolny'
                self.CBwall.edgesTaped = [w-d-glob.FplatT,0,0,0]
                self.plates.append (self.CBwall)
                self.CTwall = Plate (w-d-glob.FplatT,d,glob.FplatT,'wreath')
                self.CTwall.name = 'Wieniec narozny gorny'
                self.CTwall.edgesTaped = [w-d-glob.FplatT,0,0,0]
                self.plates.append (self.CTwall)
                self.accesories.append ("2 x wieszak")

        #function section 
        functions = ['drawers','kitchenware', 'shelfs']

        if Function in functions:

            if Function == 'shelfs':
                numberOfShelfs = int(h/300)
                for i in range(numberOfShelfs):
                    plat = Plate (w-2*glob.FplatT-1,d-glob.FplatT,glob.FplatT,'shelf','Polka')
                    plat.edgesTaped = [plat.height,0,0,0]
                    self.plates.append (plat)


        else:

            print ("no such function as",Function)





    def showComponents(self, accesories:bool):
        totalArea = 0
        totalTape = 0
        totalHoles = 0
        info =''
        if self.isCorner: info = info + 'narozny'
        if not self.FullTopWall: info = info + ', niepelny wieniec gorny'
        print ("Korpus (",self.DownMiddleUp,") - ", self.height,'mm',' x ', self.width,'mm',' x ', self.depth,'mm [',info,']')
        for plate in self.plates:
            details = str (plate.name) + ': '+str(plate.height)+'mm'+' x '+ str(plate.width)+'mm'
            if Plate.TapeSum(plate) != 0:
                details = details + ' | Okleina ' + str(Plate.TapeSum(plate)/1000) +'m: '+ str(plate.edgesTaped)
            if plate.numOfHoles != 0:
                details = details + ' | Otwory: '+ '2x'+str(plate.numOfHoles)
            #print (plate.name,': ',plate.height,'mm',' x ', plate.width,'mm', '| Okleina',Plate.TapeSum(plate)/1000,'m:', str(plate.edgesTaped), '| Otwory:', '2x'+str(plate.numOfHoles))
            print (details)
            if plate.thickness == glob.FplatT: 
                totalArea=totalArea+plate.area
                totalTape = totalTape+Plate.TapeSum(plate)/1000
                totalHoles = totalHoles + 2*plate.numOfHoles
        
        totalArea = totalArea * 0.000001
        print ('\nMaterial uzyty: ',round(totalArea,2), '㎡', "| Okleina:",round(totalTape,2), 'm', "| Calkowita liczba otworow:", totalHoles)

        if accesories:
            print("\nDodatkowe akcesoria: ", str(self.accesories))
        print("_____________________________")


class Project:    

    def __init__(self,ProjectName):
        self.Pname = ProjectName
        self.corpuses=[]
        self.plates = []

    def Add(self,item):

        if type(item) == Corpus:
            self.corpuses.append(item)
            self.plates = self.plates + item.plates
        elif type(item) == Plate:
            self.plates.append(item)

    def Aggregate(self):

        for cor in self.corpuses:
            #cor.showComponents(True)
            for plate in cor.plates:
                #plate.PrintPlate()
                plate.id = str(plate.height)+'x'+str(plate.width)+'x'+str(plate.thickness)+'_'+str(plate.type)
                if plate.height >= plate.width:
                    plate.Sid = plate.id
                else:
                    plate.Sid = str(plate.width)+'x'+str(plate.height)+'x'+str(plate.thickness)+'_'+str(plate.type)
                #print(id)
                self.plates.append(plate)

        c = Counter(plat.id for plat in self.plates)
        print (c.most_common())

    
class Production:

    def __init__(self,ProductionData):
        self.data = ProductionData
        self.projects = []
        self.corpuses=[]
        self.plates = []

    def Add(self,project:Project):
        self.projects.append(project)

    def Aggregate(self,ignoreRotate: bool):
        
        #lst = copy.deepcopy(self)
        lst = self
    
        for proj in lst.projects:
            lst.corpuses.extend(proj.corpuses)
            lst.plates.extend(proj.plates)


        if not ignoreRotate: c = Counter(plat.id for plat in lst.plates)
        else: c = Counter(plat.Sid for plat in lst.plates)
        print (c.most_common())


def RandomCode (length):
	start = 0   # inclusive
	end = 10	# exclusive

	x = random.choices(range(start, end), k=length)
	code = [str(int) for int in x]
	y = "".join(code)
	return y

def RandomBool():
    return bool(random.getrandbits(1))

def GenerteLabels (listOfPlates: list, path):
    records =[]
    for p in listOfPlates:
        records.append(CreateEntry(p.width,p.height,p.edgesTaped,RandomCode(10),RandomCode(20),p.name,RandomBool()))
    Generator (records,path)

from DrillModule import PlanDrilling
from LabelModule import CreateEntry, Generator