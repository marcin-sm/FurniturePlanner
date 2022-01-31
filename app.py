from FurniturePlanner import *

Prod = Production ('TODAY')
Proj = Project ('KUCHNIA')


Proj.Add(Corpus(2070,450,510,'down','shelfs',False,False))
Proj.Add(Corpus(720,600,510,'up','shelfs',False,True))
Proj.Add(Corpus(720,600,510,'up','shelfs',False,True))
Proj.Add(Corpus(720,1200,510,'down','shelfs',False,False))

#Corpus.showComponents(Corpus(2070,450,500,'down','shelfs',False,False),True)

GenerteLabels(Proj.plates,"output/labels.pdf")