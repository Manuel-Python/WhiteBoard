# Find the maximum total from top to bottom in triangle.txt,
# a 15K text file containing a triangle with one-hundred rows.

f = open("p067_triangle.txt", "r") # file comes from PE problem 67
a = f.read()
f.close()

b = a.split('\n')
first_term = int(b[0])


for i in range(1,len(b)-1):
    b[i] = b[i].strip("0").split(' ')
    b[i] = [int(x) for x in b[i]]

b.pop() #clean up last entry
b[0] = [first_term]


for i in range(len(b)-2,-1,-1):
    for j in range(len(b[i])):
        b[i][j] = b[i][j] + max(b[i+1][j], b[i+1][j+1])
    b.pop()

print( 'Max path found is {}'.format(b[0][0]))
