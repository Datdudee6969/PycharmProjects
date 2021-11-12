
def readm1():
    file = open("hw2-m1.txt", "r")
    lines = file.readlines()
    a=[]
    for line in lines:
        b=[]
        for x in line.strip('\n').split(' '):
            b.append(int(x))
        a.append(b)                
    return a


def readm2():
    file = open("hw2-m2.txt", "r")
    lines = file.readlines()
    a=[]
    for line in lines:
        b=[]
        for x in line.strip('\n').split(' '):
            b.append(int(x))
        a.append(b)                
    return a


