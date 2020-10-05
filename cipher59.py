matrix = []
test = []


def countCharVal():
    sum = 0
    for val in test:
        sum += val
    print("Total sum of all decripted character values is {}".format(sum))

def testForEnglish():
    isEnglish = False
    times = 0 # number of 'the ' found in text  // 116 104 101 32

    for index in range(3,len(test)):
        if (test[index] == 32 and test[index-1] == 101 and test[index-2] == 104 and test[index-3] == 116):
            times += 1
    if times > 10:
        isEnglish = True
    else:
        isEnglish = False
    return isEnglish


def decript():
    key = [0,0,0]
    for a in range(97,123): #lower case ascii range
        for b in range(97,123):
            for c in range(97,123):
                test.clear()
                key[0] = a
                key[1] = b
                key[2] = c
                print("Key {} {} {}".format(a,b,c))
                index = 0
                for val in matrix:
                    cypher = key[index] ^ val
                    index += 1
                    if index > 2:
                        index = 0
                    test.append(cypher)
                if testForEnglish():
                    testArray()
                    countCharVal()
                    return


def loadMatrix():
    f = open("p059_cipher.txt", "r") # file comes from PE problem 59
    a = f.read()
    f.close()

    b = a.split(',')

    for val in b:
        matrix.append(int(val))

def testArray(): #print the test array ascii values
    for val in test:
        print(chr(val), end='')
    print("\n", end='\n')



loadMatrix()
decript()
