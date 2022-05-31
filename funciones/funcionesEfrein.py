#primer def

from audioop import reverse


def mostrarCadena(cadena):
    for i in lista:
        print(i)
        cadena+=str(i)+coma
    return cadena

#segundo def
def listaInversa(lista):
    lista.sort(reverse=True)
    lista2=lista
    return lista2
#tercer def

def menu(lista):
    menu = int(input("selecione \n 1. Para buscar en la lista \n 2. Para salir\n"))

    while menu> 2:
        print('digite un numero del 1 al 2 SOLAMENTE')
        menu = int(input("selecione \n 1. Para buscar en la lista \n 2. Para salir\n"))

    while menu == 1:
        contador=0
        letra = input("Introdusca la palabra a buscar en la lista: ")
        for i in lista:
            if i == letra:
                print('Esta dentro de la lista ')
            else:
                contador+=1
        if contador==10:
            print('no existe la palabra dentro de la lista')

        menu = int(input("selecione \n 1. Para buscar en la lista \n 2. Para salir\n"))

    if menu == 2:
        print('Dejaste de buscar nombres dentro de la lista')

# ultimo
def contar(lista):
    letra = input("Introdusca la palabra que este dentro de la lista para contar sus silabas: ")
    contador=0
    for i in lista:
        if i == letra:
            verdad=len(i)
            print(f'{verdad}')
        else:
            contador += 1
    if contador == 10:
        print(f'No se encuentra la palabra en la lista')

#base
lista=['efrein','isrrael','guedez','diaz','luisa','guzman','pedro','juan','benito','lopez']
cadena=""
coma=","

print("\n El programa mostrara en una variable la lista \n")

cadena =mostrarCadena(cadena)
print(f"{cadena}")

print("\n Se imprimira la lista en de manera desendente alfabeticamente \n")

lista2 =listaInversa(lista)
print(f"{lista2}")
# OJO al buscar en la lista queda ordenada de mayor a menor Z a A
print("\n El programa dira si ese nombre esta dentro de la lista \n")

menu(lista)

print("\n El programa contara las silabas \n")

contar(lista)

print("finalizo el programa")


 

