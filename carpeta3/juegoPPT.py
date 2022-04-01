persona1 = input("¿Piedra, papel o tijera? ")
persona2 = input("¿Piedra, papel o tijera? ")

if persona1 == "piedra" and persona2== "papel":
    print(f"gana papel")
elif persona1 == "piedra" and persona2== "piedra":
        print(f"empate")
elif persona1 == "piedra" and persona2== "tijera":
        print(f"gana piedra")
        
        
elif persona1 == "papel" and persona2== "piedra":
        print(f"gana papel")
elif persona1 == "papel" and persona2== "papel":
        print(f"empate")  
elif persona1 == "papel" and persona2== "tijera":
        print(f"gana tijera") 


elif persona1 == "tijera" and persona2== "piedra":
        print(f"gana piedra")
elif persona1 == "tijera" and persona2== "tijera":
        print(f"empate")
elif persona1 == "tijera" and persona2== "papel":
        print(f"gana papel")
    
        
        
