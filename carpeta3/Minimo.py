input("Programa para saber el numero menor ")
num1=int(input("Dijite un numero: "))
num2=int(input("Dijite un numero: "))
num3=int(input("Dijite un numero: "))

if num1 < num2 and num3:
     print(f'El numero menor es: {num1}')
elif num2 < num1 and num3:
     print(f'El numero menor es: {num2}')
elif num3 < num1 and num2:
     print(f'El numero menor es: {num3}')