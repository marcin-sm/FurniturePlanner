from FurniturePlanner import *
from DrillModule import MultiSpindleDrillingMachnie
import time
start_time = time.time()


Prod = Production ('TODAY')
Proj = Project ('KUCHNIA')

Proj2 = Project ('SZAFA')


Proj.Add(Corpus(2070,450,510,'down','shelfs',False,False))
Proj.Add(Corpus(720,600,350,'up','shelfs',False,True))
Proj.Add(Corpus(720,600,350,'up','shelfs',False,True))
Proj.Add(Corpus(720,1200,510,'down','shelfs',False,False))
Proj.Add(Plate(100,3000,18,'blend','cokol'))
Proj2.Add(Corpus(720,1200,1110,'down','shelfs',True,False))
Proj2.Add(Corpus(1600,600,350,'up','shelfs',False,True))
Proj2.Add(Corpus(1600,600,350,'up','shelfs',False,True))

Prod.Add(Proj)
Prod.Add(Proj2)

for p in Prod.plates[:4]:
    MultiSpindleDrillingMachnie(p)

#MultiSpindleDrillingMachnie(Plate(100,3000,18,'blend','cokol'))


print("--- %s seconds ---" % round((time.time() - start_time),0),str(len(Prod.plates))+" plates")
