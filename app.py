from FurniturePlanner import *
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

#GenerateStock / CheckStock / applicable Stock items form STORE to PACK state

#GenerteLabels(Prod.plates,"output/labels.pdf")

Prod.OperationsProgress (prt = True)

# start server to enable changes (rest of production)
code2find = '?'
True #stab fo breakpoint to inject code from scanner
plateFound= FindPlate (Prod.plates,code2find).pop()

print (plateFound.PerformOperation('PAINT', 'datetime'))

Prod.OperationsProgress (prt = True)

print("--- %s seconds ---" % round((time.time() - start_time),0),str(len(Prod.plates))+" plates")
