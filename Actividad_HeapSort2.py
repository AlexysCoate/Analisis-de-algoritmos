import random

#Generates an unordered random array of size 'size' and values form 1 to 'max'
def genRandArr(size, max):
    arr = []
    for i in range(size):
        arr.append(random.randint(1, max))
    return arr

def maxHeapify(arr, heapSize, i):
    largest = i     #Se define a la raiz como el mayor elemento
    l = 2 * i + 1   #Elemento de la rama izquierda
    r = 2 * i + 2   #Elemento de la rama derecha

    #Si el elemento inicial es más pequeño que la rama izquierda
    if l < heapSize and arr[largest] < arr[l]:
        largest = l
    #Si el elemento inicial es más pequeño que la rama derecha
    if r < heapSize and arr[largest] < arr[r]:
        largest = r
    #Si el la raiz no es la más larga, entonces cambiar con el mayor
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        maxHeapify(arr, heapSize, largest)

def buildMaxHeap(arr):
    heapSize = len(arr)
    for i in range(heapSize//2-1,-1,-1):
        maxHeapify(arr,heapSize,i)

def heapSort(arr):
    heapSize = len(arr)
    buildMaxHeap(arr)

    for i in range(heapSize - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Exchange
        maxHeapify(arr, i, 0)

arr = genRandArr(10,20)
print(arr)
heapSort(arr)
print(arr)