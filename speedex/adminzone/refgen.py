import random#modeule generating random nos

def getref():
    refno='sp'
    for i in range(1,3):#here range(1,3) means for(i>=1;i<=3;i++)
        n=random.randrange(1,5)
        refno+=str(n)
        n=random.randrange(0,7)
        refno +=str(n)
        n = random.randrange(3,9)
        refno +=str(n)
    return refno