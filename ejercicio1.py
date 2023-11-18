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
peso_payaso = 112
peso_muñeca = 75
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
print("El peso total del paquete es " + str(peso_total))

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

#Problema 7
numero1 =int(input("Ingrese numero 1: "))
numero2 =int(input("Ingrese numero 2: "))
msg=input("Selecciona una de las 3 opciones: \n1) Suma de ambos numeros. \n2) Resta de Ambos numeros \n3) Multiplicacion de ambos numeros.")
if msg == '1':
    suma=numero1+numero2
    print("La suma es:",suma)
elif msg=='2':
    resta=numero2-numero1
    print("La resta es:",resta)
elif msg =='3':
    multi=numero1*numero2
    print("La multiplicacion es:",multi)
else:
    print("Opcion incorrecta, seleccionar una opcion valida")

#Problema 8
tiempo=(input("Ingrese hora: "))
hora, minutos=tiempo.split(":")
if hora =='7' or (hora=='8' and minutos=='00'):
    print("Es hora de Desayunar")
elif hora == '12' or (hora=='12' and minutos=='00'):
    print("Es hora de Almorzar")
elif hora == '18' or (hora=='18' and minutos=='00'):
    print("Es hora de Cenar")
else:
    print("")

#COLECCION DE DATOS

#Problema 9

a = input("Ingrese palabra 1: ")
b = input("Ingrese palabra 2: ")
c = input("Ingrese palabra 3: ")
d = input("Ingrese palabra 4: ")
e = input("Ingrese palabra 5: ")
listado=[e,d,c,b,a]
print(listado)

#Problema 10
lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

lista.remove(lista[5])
lista.remove(lista[4])
lista.remove(lista[0])

lista


#Problema 11
lista= [1, 1, 2, 3, 4, 4, 5, 1]
lista1=set(lista)
lista1

#Problema 12












