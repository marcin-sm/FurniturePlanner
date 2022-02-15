from collections import Counter
import copy
import random
from datetime import datetime


class glob:
    FplatT = 18
    FplatD = 650 #[kg/m3]
    BplatT = 3
    Dfornir = 'RAL9001'
    Operations = ['CUT', 'TAPE', 'DRILL', 'PAINT', 'STORE', 'PACK']
    Modes = ['OPERATION','VIEW']
    server_url="http://192.168.100.12:8001/?code="
    purposes = ['drawers','kitchenware', 'shelfs']

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
        self.mass = (glob.FplatD*self.area*self.thickness)/1000000000 #[kg]

        self.edgesTaped = [0,0,0,0]
        self.toDrill = False
        self.isDrilled = False
        self.numOfHoles = 0
        self.holes = []
        self.Operations = dict.fromkeys(glob.Operations)
        self.Operations ['CUT'] = 'TBD'
        self.Operations ['PACK'] = 'TBD'


        self.Project = ''
        self.code = RandomCode(10)
        self.qr = glob.server_url+self.code
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

    def PerformOperation (self, OperationName, info):
        message = ''
        info2 =''
        now = datetime.now()
        if info == 'datetime':
            info2 = now.strftime("%m/%d/%Y, %H:%M:%S")
        if OperationName in self.Operations:
            if self.Operations[OperationName] == 'TBD' :
                self.Operations[OperationName] = info2
                message = 'Operation '+ OperationName + ' performed succesfully'  

            elif self.Operations[OperationName] != 'TBD' and self.Operations[OperationName]:
                message = 'Operation '+ OperationName + ' has already been performed by '+ self.Operations[OperationName]

            else:
                message = 'Operation has not been planned for this plate'

        else:
            message = 'Unknown Operation'

        return message

        

class Accesory:
    True

class Corpus:

    BackOffset = 5
    FrontOffset = 2

    def __init__(self,h,w,d, DownMiddleUp, Purpose,  isCorner: bool, FullTopWall: bool,NumOrKitchenware=''):

        #====== CORPUS BASIC ELEMENTS ======
        self.plates =[]
        self.accesories = []
        self.Project = ''

        #====== CORPUS BASIC PARAMETERS ======
        self.height = h
        self.width = w
        self.depth = d
        self.DownMiddleUp = DownMiddleUp
        self.Purpose = Purpose
        self.NumOrKitchenware = NumOrKitchenware
        self.isCorner = isCorner
        self.FullTopWall = FullTopWall

        # ====== BACK ======
        self.Back = Plate(h-2*self.BackOffset,w-2*self.BackOffset,glob.BplatT,'back')
        self.Back.name = 'Plecy'
        self.Back.Operations.update(dict.fromkeys(['CUT', 'STORE', 'PACK'], 'TBD'))
        self.plates.append(self.Back)

        # ====== LEFT WALL ======
        self.Lwall = Plate (h,d,glob.FplatT,'wall')
        self.Lwall.name = 'Sciana lewa'
        self.Lwall.Operations.update(dict.fromkeys(['CUT', 'TAPE', 'DRILL', 'STORE', 'PACK'], 'TBD'))
        self.Lwall.edgesTaped = [h,d,0,d]
        self.Lwall.type+='_'+self.Purpose
        PlanDrilling (self.Lwall)
        self.plates.append (self.Lwall)

        # ====== RIGHT WALL ======
        self.Rwall = Plate (h,d,glob.FplatT,'wall')
        self.Rwall.name = 'Sciana prawa'
        self.Rwall.Operations.update(dict.fromkeys(['CUT', 'TAPE', 'DRILL', 'STORE', 'PACK'], 'TBD'))
        self.Rwall.edgesTaped = [0,d,h,d]
        self.Rwall.type+='_'+self.Purpose
        PlanDrilling (self.Rwall)
        self.plates.append (self.Rwall)


        # ====== BOTTOM WALL ======
        self.Bwall = Plate (w-2*glob.FplatT,d,glob.FplatT,'wreath')
        self.Bwall.name = 'Wieniec dolny'
        self.Bwall.Operations.update(dict.fromkeys(['CUT', 'TAPE', 'DRILL', 'STORE', 'PACK'], 'TBD'))
        self.Bwall.edgesTaped = [w-2*glob.FplatT,0,0,0]
        self.plates.append (self.Bwall)

        # ====== TOP WALL ======
        if FullTopWall:
            self.Twall = Plate (w-2*glob.FplatT,d,glob.FplatT,'wreath')
            self.Twall.name = 'Wieniec gorny'
            self.Twall.Operations.update(dict.fromkeys(['CUT', 'TAPE', 'DRILL', 'STORE', 'PACK'], 'TBD'))
            self.Twall.edgesTaped = [w-2*glob.FplatT,0,0,0]
            self.plates.append (self.Twall)
        else:
            self.Twall1 = Plate (w-2*glob.FplatT,100,glob.FplatT,'wreath')
            self.Twall1.name = 'Wieniec gorny 1'
            self.Twall1.Operations.update(dict.fromkeys(['CUT', 'TAPE', 'DRILL', 'STORE', 'PACK'], 'TBD'))
            self.Twall1.edgesTaped = [w-2*glob.FplatT,0,w-2*glob.FplatT,0]
            self.plates.append (self.Twall1)
            self.Twall2 = Plate (w-2*glob.FplatT,100,glob.FplatT,'wreath')
            self.Twall2.name = 'Wieniec gorny 2'
            self.Twall2.Operations.update(dict.fromkeys(['CUT', 'TAPE', 'DRILL', 'STORE', 'PACK'], 'TBD'))
            self.Twall2.edgesTaped = [w-2*glob.FplatT,0,w-2*glob.FplatT,0]
            self.plates.append (self.Twall2)

        # ====== FRONT ======
        self.Front = Plate(h-2*self.FrontOffset,w-2*self.FrontOffset,glob.FplatT, 'front')
        self.Front.name = 'Front'
        self.Front.Operations.update(dict.fromkeys(['CUT', 'DRILL', 'PAINT', 'STORE', 'PACK'], 'TBD'))
        self.plates.append(self.Front) 


        # ====== CORNER CORPUS CASE - ADDITIONAL PLATES ======
        if DownMiddleUp == "down":
            self.accesories.append ("4 x nogi")
            if isCorner:
                # ====== CORNER WALL - LOWER CORPUS ======
                self.Cwall = Plate (h,d+5,glob.FplatT,'wall')
                self.Cwall.name = 'Sciana narozna'
                self.Cwall.Operations.update(dict.fromkeys(['CUT', 'TAPE', 'DRILL', 'STORE', 'PACK'], 'TBD'))
                self.plates.append (self.Cwall)

        elif DownMiddleUp == "up":
            self.accesories.append ("2 x wieszak")
            if isCorner:
                # ====== CORNER BACK - UPPER CORPUS ======
                self.Cback = Plate (h,w-d-glob.FplatT,glob.FplatT,'wall')
                self.Cback.name = 'Plecy narozne'
                self.Cback.Operations.update(dict.fromkeys(['CUT', 'TAPE', 'DRILL', 'STORE', 'PACK'], 'TBD'))
                self.Cback.edgesTaped = [0,w-d-glob.FplatT,0,w-d-glob.FplatT]
                #drill
                self.plates.append (self.Cback)

                # ====== CORNER WALL - UPPER CORPUS ======
                self.Cwall = Plate (h,d,glob.FplatT,'wall')
                self.Cwall.name = 'Sciana narozna'
                self.Cwall.Operations.update(dict.fromkeys(['CUT', 'TAPE', 'DRILL', 'STORE', 'PACK'], 'TBD'))
                self.Cwall.edgesTaped = [h,d,0,d]
                #drill
                self.plates.append (self.Cwall)

                # ====== CORNER BOTTOM WALL - LOWER CORPUS ======
                self.CBwall = Plate (w-d-glob.FplatT,d,glob.FplatT,'wreath')
                self.CBwall.name = 'Wieniec narozny dolny'
                self.CBwall.Operations.update(dict.fromkeys(['CUT', 'TAPE', 'DRILL', 'STORE', 'PACK'], 'TBD'))
                self.CBwall.edgesTaped = [w-d-glob.FplatT,0,0,0]
                self.plates.append (self.CBwall)

                # ====== CORNER BOTTOM WALL - UPPER CORPUS ======
                self.CTwall = Plate (w-d-glob.FplatT,d,glob.FplatT,'wreath')
                self.CTwall.name = 'Wieniec narozny gorny'
                self.CTwall.Operations.update(dict.fromkeys(['CUT', 'TAPE', 'DRILL', 'STORE', 'PACK'], 'TBD'))
                self.CTwall.edgesTaped = [w-d-glob.FplatT,0,0,0]
                self.plates.append (self.CTwall)
                self.accesories.append ("2 x wieszak")

        # ====== SPECIAL PURPOSE ====== 
        
        if Purpose in glob.purposes:

            if Purpose == 'shelfs':
                numberOfShelfs = int(h/300)
                for i in range(numberOfShelfs):
                    plat = Plate (w-2*glob.FplatT-1,d-glob.FplatT,glob.FplatT,'shelf','Polka')
                    plat.Operations.update(dict.fromkeys(['CUT', 'TAPE', 'STORE', 'PACK'], 'TBD'))
                    plat.edgesTaped = [plat.height,0,0,0]
                    self.plates.append (plat)


        else:

            print ("no such Purpose as",Purpose)



    # ====== CORPUS SPECIFIC METHODS ======

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
            item.Project = self.Pname
            for p in item.plates:
                p.Project = self.Pname
            self.corpuses.append(item)
            self.plates = self.plates + item.plates

        elif type(item) == Plate:
            item.Project = self.Pname
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
        self.corpuses = self.corpuses + project.corpuses
        self.plates = self.plates + project.plates


    def Aggregate(self,ignoreRotate: bool):
        
        #lst = copy.deepcopy(self)
        lst = self
    
        for proj in lst.projects:
            lst.corpuses.extend(proj.corpuses)
            lst.plates.extend(proj.plates)


        if not ignoreRotate: c = Counter(plat.id for plat in lst.plates)
        else: c = Counter(plat.Sid for plat in lst.plates)
        print (c.most_common())

    def OperationsProgress (self, prt:bool):
       
        #ProgressDict = dict.fromkeys(glob.Operations,{'NOT DONE':0,'DONE':0})
        ProgressDict = dict((o,dict({'NOT DONE':0,'DONE':0})) for o in glob.Operations)
        for p in self.plates:
            for o in p.Operations:
                field = p.Operations[o]
                if p.Operations[o] == 'TBD':
                    ProgressDict[o]['NOT DONE'] +=1
                    #print (o,ProgressDict[o],ProgressDict[o]['NOT DONE'])
                elif p.Operations[o] != 'TBD' and p.Operations [o]:
                    ProgressDict [o]['DONE'] +=1
        
        if prt:
            for k in ProgressDict:
                D = ProgressDict [k]['DONE']
                ND = ProgressDict [k]['NOT DONE']
                print (k, ProgressDict[k], '| Progress:', round(D*100/(D+ND),0),'%')

        return ProgressDict



# ====== GENERIC METHODS ======

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
        records.append(CreateEntry(p.width,p.height,p.edgesTaped,p.code,p.qr,p.name,RandomBool()))
    Generator (records,path)

def FindPlate (ListOfplates:list,code):
    found = [x for x in ListOfplates if x.code == code]
    if found: return found.pop()
    else: return 'noplate'

from DrillModule import PlanDrilling
from LabelModule import CreateEntry, Generator