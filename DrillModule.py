from FurniturePlanner import Corpus, Plate
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import pylab
from collections import defaultdict

class Hole:

    def __init__(self,x,y,s) -> None:
        self.x = x
        self.y = y
        self.s = s
        self.through = False
        self.covered = False

def PlanDrilling (plate:Plate):
    H = plate.height
    W = plate.width

    if plate.type=='wall_shelfs':

        offset = 100 #up and down offset
        Voffset = 35
        spacing = 32
        plate.numOfHoles = 1+2*int((0.5*H-offset)/spacing)
        n=plate.numOfHoles
        t=(H-(n-1)*spacing-2*offset)/2

        for h in range(n):
            plate.holes.append (Hole(Voffset,offset+t+h*spacing,6))
            plate.holes.append (Hole(W-Voffset,offset+t+h*spacing,4))

        plate.holesCoordinates=Holes2Coord(plate.holes)
        
        

    elif plate.type=='wall_drawers':
        drawerOffset = 30
        heightSum = 0
        drawers = plate.DrawerHeights
        drawers.reverse()
        for drawer in drawers:
            plate.holes.append(Hole(37,(heightSum+drawerOffset),6))
            plate.holes.append(Hole(37+160,heightSum+drawerOffset,6))
            plate.holes.append(Hole(37+256,heightSum+drawerOffset,6))
            heightSum+=drawer




def Drill (plate:Plate):

    if plate.toDrill:
            
            plate.isDrilled = True

    else:
        print ("No drill operation on object")
        return 

def ShowPlate (plate:Plate):
        #RECTANGLE
        fig = pylab.gcf()
        fig.canvas.manager.set_window_title(plate.name)
        plt.axes().add_patch(
            patches.Rectangle(
                (0, 0),   # (x,y)
                plate.width,          # width
                plate.height,          # height
                facecolor="None",
                edgecolor="black",
                alpha=1
            )
        )
        plt.text(0.5*plate.width,plate.height+50,plate.width,fontsize=9, horizontalalignment='center', verticalalignment='center')
        plt.text(plate.width+50,0.5*plate.height,plate.height,fontsize=9, rotation=90, horizontalalignment='center', verticalalignment='center',)
        #TAPING
        LW=3
        #left
        if plate.edgesTaped[0]:plt.vlines(x=0, ymin=0, ymax=plate.height, color="black", linewidth=LW)
        #right
        if plate.edgesTaped[2]:plt.vlines(x=plate.width, ymin=0, ymax=plate.height, color="black", linewidth=LW)
        #up
        if plate.edgesTaped[1]:plt.hlines(plate.height,xmin=0,xmax=plate.width, color="black", linewidth=LW)
        #down
        if plate.edgesTaped[3]:plt.hlines(0,xmin=0,xmax=plate.width, color="black", linewidth=LW)

        #HOLES
        holes = plate.holes
        X=list(h.x for h in holes)
        Y=list(h.y for h in holes)
        S=list(h.s for h in holes)
        plt.scatter(X, Y, S, facecolors='none', edgecolors='black')
        plt.gca().set_aspect('equal', adjustable='box')

        plt.autoscale(tight=None)
        plt.show()

def FindHole (ListOfholes:list,x,y):
    found = [h for h in ListOfholes if h.x == x and h.y==y]
    if found: return found.pop()
    else: return False

def GroupHolesPattern (plate:Plate):

    gridSize = 32

    groups = {'X': [], 'Y':[]}
    if plate.holes:
        groupX = defaultdict(list)
        groupY = defaultdict(list)
        for h in plate.holes:

                
            X1= h.x
            X2=h.x
            Y=h.y
            while (X1 <= plate.width and X1 >= 0) and (X2 <= plate.width and X2 >= 0):
                X1 += gridSize
                X2 -= gridSize
                FoundHole=FindHole (plate.holes, X1,Y)
                if FoundHole and not FoundHole.covered:
                    FoundHole.covered = True
                    groupX[FoundHole.y].append((FoundHole.x,FoundHole.y))
                FoundHole=FindHole (plate.holes, X2,Y)
                if FoundHole and not FoundHole.covered:
                    FoundHole.covered = True
                    groupX[FoundHole.y].append((FoundHole.x,FoundHole.y))
                
                
            X= h.x
            Y1=h.y
            Y2=h.y
            while (Y1 <= plate.height and Y1 >= 0) and (Y2 <= plate.height and Y2 >= 0):
                Y1 += gridSize
                Y2 -= gridSize
                FoundHole=FindHole (plate.holes, X,Y1)
                if FoundHole and not FoundHole.covered:
                    FoundHole.covered = True
                    groupY[FoundHole.x].append((FoundHole.x,FoundHole.y))
                FoundHole=FindHole (plate.holes, X,Y2)
                if FoundHole and not FoundHole.covered:
                    FoundHole.covered = True
                    groupY[FoundHole.x].append((FoundHole.x,FoundHole.y))

        #handle uncovered & out of pattern
        for h in plate.holes:
            if not h.covered:
                for k,v in groupX.items():
                    if k == h.y and (v[0][0]-h.x)%gridSize ==0:
                        groupX[k].append((h.x,h.y))
                        h.covered = True
                    else:
                        groupX[k].append((h.x,h.y))
                        h.covered = True

                for k,v in groupX.items():
                    if k == h.x and (v[0][1]-h.y)%gridSize ==0:
                        groupY[k].append((h.x,h.y))
                        h.covered = True
                    else:
                        groupY[k].append((h.x,h.y))
                        h.covered = True

        groups['X']= dict(groupX)
        groups['Y']= dict(groupY)
        plate.grouppedHoles = groups
        
    else:
        print ("No holes planned")

def Holes2Coord(ListOfholes:list):
    coord=[]
    for h in ListOfholes:
        coord.append((h.x,h.y))

    return coord


class MultiSpindleDrillingMachnie:

    def __init__(self,plate:Plate):
        matrix = plate.holes