from collections import Counter
import copy

class glob:
    FplatT = 18
    BplatT = 3

class Plate:

    def __init__(self,height,width,thickness, type, name=''):
        self.height = height
        self.width = width
        self.thickness = thickness
        self.area = self.height * self.width
        self.name = name
        self.type = type
        self.material = ''
        self.Sid = '' 
        self.id = str(self.height)+'x'+str(self.width)+'x'+str(self.thickness)+'_'+str(self.type)
        self.Sdim= ''
        if self.height >= self.width:
            self.Sid = self.id
            self.Sdim=str(self.height)+'x'+str(self.width)+'x'+str(self.thickness)
        else:
            self.Sid = str(self.width)+'x'+str(self.height)+'x'+str(self.thickness)+'_'+str(self.type)
            self.Sdim = str(self.width)+'x'+str(self.height)+'x'+str(self.thickness)
    
    def PrintPlate(self):
        print (self.name, self.thickness, "mm  : ", self.height, "mm x ", self.width, "mm")

    #def change id because of type
        

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

        self.Back = Plate(h-2*self.BackOffset,w-2*self.BackOffset,glob.BplatT,'back')
        self.Back.name = 'Plecy'
        self.plates.append(self.Back)

        self.Lwall = Plate (h,d,glob.FplatT,'wall')
        self.Lwall.name = 'Sciana lewa'
        self.plates.append (self.Lwall)
        self.Rwall = Plate (h,d,glob.FplatT,'wall')
        self.Rwall.name = 'Sciana prawa'
        self.plates.append (self.Rwall)

        self.Bwall = Plate (w-2*glob.FplatT,d,glob.FplatT,'wreath')
        self.Bwall.name = 'Wieniec dolny'
        self.plates.append (self.Bwall)

        if FullTopWall:
            self.Twall = Plate (w-2*glob.FplatT,d,glob.FplatT,'wreath')
            self.Twall.name = 'Wieniec gorny'
            self.plates.append (self.Twall)
        else:
            self.Twall1 = Plate (w-2*glob.FplatT,100,glob.FplatT,'wreath')
            self.Twall1.name = 'Wieniec gorny 1'
            self.plates.append (self.Twall1)
            self.Twall2 = Plate (w-2*glob.FplatT,100,glob.FplatT,'wreath')
            self.Twall2.name = 'Wieniec gorny 2'
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
                self.plates.append (self.Cback)
                self.Cwall = Plate (h,d,glob.FplatT,'wall')
                self.Cwall.name = 'Sciana narozna'
                self.plates.append (self.Cwall)
                self.CBwall = Plate (w-d-glob.FplatT,d,glob.FplatT,'wreath')
                self.CBwall.name = 'Wieniec narozny dolny'
                self.plates.append (self.CBwall)
                self.CTwall = Plate (w-d-glob.FplatT,d,glob.FplatT,'wreath')
                self.CTwall.name = 'Wieniec narozny gorny'
                self.plates.append (self.CTwall)
                self.accesories.append ("2 x wieszak")

        #function section 
        functions = ['drawers','kitchenware', 'shelfs']

        if Function in functions:

            if Function == 'shelfs':
                numberOfShelfs = int(h/300)
                for i in range(numberOfShelfs):
                    self.plates.append (Plate (w-2*glob.FplatT-0.1,d-glob.FplatT,glob.FplatT,'shelf','polka'))


        else:

            print ("no such function as",Function)





    def showComponents(self, accesories:bool):
        totalArea = 0
        info =''
        if self.isCorner: info = info + 'narozny'
        if not self.FullTopWall: info = info + ', niepelny wieniec gorny'
        print ("Korpus (",self.DownMiddleUp,") - ", self.height,'mm',' x ', self.width,'mm',' x ', self.depth,'mm [',info,']')
        for plate in self.plates:
            print (plate.name,': ',plate.height,'mm',' x ', plate.width,'mm')
            if plate.thickness == glob.FplatT: totalArea=totalArea+plate.area
        
        totalArea = totalArea * 0.000001
        print ('\nMaterial uzyty: ',round(totalArea,2), '㎡')

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
