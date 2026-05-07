# EJERCICIO 1 - Ludo

# import random
# import time

# name=input("Ingrese su nombre: ")
# cont=0

# while cont <= 30:

#     dado=random.randint(1,6)
#     dado2=random.randint(1,6)

#     print(f"{name} sacó: {dado}")
    

#     print(f"{name} sacó: {dado2}")
    

#     print(f"{name} avanzó: {dado+dado2} casillas")

#     cont+=dado+dado2

# if cont==30:
#     print(f"Has ganado! has llegado a {cont}")

# elif cont>30:
#     print(f"Te has pasado! avanzaste en total {cont}")

# EJERCICIO 2 - Golf

# import random
# import time

# name=(input("Ingrese nombre: "))

# player=random.randint(60,190)
# j2=random.randint(60,190)
# j3=random.randint(60,190)

# print(f"{name} Lanzó {player}mts")
# time.sleep(1)
# print(f"Bot 2 Lanzó {j2}mts")
# time.sleep(1)
# print(f"Bot 3 Lanzó {j3}mts")
# time.sleep(1)

# if player >j2 and player >j3:
#     print(f"{name} Lanzó mas lejos")

# elif j2> j3:
#     print(f"Bot 2 Lanzó mas lejos") 

# else: 
#     print(f"Bot 3 Lanzó mas lejos")
   

# EJERCICIO 3 - Juego de pelea

# import random
# import time

# name=input("Ingrese el nombre del jugador 1: ")
# name2=input("Ingrese el nombre del jugador 2: ")

# vida=100
# vida2=100

# while vida or vida2 > 0:
#     combosp1=random.randint(7,18)
#     combosp2=random.randint(7,18)

#     print(f"{name} Hizo {combosp1} de daño!")
#     time.sleep(1)
#     vida2+=-combosp1
#     print(f"{name2} Tiene {vida2} de salud")
#     time.sleep(2)
#     if vida2<=0:
#         print(f"{name} Ganó!")
#         break

#     print(f"{name2} Hizo {combosp2} de daño!")
#     time.sleep(1)
#     vida+=-combosp2
#     print(f"{name} Tiene {vida} de salud")
#     time.sleep(2)
#     if vida<=0:
#         print(f"{name2} Ganó!")
#         break


#EJERCICIO 4 - Cajero (Valores randoms y el uso del while)


#Genera un "sueldo" aleatorio entre 500 y 2000.

#Pide al usuario que ingrese cuánto dinero quiere retirar.

#Valida con un while que el monto a retirar no sea mayor al sueldo ni menor a 1.

#Al final, muestra el sueldo original, lo retirado y el saldo restante.


# import random
# import time




# clave=2007

# put=int(input("Ingrese clave: "))
# while put != clave:
#     print("Clave Erronea")
#     put=int(input("Ingrese clave: "))



# select=0
# op=0
# sueldo=random.randint(10000,20000)
# cartera=25000


# while select != 3:
#     print("BIENVENIDO AL SISTEMA")
#     print("1.- Depositar Dinero")
#     print("2.- Retirar Dinero")
#     print("3.- Salir")
#     select=int(input())
#     match select:
#         case 1:
#             op=int(input(f" Saldo: ({sueldo}) Cartera: ({cartera}) Cuanto dinero desea depositar?: "))
#             while op <1 or op >cartera:
#                     print("Error, valor invalido")
#                     op=int(input(f" Saldo: ({sueldo}) Cartera: ({cartera}) Cuanto dinero desea depositar?: "))
            
#             sueldo+=op
#             cartera-=op

#             print(f'''   

#                 RESUMEN DE CUENTA:

#                 Saldo depositado: {op}  
#                 Saldo Restante: {sueldo}  
#                 Saldo Cartera: {cartera}


#                 ''')
            
#         case 2: 
      
#             op=int(input(f" Saldo: ({sueldo}) Cuanto dinero desea retirar?: "))
#             while op <1 or op >sueldo:
#                 print("Error, valor invalido")
#                 op=int(input(f"Monto: ({sueldo}) Cuanto dinero desea retirar?: "))
                
#             sueldo-=op
#             cartera+=op
                
#             print(f'''   

#                 RESUMEN DE CUENTA:

#                 Saldo Retirado: {op}  
#                 Saldo Restante: {sueldo}  
#                 Saldo Cartera: {cartera}

#                 ''')

#         case 3:
#             print("Saliendo")
            
#         case _:
#             print("Opción Invalida")


#EJERCICIO 5 - Loteria

#GENERAR 3 NUMEROS ENTRE 1 Y 9
#LUEGO TIRAR NUMEROS AL AZAR EN ESE RANGO
#GENERAR NUMEROS GANADORES DE LOTERIA Y SI ESTOS SON IGUALES A LOS GENERADOS, GANA.
# LUEGO CONTAR CUANTOS NUMEROS TUVO QUE TIRAR PARA GANAR LA LOTERIA

# import random

# num1=random.randint(1,9)
# num2=random.randint(1,9)
# num3=random.randint(1,9)

# t1=False
# t2=False
# t3=False

# intentos=0

# print(f"Numeros ganadores: {num1} {num2} {num3}")
# while not t1 or not t2 or not t3:
#         numero=random.randint(1,9)
#         print(f"El numero es: {numero}")

#         if numero == num1:
#             t1=True
#         elif numero == num2:
#             t2=True
#         elif numero == num3:
#             t3=True

#         intentos+=1

# print("Ganaste!")
# print(f"Ganaste en {intentos} intentos")


#Conceptos



#MENU


# op=int(input('''

# Seleccione una opción:
             
# 1.- OP 1
# 2.- OP 2
# 3.- OP 3
# '''))

# if op == 1:
#     print("Seleccionaste OP 1")
# elif op == 2:
#     print("Seleccionaste OP 2")
# elif op == 3:
#     print("Seleccionaste OP 3")
# else:
#     print("Opción Invalida")



#MENU RECURSIVO (USO DEL MATCH)


# op=0

# while op !=3:  
#     print("MENU")
#     print("Opción 1")
#     print("Opción 2")
#     print("Salir")
#     op=int(input())
#     match op:
#         case 1:
#             print("Seleccionate OP 1")
#         case 2:
#             print("Seleccionate OP 2")
#         case 3:
#             print("Saliendo")
#         case _:
#             print("Opción Invalida")
