numero=[]
for x in range (20):
    valor=int(input('ingrese un numero: '))
    numero.append(valor)
    if numero [x]<0:
        numero[x]=int(input('ingrese un nuero positivo: '))
print(numero)