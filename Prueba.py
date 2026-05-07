
# print("Ingrese su nombre")
# nombre=input()
# edad=int(input("Ingrese su edad: "))
# print("Hola", nombre, "su edad en 5 años será", edad+5)

# nombre=input("Ingrese su nombre: ")
# edad=input("Ingrese su edad: ")
# print(f"Hola {nombre} Su edad es {edad}")

# ========================================

# print("Ingrese el 1er numero: ")
# num1=int(input())
# print("Ingrese el 2do numero: ")
# num2=int(input())

# print("La suma de los dos numeros es: ", num1+num2)
# print("La resta de los dos numeros es: ", num1-num2)

# ========================================

# n1=int(input("Ingrese 1er numero: "))
# n2=int(input("Ingrese 2do numero: "))
# print("La suma de los dos numeros es: ", n1+n2)
# print("La resta de los dos numeros es: ", n1-n2)

# ========================================

#Menu uso del IF

# print(
# '''
# 1.- Pera 1200
# 2.- Manzana 1400
# 3.- Piña 2000

# '''
# )

# select=int(input("Seleccione una opción: "))

# if select==1:
#     print("El total a pagar es: ", 1200*1.19)
# elif select==2:
#     print("El total a pagar es: ", 1400*1.19)
# elif select==3:
#     print("El total a pagar es: ", 2000*1.19)
# else:
#     print("Numero no valido")

# ========================================

#Uso del FOR

# 1)


# for i in range(3):
#     print("Repeticion N ", i+1)


# 2)


# num=int(input("Ingrese un numero: "))

# for i in range (num):
#     print(i+1, "Hola")


# 3)


# num=int(input("Ingrese un numero: "))

# for i in range (10):
#     print(num, " X ", i+1, " = ", num*(i+1))


# 4)


# num=int(input("Ingrese la cantidad de notas: "))
# suma=0
# for i in range(num):
#     nota=float(input("Ingresa la nota: "))
#     suma=suma+nota
# prom=suma/num
# print("El promedio es: ", prom)
# if prom >= 4:
#     print("El alumno aprobó")
# else:
#     print("El alumno reprobó")


# 5)

# for i in "TunTunSahur":
#     print(i)


# 6)


# nom=input("Ingrese su nombre: ")
# cont=nom
# for i in nom:
#     print(i)
#     cont=cont+1
# print("La cantidad de caracteres es: ", cont)


# 7)


# nom=input("Ingrese su nombre: ")
# cont=nom
# cont=0
# for i in nom:
#     if i in "aeiouAEIOU":
#     cont=+1
# print("La cantidad de caracteres es: ", cont)

# ========================================

#Promedio

# num=int(input("Ingrese cantidad de notas: "))
# sum=0
# for i in range (num):
#     notas=float(input(f"Ingrese la nota {i+1}: "))
#     sum=sum+notas
# prom=sum/notas
# print("Promedio: ",round(prom, 1))

# if prom>= 4:
#     print("El alumno aprobo")
# else:
#     print("Alumno reprobó")

# titulo="Clima actual" #Tipo string
# temp=18.6 #float
# DiaDelMes=16 #int
# Mes=4 #int
# Llueve=False

# print(f"{titulo}")
# print(f"Fecha de hoy: {DiaDelMes}-{Mes}")
# print(f"temperatura actual: {temp} Grados")

# if Llueve:
#     print("Saque el paraguas")
# else:
#     print("No saque paraguas")

# num=int(input("Ingrese un numero: "))
# for i in range(num):
#     print(f"{i+1} Hola guatona con moño")


#Pedir nombre al usuario y decirle cuantas letras son


# nom=(input("Ingrese su nombre: "))
# cont=0
# for i in nom:
#     cont=cont+1
# print(f"Su nombre posee: {cont} caracteres")

#Se usa f {variable} para usar una concatenacion dentro de una linea de codigo (print)


#Contar solamente las vocales en un nombre


# nom=(input("Ingrese su nombre: "))
# vocales=0
# for i in nom:
#     # vocales=vocales+1
#     if i in "aeiou" "AEIOU":
#         vocales+=1
# print(f"Su nombre posee: {vocales} vocales")


#Contar solamente las consonantes


# nom=(input("Ingrese su nombre: "))
# consonantes=0
# for i in nom:
#     # vocales=vocales+1
#     if i in "BCDFGHJKLMNÑPQRSTVXZWY" "bcdfghjklmnñpqrstvxzwy":
#         consonantes+=1
# print(f"Su nombre posee: {consonantes} consonantes")


#Vocales y consonantes: 


# nom=(input("Ingrese su nombre: "))
# vocales=0
# cons=0
# for i in nom:
#     # vocales=vocales+1
#     if i in "aeiou" "AEIOU":
#         vocales+=1
#     elif i==" ":
#         print()
#     else:
#         cons+=1
# print(f"Su nombre posee: {vocales} vocales")
# print(f"Su nombre posee: {cons} consonantes")


#Formas de concatenar


# ent1="Seba"
# equip1=6

# ent2="Jairito"
# equip2=4

# print(f"El entrenador {ent1} Tiene {equip1} Pokemons")
# print("El entrenador", ent1,  "Tiene", equip1,  "Pokemons")


#Repeticion de una variable


# print((ent1+" ")*5)


#Caracter


# name="Seba"

# print(name[3])


#Funciones para strings


# name=" Seba "

# print(name.strip()) #Junta los espacios
# print(name.lower()) #Minuscula
# print(name.upper()) #Mayuscula
# print(name.upper().strip()) #Combinacion de ambos
# print(name.replace("Seba", "Tomas")) #Reemplazar string
# print(name.split()) #Hacer lista
# print(name.replace("Seba", "Tomas").split()) #Combinacion de ambos
# print(len(name))


#Ejercicio 1

# clave="SHAZAM"

# pasw=input("Ingrese la clave: ")

# if pasw.upper() == clave:

#     print("Clave Correcta")

# else:
#     print("Clave Incorrecta")


#Ejercicio 2


# nom=input("Ingrese un nombre de usuario: ")

# if len(nom) in range(4,10):
#       print("Sucess")
# else:
#     print("Unsucess")


#Ejercicio 3


# pin=(input("CREE PIN DE 4 DIGITOS: "))

# if len(str(pin)) in range(4, 5):
#      print("Pin creado correctamente")
# else:
#      print("Pin Invalido")

     
# pin=int(input("CREE PIN DE 4 DIGITOS: "))

# if pin> 1000 and pin <9999:
#      print("Pin creado correctamente")
# else:
#      print("Pin Invalido")



#Uso del match y case

# print("1.- Opcion 1")
# print("1.- Opcion 1")
# print("1.- Opcion 1")
# print("Seleccione una opcion")
# op=int(input())
# match op:
#     case 1:
#         print("El total a pagar es: ")
#     case 2:
#         print("El total a pagar es: ")
#     case 3:
#         print("El total a pagar es: ")
#     case _:
#         print("Opcion invalida")

#Usar while


# cont=1
# while cont<=3:
#     print(f"El contador es {cont}")
#     cont+=1

#================================================

# pin=5656
# num=int(input("Ingrese su pin: "))
# while num != pin:
#     print("Clave erronea")
#     num=int(input("Ingrese su pin: "))
# print("Bienvenido al sistema")

#================================================


#Tienda

# op=0
# total=0
# while op != 4:
#     print("1.- PC $500.000")
#     print("2.- LGTV $450.000")
#     print("3.- MICROONDAS $100.000")
#     print("4.- SALIR")
#     op=int(input())
#     match op:
#         case 1:
#             print(f"El total a pagar es: {500000*1.19}" )
#             total+=500000*1.19
#         case 2:
#             print(f"El total a pagar es: {450000*1.19}")
#             total+=450000*1.19
#         case 3:
#             print(f"El total a pagar es: {100000*1.19}")
#             total+=100000*1.19
#         case 4:
#             print("Saliendo")
#             print(f"El total a pagar es {total}")
#         case _:
#             print("Opcion invalida")


#================================================

#Calculadora


# op=0
# total=0
# while op != 5:
#     print("== CALCULADORA ==")
#     print("1.- Sumar")
#     print("2.- Restar")
#     print("3.- Multiplicar")
#     print("4.- Dividir")
#     print("5.- SALIR")
#     op=int(input())
#     match op:
#         case 1:
#             n1=int(input("Ingrese un numero: "))
#             n2=int(input("Ingrese otro numero: "))
#             print(f"El resultado es {n1+n2}") 

#         case 2:
#             n1=int(input("Ingrese un numero: "))
#             n2=int(input("Ingrese otr numero: "))
#             print(f"El resultado es {n1-n2}") 

#         case 3:
#             n1=int(input("Ingrese un numero: "))
#             n2=int(input("Ingrese otr numero: "))
#             print(f"El resultado es {n1*n2}") 

#         case 4:
#             n1=int(input("Ingrese un numero: "))
#             n2=int(input("Ingrese otr numero: "))
#             print(f"El resultado es {n1/n2}") 

#         case 5:
#             print("Saliendo")

#         case _:
#             print("Opcion invalida")


#================================================


#Funciones

#DEF se usa para acelerar, asignar y definir procesos en una funcion (basicamente asigan todo un bloque de codigo a una sola variable)

# def suma():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"El resultado es {n1+n2}")
# def resta():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"El resultado es {n1-n2}")
# def mult():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"El resultado es {n1*n2}")
# def div():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"El resultado es {n1/n2}")
# def calculadora():
    # op=0
    # total=0
    # while op != 5:
    #     print("== CALCULADORA ==")
    #     print("1.- Sumar")
    #     print("2.- Restar")
    #     print("3.- Multiplicar")
    #     print("4.- Dividir")
    #     print("5.- SALIR")
    #     op=int(input())
    #  match op:
    #     case 1:
    #         suma()

    #     case 2:
    #         resta()

    #     case 3:
    #         mult()

    #     case 4:
    #         div() 

    #     case 5:
    #         print("Saliendo")

    #     case _:
    #         print("Opcion invalida")


#Tarea 1

# def promedio():
#     num=int(input("Ingrese la cantidad de notas: "))
#     suma=0
#     for i in range(num):
#         nota=float(input("Ingresa la nota: "))
#         suma=suma+nota
#     prom=suma/num
#     print("El promedio es: ", prom)
#     if prom >= 4:
#         print("El alumno aprobó")
#     else:
#         print("El alumno reprobó")
# def calculadora():
#      op=0
#      total=0
#      while op != 5:
#         print("== CALCULADORA ==")
#         print("1.- Sumar")
#         print("2.- Restar")
#         print("3.- Multiplicar")
#         print("4.- Dividir")
#         print("5.- SALIR")
#         op=int(input())
#         match op:
#             case 1:
#                 n1=int(input("Ingrese un numero: "))
#                 n2=int(input("Ingrese otro numero: "))
#                 print(f"El resultado es {n1+n2}") 

#             case 2:
#                 n1=int(input("Ingrese un numero: "))
#                 n2=int(input("Ingrese otr numero: "))
#                 print(f"El resultado es {n1-n2}") 

#             case 3:
#                 n1=int(input("Ingrese un numero: "))
#                 n2=int(input("Ingrese otr numero: "))
#                 print(f"El resultado es {n1*n2}") 

#             case 4:
#                 n1=int(input("Ingrese un numero: "))
#                 n2=int(input("Ingrese otr numero: "))
#                 print(f"El resultado es {n1/n2}") 

#             case 5:
#                 print("Saliendo")

#             case _:
#                 print("Opcion invalida")
# def tienda():
# op=0
# total=0
# while op != 4:
#         print("== TIENDA ==")
#         print("1.- PC $500.000")
#         print("2.- LGTV $450.000")
#         print("3.- MICROONDAS $100.000")
#         print("4.- SALIR")
#         op=int(input())
#         match op:
#             case 1:
#                 print(f"El total a pagar es: {500000*1.19}" )
#                 total+=500000*1.19
#             case 2:
#                 print(f"El total a pagar es: {450000*1.19}")
#                 total+=450000*1.19
#             case 3:
#                 print(f"El total a pagar es: {100000*1.19}")
#                 total+=100000*1.19
#             case 4:
#                 print("Saliendo")
#                 print(f"El total a pagar es {total}")
#             case _:
#                 print("Opcion invalida")

# op=0
# while op != 4:
#     print("PROGRAMAS DE PYTHON")
#     print("1.-  Promedio de notas")
#     print("2.-  Calculadora")
#     print("3.-  Tienda")
#     print("4.-  Salir")
#     op=int(input())
#     match op:
#         case 1: 
#             promedio()
#         case 2: 
#             calculadora()
#         case 3: 
#             tienda()
#         case 4:
#             print("Saliendo")
#         case _:
#             print("Opcion Invalida")

#==================================================


#Ejemplos RANDOM

# import random

# num=random.randint(1,10)
# print(num)

# for i in range(num):
#     print("Hola Seba")

#==================================================

# dado1=random.randint(1,6)

# print(F"El dado dio {dado1}")

#==================================================

# Ejercicio 1 Adivinar un numero del 1,10 (SIN TERMINAR)

# import random

# intentos=5

# num=random.randint(1,10)



# for i in range (5):

#     asw=int(input("Adivine el numero:"))

#     if asw<num:
#         print("El numero a adivinar es mayor ")

#     else:
#         print("El numero a adivinar es menor ")
    

#         if asw==num:
#             print("Adivinaste ")

#         elif intentos==5:
#             print(f"Intentos terminados. El numero era {num} ")

#=====================================================

#Ejercicio 2 Crear un ludo

# import time
# import random

# acum=0

# while acum!=30:

#     dado=random.randint(1,6)
#     dado2=random.randint(1,6)

#     print(f"Usted saco un {dado}")
    
#     print(f"Usted saco un {dado2}")
    
#     print(f"Avanzas {dado+dado2} casillas")
    
#     acum=acum+dado+dado2

# if acum<=30:
#     print(f"Has ganado, haz llegado a {acum}")

#======================================================

#Ejercicio 3 crear un juego de pelea

# import random
# import time

# fighter1=100
# fighter2=100


# while fighter1 or fighter2 >0:
#     golpe=random.randint(7,18)
#     golpe2=random.randint(7,18)
#     print(f"Fighter 1 hizo {golpe} de Daño!")
#     fighter2=fighter2-golpe
#     time.sleep(2)
#     print(f"Fighter 2 tiene {fighter2} puntos de vida")
#     if fighter2<=0:
#         print("Fighter 1 Gano!")
#         break

#     time.sleep(2)
#     print(f"Fighter 2 hizo {golpe2} de Daño!") 
#     fighter1=fighter1-golpe2
#     time.sleep(2)
#     print(f"Fighter 1 tiene {fighter2} puntos de vida")
#     time.sleep(2)
#     if fighter1<=0:
#         print("Fighter 2 Gano!")
#         break
    
#========================================================

#Ejercicio 4 Juego de golf

# import random
# import time

# j1=random.randint(60,190)
# j2=random.randint(60,190)
# j3=random.randint(60,190)
# print(f"El jugador 1 lanzo la pelota {j1} Metros")
# time.sleep(2)
# print(f"El jugador 2 lanzo la pelota {j2} Metros")
# time.sleep(2)
# print(f"El jugador 3 lanzo la pelota {j3} Metros")

# if j1>j2 and j1>j3:
#     print("El jugador 1 lanzo la pelota mas lejos")
    
# elif j2>j3:
#     print("El jugador 2 lanzo la pelota mas lejos")
    
# else:
#     print("El jugador 3 lanzo la pelota mas lejos")
    

# EJERCICIOS REPASO PARA LA PRUEBA

# 1)

#USO DEL IF

# op=0
# cantP=0
# total=0
# niños=0
# limite=0
# while op !=4:
#     print(''' ==EPSTEIN ISLAND==
#     1.- Niño (1-17) $1.000
#     2.- Adulto (18-64) $3.000
#     3.- Adulto Mayor (64 o más) $1.500     
#     4.- Salir''')
#     op=int(input())
#     match op:
#         case 1:
#             print("Usted selecciono entrada: Niño")
#             c=int(input("Cuantos niños son? (1-10): "))
            
#             if c>1 or c<=10:
#                 total+=1000*c
#                 cantP+=c
#             else:
#                 print("ERROR: FUERA DE RANGO")
                
#         case 2:
#             print("Usted selecciono entrada: Adulto")
#             c=int(input("Cuantos adultos son? (1-10): "))
#             if  c>1 or c<=10:
#                 total+=3000*c
#                 cantP+=c
#             else:
#                 print("ERROR: FUERA DE RANGO")
        
#         case 3:
#             print("Usted selecciono entrada: Adulto Mayor")
#             c=int(input("Cuantos adultos son? (1-10): "))
#             if  c>1 or c<=10:
#                 total+=1500*c
#                 cantP+=c
#             else:
#                 print("ERROR: FUERA DE RANGO")
        
#         case 4:
#             print("Saliendo")
#             print(f"El total a pagar es: {total}")
#             print(f"Tickets: {cantP}")
#         case _:
#             print()
            

#USO DEL WHILE

# op=0
# cantP=0
# total=0
# niños=0
# limite=0
# while op !=4:
#     print(''' ==EPSTEIN ISLAND==
#     1.- Niño (1-17) $1.000
#     2.- Adulto (18-64) $3.000
#     3.- Adulto Mayor (64 o más) $1.500     
#     4.- Salir''')
#     op=int(input())
#     match op:
#         case 1:
#             print("Usted selecciono entrada: Niño")
#             c=int(input("Cuantos niños son? (1-10): "))
#             while c<1 or c>10:
#                 print("ERROR: FUERA DE RANGO")
#             total+=1000*c
#             cantP+=c
                
#         case 2:
#             print("Usted selecciono entrada: Adulto")
#             c=int(input("Cuantos adultos son? (1-10): "))
#             while c<1 or c>10:
#                 print("ERROR: FUERA DE RANGO")
#             total+=3000*c
#             cantP+=c
        
#         case 3:
#             print("Usted selecciono entrada: Adulto Mayor")
#             while c<1 or c>10:
#                 print("ERROR: FUERA DE RANGO")
#             total+=1500*c
#             cantP+=c
        
#         case 4:
#             print("Saliendo")
#             print(f"El total a pagar es: {total}")
#             print(f"Tickets: {cantP}")
#         case _:
#             print()


#2) (INACABADO, HACER QUE EL DESCUENTO RANDOM AL APLICARSE, APAREZCA EN LA PANTALLA UN TEXTO QUE DIGA: DESCUENTO APLICADO. PRECIO FINAL: (PRECIO CON DESCUENTO))

# import random
# import time

# cod=random.randint(1, 21000)

# vip=40000*1.8
# general=40000*1.4
# tribuna=40000*1.2
# pd=vip*0.90
# asw=int(input('''
#     QUE CANCHA ES?
          
#     1.- Vip - $40000
#     2.- General - $40000
#     3.- Tribuna - $40000      
          
#     '''))
    
# match asw:
#         case 1:
#                 print(f"Precio a pagar: {vip}")

#         case 2:
#                 print(f"Precio a pagar: {general}")

#         case 3:
#                 print(f"Precio a pagar: {tribuna}")



# if cod <6999 and cod>21001:
#         print(f"Precio a pagar con descuento: {pd}")

#================================================================

# NUEVOS EJERCICIOS:

#EJERCICIO PRUEBA 1:

#1) LOTERIA.
#GENERAR 3 NUMEROS ENTRE 1 Y 9
#LUEGO TIRAR NUMEROS AL AZAR EN ESE RANGO
#GENERAR NUMEROS GANADORES DE LOTERIA Y SI ESTOS SON IGUALES A LOS GENERADOS, GANA.
# LUEGO CONTAR CUANTOS NUMEROS TUVO QUE TIRAR PARA GANAR LA LOTERIA
 
# import random
# import time

# intentos=0

# n1=random.randint(1,9)
# n2=random.randint(1,9)
# n3=random.randint(1,9)
# t1=False
# t2=False
# t3=False

# print(f"Numeros ganadores: {n1} {n2} {n3}")
# while not t1 or not t2 or not t3:
#     numero=random.randint(1,9)
#     print(f"El numero es: {numero}")
    
    
#     if numero==n1:
#         t1=True
#     elif numero==n2:
#         t2=True
#     elif numero==n3:
#         t3=True

#     intentos+=+1

# print(f"Ganaste")
# print(f"Ganaste en {intentos} turnos")
    
#================================================================

#EJERCICIO PRUEBA 2:

#Se necesita hacer un algoritmo de productos enlatados
#Se debe consultar el peso del producto (en gramos) (solo valores positivos)
#Se debe consultar el porcentaje de sodio (1-100)
#Y si se vende nacional o internacional

#Criterios:

#Menos de 500grs, lata normal
#Sodio hasta 1500gr, lata mediana
#Sodio +1501, lata grande
#Si el sodio es menos de 5 queda igual.
#Si es entre 5 y 8, lata especial
#Si tiene +9, lata acorazada
#A las latas internacionales, se le debe pegar un sticker y las nacionales no
#Hacer un resumen de todo

#Codigo:

# prod=int(input("Ingrese el peso del producto (Gramos): "))
# while prod <1:
#     print("Debe ser un valor positivo")
#     prod=int(input("Ingrese el peso del producto (Gramos): "))



# sodium=int(input("Ingrese el porcentaje de sodio (1-100): "))
# while sodium <1 or sodium >100:
#     print("Procentaje Invalido")
#     sodium=int(input("Ingrese el porcentaje de sodio (1-100): "))



# inter=int(input('''

# Como se vendera?
             
# 1-Internacional
# 2-Nacionalmente
             
             
# Ingrese valor: '''))



# while inter <1 or inter >3:
#        print("Opción Invalida")
#        inter=int(input('''

# Como se vendera?
             
# 1-Internacional
# 2-Nacionalmente
             
             
# Ingrese valor: '''))
       


# if prod > 0 and prod <= 500:
#     print("Lata normal")

# elif prod >=501 and prod <=1500:
#     print("Lata mediana")

# elif prod >1500:
#     print("Lata grande")



# if sodium >0 and sodium <5:
#         print("Lata comun")

# elif sodium >=5 and sodium <8:
#         print("Lata especial")

# elif sodium >=9:
#         print("Lata acorazada")




# if inter ==1:
#             print("Pegue un sticker de validación")

# elif inter == 2:
#             print("No se debe pegar ningun sticker")
