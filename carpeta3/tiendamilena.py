import random
valor_compra=int(input("Ingrese el monto de su compra: "))
balota =['roja', 'verde', 'blanca', 'verde', 'amarilla']

des_verde=valor_compra-(valor_compra*0.5)
des_blanca=valor_compra-(valor_compra*0.3)
des_negra=valor_compra-(valor_compra*0.2)
des_amarilla=valor_compra-(valor_compra*0.1)

des2_verde=valor_compra*0.5
des2_blanca=valor_compra*0.3
des2_negra=valor_compra*0.2
des2_amarilla=valor_compra*0.1

def selectRandom(balota):
    return random.choice(balota)
colorbalota=selectRandom(balota)
print(f'Su balota es: {colorbalota} ')


if valor_compra >= 50000:
    if colorbalota== ("roja"):
        print (f'valor del descuento: {valor_compra} ,valor a pagar con descuento aplicado 0 ')
    elif colorbalota == ("verde"):
        print (f'valor del descuento: {des2_verde} ,valor a pagar con descuento aplicado {des_verde} ')
    elif colorbalota == ("blanca"):
        print (f'valor del descuento: {des2_blanca} ,valor a pagar con descuento aplicado {des_blanca} ')
    elif colorbalota == ("amarilla"):
        print (f'valor del descuento: {des2_amarilla} ,valor a pagar con descuento aplicado {des_amarilla} ')
    elif colorbalota == ("negra"):
        print (f'valor del descuento: {des2_negra} ,valor a pagar con descuento aplicado {des_negra} ')
else: 
    print ("compra menor a 50000 no hay descuento ")

