from FurniturePlanner import Plate
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import pylab
import numpy as np


class MultiSpindleDrillingMachnie:

    def __init__(self,plate:Plate):
        self.Type = plate.type
        self.H = plate.height
        self.W = plate.width
        print ("DRILLING", plate.name,"of type", self.Type,"and Dimensions",self.H,"x",self.W)

        fig = pylab.gcf()
        fig.canvas.manager.set_window_title(plate.name)
        plt.axes().add_patch(
            patches.Rectangle(
                (0, 0),   # (x,y)
                self.W,          # width
                self.H,          # height
                facecolor="None",
                edgecolor="black",
                alpha=1
            )
        )
        xpoints = np.array([200, 300])
        ypoints = np.array([30, 250])

        plt.plot(xpoints, ypoints, 'o')
        plt.gca().set_aspect('equal', adjustable='box')
        plt.autoscale()
        plt.show()



def PlanDrilling (plate:Plate):

    H = plate.height
    W = plate.width
    offset = 150 #up and down offset
    spacing = 32

    plate.numOfHoles = 1+2*int((0.5*H-offset)/spacing)


def Drill (plate:Plate):

    if plate.toDrill:
            
            plate.isDrilled = True

    else:
        print ("No drill operation on object")
        return 