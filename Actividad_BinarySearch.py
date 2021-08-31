import random
import math

#Generates an ordered random array of size 'size' and values form 1 to 'max'
def genRandArr(size, max):
    arr = []
    for i in range(size):
        arr.append(random.randint(1, max))
    arr.sort()
    return arr

# Realiza un BinarySearch y devuelve la posición del elemento a buscar
# En caso de que haya 2 o más elementos devuelve la primera coincidencia
def binarySearch(arr,k):
    r = len(arr)-1
    l = 0
    while l <= r:
        m = math.floor((l+r)/2)
        if k == arr[m]:
            return m
        elif k < arr[m]:
            r = m-1
        else:
            l = m+1
    return -1

arr = genRandArr(10,15)
print(arr)
pos = binarySearch(arr,15)
print('Posición =',pos)