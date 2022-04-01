compra = int (input("total de la compra "))
balota = input("escoja el color de la balota: roja, verde, blanca, amarilla y negra ")

des_verde = 0.5 * compra 
des_blanca = 0.3 * compra   
des_amarilla = 0.1 * compra 
des_negra= 0.2 * compra 

balotaverde_des1 = compra - ( 0.5 * compra ) 
balotablanca_des1 = compra - ( 0.3 * compra ) 
balotaamarilla_des1 = compra - ( 0.1 * compra ) 
balotanegra_des1 = compra - ( 0.2 * compra ) 

if compra >= 50000:
    if balota== ("roja"):
        print (f'valor del descuento: {compra} ,valor a pagar con descuento aplicado 0 ')
    elif balota == ("verde"):
        print (f'valor del descuento: {des_verde} ,valor a pagar con descuento aplicado {balotaverde_des1} ')
    elif balota == ("blanca"):
        print (f'valor del descuento: {des_blanca} ,valor a pagar con descuento aplicado {balotablanca_des1} ')
    elif balota == ("amarilla"):
        print (f'valor del descuento: {des_amarilla} ,valor a pagar con descuento aplicado {balotaamarilla_des1} ')
    elif balota == ("negra"):
        print (f'valor del descuento: {des_negra} ,valor a pagar con descuento aplicado {balotanegra_des1} ')
else: 
    print ("compra menor a 50000 no hay descuento ")