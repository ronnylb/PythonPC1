#PRACTICA 1

#VARIABLES

#Problema 1
nombre=str(input("Solicitar nombre: "))
print("¡Hola",nombre,"!")

#Problema 2
consumo= float(input("¿Cuanto fue su consumo?: "))
propina= float(input("¿Cuanto de propina desea dejar? (colocar en decimales el %): "))
propinafinal=consumo*propina
print("La propina es de:",propinafinal)

#Problema 3
payaso=1
payaso=payaso+1
munecas=1

#Problema 4
numero=int(input("Escriba un numero entero: "))
n=(numero*(numero+1))/2
print(n)

#CONDICIONALES

#Problema 5
show=int(input("¿cuántos shows musicales ha visto en el último año?: "))
if show > 3:
    print("true")
else:
    print ("false")

#Problema 6
edad=int(input("¿Cual es su edad?: "))
if edad<4:
    print("Ingresa Gratis")
elif edad>4 and edad<18:
    print("Debe pagar $5")
elif edad>18:
    print("Debe pagar $10")