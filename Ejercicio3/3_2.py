#importamos numpy para poder crear la matriz
import numpy as np
import random


# 3.2.1
lista=[]

while True:
    numero_aleatorio = random.randint(0,100)
    if numero_aleatorio%9 ==0:
        lista.append(numero_aleatorio)
        lista
    elif len(lista)==12:
        array = np.array(lista)
        print(array)
        print(type(array))
        array = array.reshape(3,4)
        print(array)
        break
    

#3.2.2
print(array[0][0])
print(array[0])
print(array.size)
print(list(array.shape)[0])


for i in range(list(array.shape)[0]):
    for j in range(list(array.shape)[1]):
        if(array[i][j]>0 and array[i][j]%5==0):
            pass
        else:
            array[i][j]=-1

print(array)