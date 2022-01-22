from FurniturePlanner import Plate

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