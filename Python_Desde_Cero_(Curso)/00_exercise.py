#Ejercicio 1

print("Hola Mundo")

#Ejercicio 2

# En la linea 1 usamos la funcion print 
# para mostrar en la terminal "Hola Mundo"

#Ejercicio 3

print("Mi nombre es Jheremy, tengo 21 años")

#Ejercicio 4
print(type("esto es un str")) #<class 'str'>
print(type(16)) # <class 'int'>
print(type(16.5)) # <class 'float'>

#En las lineas 8, 9, 10, imprimimos la función type para saber
#cual es el tipo de dato de lo que estamos imprimiendo

#Ejercicio 5

""" 
Los tipos de datos son la informacion que ya esta lo que es el leguaje lo reconoce,
a lo que me refiero es que son datos que nosotros usamos atraves del interprete para
comunicarnos y darle ordenes al sistema, y todo lenguaje de programacion cuenta con estos.
si no me equivoco son los datos de tipo primitivo, son los mas xbasicos. (str, int, float,
bool, etc...)
"""
#Ejercicio 6

hello = "Hi!!"

name = "Jheremy"

mensaje = hello + " " + name

print(mensaje)

#My exaple.

hello_2 = "Hi!!"

name_2 = "Jheremy"

texto = ("hi!!", "Jheremy")

print(hello_2, name_2)

""" 
Que ocurre aqui, en esta parte del codigo, use dos formas de juntar
valores (str en este caso). Pero que pasa, en el primer ejemplo se realizo
una concatenacion, pero en el segundo ejemplo no, ya que usar la funcion print()
y separando cada variable con comas, no estamos concatenando, solo estamos imprimiendo 
los valores juntos pero por se parado, a lo que me refiero es a que no estan unidos en 
en una variable lo cual puedas ver claramente que estan juntos en una sola linea por + o 
una F_string (f"")
"""

#Ejercicio 7

nombre = "jheremy"

edad = str(21)

saludo = ("hola mi nombre es " + nombre + "tengo " + edad + " años")

saludo_2 = f"hola mi nombre es {nombre} y tengo {edad} años"

print(saludo)
print(saludo_2)

#Ejercicio 8

print("Hola usuario, cual es tu nombre? ")

user_name = input()

print("Hola", user_name, "es un gusto verte por aqui <3")

user_salu = "Hola " + user_name + ", es un gusto verte por aqui <3"

print(user_salu)

# Ejercicio 9 y 10

val_1 = 10  # Se crea una variable con valor entero (int)
val_2 = 15  # Se crea otra variable con valor entero (int)

suma = val_1 + val_2  # Se suman ambas variables y el resultado se guarda en 'suma'

# Se muestra el resultado de la suma usando f-string
print(f"Este es el resultado de la suma: {suma}")

# Se muestra el tipo de dato del resultado usando la función type()
print(type(suma))  # <class 'int'>
