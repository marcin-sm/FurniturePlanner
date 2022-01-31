from FurniturePlanner import *

Prod = Production ('TODAY')
Projects = []



Corpus.showComponents(Corpus(720,600,500,'up','shelfs',True,True),True)

GenerteLabels(Corpus(720,600,500,'up','shelfs',True,True).plates,"output/labels.pdf")