from FurniturePlanner import *

Prod = Production ('TODAY')
Projects = []



Corpus.showComponents(Corpus(2070,450,500,'down','shelfs',False,False),True)

GenerteLabels(Corpus(2070,450,500,'down','shelfs',False,False).plates,"output/labels.pdf")