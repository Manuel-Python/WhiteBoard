names = []

def processNames():
    scores = 0
    index = 1
    for name in names:
        a = nameval(name)
        sc = index * a
        scores += sc
        index += 1

    return scores

def nameval(name):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tot = 0
    for char in name:
        num = (alpha.find(char)) + 1
        tot += num

    return tot



def loadNames():
    f = open("p022_names.txt", "r") # file comes from PE problem 22
    a = f.read()
    f.close()
    b = a.split(',')

    for val in b:
        names.append(val)

    names.sort()
    print("Name count is {}".format(len(names)))

loadNames()
a = processNames()
print("Total namescores = {}".format(a))
#print(nameval("COLIN")) #71346322 689761523 871198282