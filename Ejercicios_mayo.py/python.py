import math
lista=[1,2,3,4,5]
print ("lista sin modificar", lista )
for  i in range (0, len(lista)):
    lista[i]= (math.sqrt(lista[i]))

print("la raiz cuadrada de la lista es:", lista)
