         
while True:
    n1 = int(input("Digite un numero por favor : "))
    if(n1 % 5 == 0 and n1 != 0):
       print("Numero Multiplo de 5")
    elif (n1 % 5 != 0):
        print("Este numero no es multiplo de 5")
    else:
        print("5")   
        break # Obliga a terminar el ciclo
print("El ciclo terminó al ingresar un número negativo")
      
    