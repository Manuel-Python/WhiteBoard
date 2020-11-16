string = "Python is interesting."

# string with encoding 'utf-8'
arr1 = bytearray(string, 'utf-8')
print(arr1)

size = 100

arr = bytearray(size)
print(arr)

arr.append(78)

for b in arr:
    print(b)