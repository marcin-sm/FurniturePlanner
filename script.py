from FurniturePlanner import *

Prod = Production ('TODAY')
Projects = []

Kitchen = Project ('Kowalski')
Kitchen.Add(Corpus(960,600,505,'up',True,True))
Kitchen.Add(Corpus(870,450,300,'up',True,False))
Kitchen.Add(Corpus(2070,600,505,'down',True,False))
Kitchen.Add(Corpus(2070,600,505,'down',False,False))
Kitchen.Add(Corpus(2070,600,300,'up',True,False))

Kitchen.Aggregate()
Prod.Add(Kitchen)
print (len(Kitchen.plates))
print ("\n")

Warderobe = Project ('Nowak')
Warderobe.Add(Corpus(2070,1200,500,'down',True,False))
Warderobe.Add(Corpus(2070,1200,500,'down',True,False))
Warderobe.Add(Corpus(960,600,505,'down',True,False))
Warderobe.Add(Plate(505,564,18,'wreath'))
Warderobe.Add(Plate(505,564,18, 'wreath'))

Warderobe.Aggregate()
Prod.Add(Warderobe)
print (len(Warderobe.plates))

print ("\n")

#Prod.Aggregate(ignoreRotate=True)
Prod.Aggregate(ignoreRotate=True)

print (len(Prod.plates), ' but should be ', str(len(Kitchen.plates)+len(Warderobe.plates)))

Corpus.showComponents(Corpus(2070,1200,500,'down',True,True),True)