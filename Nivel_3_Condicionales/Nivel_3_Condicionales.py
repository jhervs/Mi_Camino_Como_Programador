#Ejercicio 1 (Edad y acceso)

""" 
Pide al usuario se edad y
muestra un mensaje:

1. Si es menor de 18: "No puedes acceder"
2. Si es mayor de 18: "Bienvenido al sistema"
"""

#Bienvenida
print(""" 
Hola usuario :3. Antes de entrar
que edad tienes?

""")

edad = int(input()) #variable input(), type<'int'>

#condicionales
if edad < 18:
    print("Lo sentimos, no puedes acceder\n ")
else:
    print("Bienvenido al sistema <3\n ")

""" 
Un programa simple de acceso
donde si el usuario cumple los
requisitos, tiene acceso y si no
no puede acceder.
"""

#Ejercicio 2 (Validad contraseña)

""" 
Crea un sistema que compare una contraseña 
predefinida con la ingresada por el usuario.
muestra "acceso concedido" si coincide o
"Accesedo denegado" si no.
"""

correct_pass = "python162" #variable type<'str'>
user_pass = input("Hola usuario. Introduzca su contraseña ") #variable input(), type<'str'>

#condicionales
if user_pass == correct_pass:
    print("Acceso concedido\n ")
else:
    print("Acceso denegado\n ")

#Ejercicio 3 (Numero positivo, negativo o cero)

""" 
Solicita un numero y di si es:

1. Positivo
2. Negativo
3. cero
"""
#Bienvenida
print("""
Hola usuario. 
Bienvenido al sistema de identificacion
positivo, negativo o cero :3
""")

num = int(input("Que numero quieres que identifique? ")) #variable input(), type<'int'>

#condicionales
if num < 0:
    print("Su numero es negativo\n ")
elif num > 0:
    print("Su numero es positivo\n ")
elif num == 0:
    print("Su numero es 0\n ")
else:
    print("Valor no valido\n ")

""" 
Programa que consiste en identificar
si el valor numerico introducido es 
negativo, positivo o es cero.

Nota quise agragar una 4ta condicion
que es la condicion "num == 0"
ya que si el usuario pone un numero
con potencias o complejo, no quiero que
le diga que es 0 por eso hice la otra 
condicion de "Valor no valido".
"""

#Ejercicio 4 (par o impar)

""" 
Pide un numero al usuario e imprime
si es par o impar.
"""

#bienvenida
print("Hola usuario. \nBienvenido al identificador de numero pares :3")

user_val = int(input("Que numero quieres comprobar?\n ")) #variable input(), type<'int'>

#condicionales
if user_val % 2 == 0:
    print("Su numero es par")
else:
    print("Su numero es impar")

""" 
Programa que consiste en comprobar por 
medio del operador "%" y hacer una
operacion junto con el 2, si el numero
introducido es par o no.

Puede que surja la duda, de como?
Bueno, el operador modulo (%)
consiste en darnos el resto de una
division, por lo que si hacemos una
operacion como esta "x_num % 2"
verificaremos primero si el numero 
es divisible entre 2 (si lo es, es par)
y si la operacion tiene residuos o no,
lo que comprobaria que es par, al no tener.
"""

#Ejercicio 5 (Mayor a tres numeros)

""" 
Solicita tres numeros y determina cual es mayor
"""

print("""
Bienvenido usuario al comprobador de cual es mayor que? :3
Comprobaremos tres nummeros :3
""")

a = int(input("Introduce el primer numero ")) #variable input(), type<'int'>
b = int(input("Introduce el segundo numero ")) #variable input(), type<'int'>
c = int(input("Introduce el tercero numero ")) #variable input(), type<'int'>

#condicionales
if a >= b and a >= c:
    print(f"El numero {a} es el mayor\n")
elif b >= a and b >= c:
    print(f"El numero {b} es el mayor\n")
else:
    print(f"El numero {c} es el mayor\n ")

""" 
Programa que compueba cual es 
el numero mayor de tre numeros
ingresado por el usuario.

Nota: se coloca mayor o igual (>=)
ya que puede que los valores introducidos 
sean iguales y al no ampliar el rago de 
posibilidades de la condicion, el programa 
no nos va dar la respuesta correcta.

por ejemplo:

si damos el 7 como valor para los
dos primeros numero, y el 4 como el
tercero, el programa nos dira que 
el tercer numero (4) es el mayor
ya que como no se cumplen las dos 
primeras condiciones, se ejecuta el else.
Claro esto se podria solucionar creando 
una condicion mas clara para el tercer 
numero, y un else para posibles valores
que no soporte el programa, pero 
poner el >= tambien lo soluciona.
"""

#Ejercicio 6 (Clasificacion de nota)

""" 
Pide al usuario una nota (0 - 100) y clasificala como:

1. 90-100: Excelente
2. 70-89: Aprobado
3. 0-69: Reprobado
"""
print("Hola usuario. Comprobemos tu nota")

nota = int(input("Introduce tu nota ")) #variable input(), type<'int'>

#condicionales
if nota >= 90 or nota == 100:
    print("Excelente, estas en tu prime :3\n ")
elif nota >= 70 or nota == 89:
    print("Has aprobado, vamos a por mas >:3\n ")
else:
    print("Has reprobado, se que puedes, sigue adelante <3\n ")

""" 
Programa que comprueba la nota
intruducida por el usuario.
Se usaron operadores de comparacion
y se fijo el rago limite de la nota.
"""

#Ejercicio 7 (Menu interactivo)

""" 
Crea un menu que le pida al usuario 
elegir una opcion del 1 al 3:

1. Ver perfil
2. Cambiar de color 
3. Salir 
"""

#Bienvenida
print("""
Hola usuario, bienvenido al menu interactivo :3
Cuales de estas opciondes quieres hacer?

1. Ver perfil
2. Cambiar de color
3. Salir

""")

opcion = int(input("Cuales de las opciones quieres hacer? ")) #variable type<'int'>

#condicionales
if opcion == 1:
    print("Mostrando perfil....")
elif opcion == 2:
    print("Cambiando de color....")
elif opcion == 3:
    print("Saliendo del sistema....")
else:
    print("Opcion no valida....")

""" 
En este reto realizamos un menu interactivo
sencillo donde el usuario escoge una opcion 
y segun la opcion el programa hace una accion.
"""

#Ejercicio 8 (Año bisiesto)

""" 
Escribe un programa que verifique si un año
es bisiesto. Un año bisiesto si es divisible
por 4 pero no por 100, salvo que tambien sea
divisible por 400
"""
#bienvenida
print("Bienvenido a tu verificador de años bisiesto :3\n")

user_year = int(input("Introduce el año a verificar\n ")) #variable input(), type<'int'>

#condicionales
if user_year % 4 == 0:
    print("Es año bisiesto")
elif user_year % 4 != 0:
    print("No es año bisiesto")
else:
    print("El valor introducido es incorrecto")

#Correccion

#condicionales
if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")

""" 
Quise intentar hacer dos ejemplos, uno sin guia
y el otro teniendo en cuenta el ejemplo.

En el primero, no esta mal, pero puede
que no cubra muchas posibilidades en 
la condicion, como en el caso de la 
correccion, esto dando mas posibilidades
de que de un resultado erroneo.

Aun que en el enunciado estaba claro 
lo que se tenia que hacer, no me 
encuentro totalmente lucido mentalmente.
"""
