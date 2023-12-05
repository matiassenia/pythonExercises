"""Ejercicio 1
Sumar tres variables
En un script de Python, crear tres variables
nombradas a, b y c con valores numéricos
cualesquiera; una cuarta llamada resultado que
sea la suma de las primeras tres, y por último
imprimir en pantalla cada una de ellas.
Antes de mostrar el valor de cada variable,
indicar su nombre en una línea anterior.
"""

a = 2
b = 9
c = 9
resultado = (a + b + c)
print ( f"a:{a}",
    f"b:{b}", 
    f"c:{c}")
print (f"resultado: {resultado}")


"""Ejercicio 1
Armar una frase con las 3 variables dadas y
mostrarla por pantalla.
texto_uno = "potente"
texto_dos = "sol"
texto_tres = "triunfo"
Es obligatorio usar las 3 variables, pero también
podés agregar palabras vos para generar una
frase. No importa el orden que elijas para las
variables."""

texto_uno = "potente"
texto_dos = "sol"
texto_tres = "triunfo"

print (f"Este {texto_uno} {texto_dos} es un simbolo de nuestro {texto_tres}")


"""Ejercicio 2
Realizar un programa que tenga 2 variables,
base = 10 y altura = 5, calcular el área de
un rectángulo y mostrar por pantalla."""

base = 10
altura = 5
area = (base*altura)
print (f"el area del rectangulo es: {area}")



"""Ejercicio 3
Dadas 2 variables: a = 20 y b = 10, mostrar por
pantalla su suma, resta, multiplicación y división"""

a = 20
b = 10
suma = (a+b)
print( f"la suma es: {suma}")

resta = (a-b)
print (f"la resta es: {resta}")

multiplicacion = (a*b)
print (f"la multiplicación es: {multiplicacion}")

division = (a/b)
print (f"la división es: {int(division)}")

"""Ejercicio 1
Tomás rindió 3 exámenes, se desea saber su
promedio sabiendo que:
nota_uno = 10
nota_dos = 6
nota_tres = 8
Mostrar el promedio por pantalla."""

nota_uno = 10
nota_dos = 6
nota_tres = 8

promedio = (nota_uno + nota_dos + nota_tres)/ 3
print (f"el promedio es: {promedio}")

"""Ejercicio 2
Hacer un programa que determine si una
persona es menor de edad o mayor de edad,
teniendo la edad en una variable.
Probar el código cambiando el valor de la
variable “edad"""

edad = 30
if edad >= 18:
    print (f"es mayor de edad")




"""Ejercicio 3
Un empleado cobró 300 dólares por mes desde enero
a junio, 500 dólares de julio a octubre, y 700 dólares
por mes en noviembre y en diciembre.
Hace un programa que calcule el sueldo promedio. Y
que diga si este “empleado” está cobrando un sueldo
bajo, normal o mejor de lo normal.
● Sueldo bajo: por debajo de 300 dólares.
● Sueldo normal: entre 300 a 900.
● Sueldo mejor de lo normal: más de 900 dólares."""

sueldo1 = 300
sueldo2 = 500
sueldo3 = 700

enero_a_junio = (sueldo1*6)
julio_a_octubre = (sueldo2*4)
noviembre_a_diciembre = (sueldo3*2)

sueldo_promedio = (enero_a_junio+julio_a_octubre+noviembre_a_diciembre)/12
print (f"sueldo promedio: {sueldo_promedio}")

if sueldo_promedio < 300:
    print(f"el sueldo es bajo")
elif sueldo_promedio < 900:
    print (f"sueldo normal")
else:
    print (f"el sueldo es mejor de lo normal") 

"""Ejercicio 1
Comparar la entrada del usuario
Crear un programa que permita ingresar dos
cadenas vía la consola y luego las compare,
imprimiendo un mensaje en caso que sean
iguales y otro en caso que sean diferentes"""

dato = input("Escribe un dato: ")
dato2 = input ("Escribe otro dato: ")

if dato == dato2:   
    print ("Está ok!")
else: 
    print ("Son distintos datos")
    
    
"""Ejercicio 2
Pedir nombre
Crear un programa que solicite el nombre de un
alumno a través de la consola, y luego chequee
que no esté vacío.
En caso de estarlo, tiene que imprimir un mensaje
de error; caso contrario, deberá imprimir un mensaje indicando que se ingresó correctamente."""

nombre = input("Escribe tu nombre: ")

if nombre == "":
    print ("Está vacio")
else:
    print (nombre)
    
"""Ejercicio 3
Comparar entrada de números
Pedir la edad por teclado y comparar si es
mayor o menor de edad. No olvidar de que para
poder comparar el ingreso debe ser convertido a
int, ya que el usuario ingresa un número entero."""

edad = input("Ingrese su edad: ")
if int(edad) < 18:
    print ("Es menor de edad")
else:
    print ("Es mayor de edad")
    
    
    
a = 1
while a < 5:
    print ("hola mundo")
    print ("desde python")
    a = a + 1
print ("Fin del programa")

"""Ejercicio 1
Incrementar una variable
Con un bucle while incrementar una variable
entera de uno en uno (desde 0 a 10 sin incluir).
Mostrar por pantalla el resultado por vuelta."""

a = 0 
while a < 11:
    print (a)
    a = a + 1



"""Ejercicio 2
Volver a pedir
Pedir por teclado el nombre de usuario, si
está vacío, volver a pedirlo hasta que se ingrese
un nombre.
Luego, saludar al usuario. """

usuario = input("Ingrese su nombre: ")

while usuario == "":
    print("No ingresó su nombre")
    usuario = input("Ingrese su nombre: ")
else:
    print (f"Hola {usuario}!")


"""Ejercicio 1
Lista de nombres
Se tiene la siguiente lista de nombres:
nombres = ["Susana","Alejandro","Roberto"]
Insertar entre Alejandro y Roberto a Paula. Y luego
agregar al final a Silvina.
Para finalizar, hay que recorrer la lista y mostrar a
todos los nombres por pantalla."""

nombres = ["Susana","Alejandro","Roberto"]
nombres.insert(2, "Paula")
nombres.append("Silvana")
indice = 0
while indice < len(nombres):
    print (nombres[indice])
    indice = indice +1
    
#for
    
"""Ejercicio 1
Recorrer lista con for
Se tiene una lista de nombres y se desea recorrer
con un bucle for.
nombres = ["Agustina","Marisa","Juan","Osvaldo"]"""

nombres = ["Agustina","Marisa","Juan","Osvaldo"]
for nombre in nombres:
    print ("dicemb")


"""Ejercicio 1
Acceso a una matriz
Los conceptos que se deberán emplear para
resolver estos ejercicios son: listas, bucle while
y bucle for, la palabra reservada break,
condicionales, la instrucción input, la instrucción int para convertir una cadena a un número
entero y str para convertir un número a una
cadena, el operador + para concatenar dos o
más cadenas, y cualquier otra que nos sea útil
para este propósito."""

"""1. Crear un programa que solicite una fila y una
columna e imprima en pantalla el número en
esa posición según la siguiente matriz:

matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

Un ejemplo de entrada (lo que escribe el
usuario) y salida (lo que se imprime en
pantalla) es el siguiente (los caracteres
en azul son ingresados por el usuario):
Fila: 1
Columna: 2
6.4
El resultado es 6.4 puesto que es el valor
ubicado en matriz[1][2]."""

matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

print (matriz)

fila = int(input("Ingrese la fila"))
columna = int(input("Ingrese la columna"))

if fila < len(matriz):
    if columna < len (matriz[fila]):
        print (matriz[fila][columna])
    else:
        print("columna invalida")
else:
    print("fila invalida")


"""Ejercicio 1
Se preguntará el tipo de rol que desempeña una
persona en una institución por una entrada del
tipo input. Los valores posibles son “admin” o
“profesor”.
Luego si la persona es “admin” o “profesor”, se
debería pedir la contraseña, siendo la única válida
“1234” (la contraseña se toma como string). Si
la contraseña ingresada es válida, se procederá a
pedir el nombre de la persona, y si no es vacío, se
lo saludará.
Contemplar los casos donde no se cumple como
corresponde y mostrar un mensaje en pantalla"""

rol = input("Que rol ocupa: ")
if rol == "admin" or rol == "profesor":
    clave = input("ingrese clave: ")
    if clave == "1234":
        nombre = input("Ingrese su nombre: ")
        print (f"Hola {nombre}")
    else:
        print ("Contraseña incorrecta")
else:    
        nombre == ("")
        print ("Incorrecto, nombre vacio")





"""1. Crear un programa que solicite una fila y una
columna e imprima en pantalla el número en
esa posición según la siguiente matriz:
matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
Un ejemplo de entrada (lo que escribe el
usuario) y salida (lo que se imprime en
pantalla) es el siguiente (los caracteres
en azul son ingresados por el usuario):
Fila: 1
Columna: 2
6.4
El resultado es 6.4 puesto que es el valor
ubicado en matriz[1][2]."""

matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

fila = int(input("Elija una fila: "))
columna = int(input("Elija una columna: "))

if fila < len(matriz):
    if columna < len(matriz[fila]):
        print(matriz[fila][columna])
    else:
        print("Error en las columnas")
else:
    print("Error en las filas")


"""Ejercicio 1
Múltiplos
Se quiere buscar los múltiplos de 3 y de 5 en un
rango que ingrese el usuario. Guardar los
múltiplos en una lista.
Se debe usar for asociado a un range como se
vio en la teoría. """

inicio = input("Ingrese el numero de incio del rango: ")
inicio = int(inicio)
final = input("Ingrese el numero del final del rango: ")
final = int(final)
multiplos = []
for n in range(inicio,final+1,1):
   if n%3 == 0 and n%5 == 0:
    multiplos.append(n)
print("Los multiplos de 3 y de 5 en ese rango son: ")
print(multiplos)

"""Ejercicio 1
Forzar el ingreso numérico.
Crear un programa que pida un número, verificar
que ese ingreso por input sea un número posible
de convertir a entero. En caso contrario volver a
pedir el ingreso."""

#Ingreso por teclado de la cantidad de nombres
cantidad = input("¿Cuantos nombres desea ingresar?: ")
#Chequeamos que sea un numero
while cantidad.isdecimal() == False:
 print("¡Error. Solo numeros!")
 cantidad = input("Ingrese un numero: ")
#Convertimos
cantidad = int(cantidad)
#Arranca la lista vacia
nombres = []
#Variable contador = 0
contador = 0

#Este bucle generara el ingreso de los nombres segun cantidad
while contador < cantidad:
 #Variable name para que sea auxiliar para guardar ingresos
 name = input("Ingrese un nombre: ")
 #el append siempre agrega al final de las listas
 nombres.append(name)
 #variable contador(de vueltas) se usara para comparar con cantidad
 contador = contador + 1
print("La lista de nombres: ")
for n in nombres:
 print("-",n)
 
 
 """Ejercicio 1
Generar un rango con una función
Crear una función rango (desde, hasta, intervalo)
que retorne una lista de números, tal como la
función incorporada range(), aunque según el
intervalo especificado.
(No puede usar la función range() para resolver este
ejercicio)
Por ejemplo, el siguiente código:
lista = rango(1, 10, 2)
print(lista)
debe imprimir:
[1, 3, 5, 7, 9]
Puesto que se genera una lista desde 1 hasta 10
con un intervalo de 2.
Tomar como base el código de la función rango()
que se encuentra en el material del alumno."""


def rango(desde, hasta, intervalo):
 numeros = []
 while desde < hasta:
    numeros.append(desde)
 desde = desde + intervalo
 return numeros
lista = rango(1, 10, 2)
print(lista)