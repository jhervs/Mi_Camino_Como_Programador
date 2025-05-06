#Reto 1 (Operaciones basicas con nuemros)

""" 
Declara dos numeros enteros y realiza:

1. + suma
2. - resta
3. * multiplicacion
4. / division
"""

a = 16 #variable type<'int'>
b = 4 #variable type<'int'>

print("suma:", a + b ) #print(20) type<'int'>
print("resta:", a - b) #print(12) type<'int'>
print("multiplicacion:", a * b) #print(64) type<'int'>
print("division:", a / b) #print(4) type<'int'>

""" 
En la susecion de lineas con print()
se realizan las operaciones que nos
pide el reto
"""

#Reto 2 (Uso del operador %)

x = 34 #variable type<'int'>
y = 4 #variable type<'int'>

#imprime el resultado de la operacion

print("residuo:", x % y) #print(2) type<'int'>

#reto 3 (comparadores logicos)

""" 
Declara dos variables y comparalas 
"""

m = 10 #variable type<'int'>
n = 5 #variable type<'int'>

#se imprimen las comparaciones 
print(m > n) #print(True) type<'bool'>
print(m < n) #print(False) type<'bool'>
print(m == n) #print(False) type<'bool'>
print(m != n) #print(True) type<'bool'>
print(m >= n) #print(True) type<'bool'>
print(m <= n) #print(False) type<'bool'>

""" 
Bueno, puede que los (>= y <=) no
sean muy necesarios, pero quice
usar todos los operadores de comparacion 
"""

#reto 4 (combina condiciones con and y or)

pedido = 5 #variable type<'int'>
comida = "hamburguesa" #variable type<'str'>

print(pedido > 3 and comida == "hamburguesa") #print(True) type<'bool'>
print(pedido < 2 or comida == "pizza") #print(False) type<'bool'>

#reto 5 (condicionales if, elif, else)

""" 
Crea un programa que pida la edad 
del usuario y diga si es:

1. menor de edad
2. adulto joven
3. adulto
"""

#edad = int(input("Hola usuario, que edad tienes? "))

#if edad < 18:
    #print("Hola usuario :3, usted es menor de edad")
#elif edad  >= 18 :
    #print("Hola usuario :3, usted es un adulto joven")
#else:
    #print("Hola usuario :3, usted es un adulto")

""" 
Tengo una duda aqui, yo intente poner un 
tercer elif con la informacion que tiene
el "else" en el codigo, armado de la
siguiente manera:

elif edad >= 30:
    print("Hola usuario :3, usted es un adulto")

Y lo que pasaba es que cuando se ejecutava el codigo,
el programa no ejecutaba esa linea, solo la que dice 
>= 18.

lo que intui sobre esto, es que como estaba usando 
un operador parecido o igual (> y >=), como que el 
programa o sistema no diferenciaba y solo 
ejecutaba el >=18. 

Correccion:
(La condicion ya se cumplia
por lo que al cumplirse la condicion, el programa
omite las otras variables. "Asegurate de crear
condiciones que se diferencien para que no pase esto")

"""
#Correccion (Reto 5) + mejora

#variable input(). type<'int'>
edad = int(input("Hola usuario :3. Que edad tienes? "))

#condicionales 
if edad < 18:
    print("Hola usuario :3. Es usted menor de edad")
elif 18 <= edad <= 30: #hacer esto, deja marcado el rango de edades de la condicion
    print("Hola usuario :3. Es usted un adulto joven")
else:
    print("hola usuario :3. Es usted un adulto")

""" 
En cada linea de codigo de la seccion de condicionales
consiste en comparar el dato almacenado en la variable
"edad" con las codiciones, de si es menor a, o mayor a.
y dependiendo de cual se cumple y cual no, va imprimir 
una frase en la terminal 

nota: Hay que realizar corractamente las condiciones
para que el programa se ejecute como queremos.
"""

#reto 6 (Validacion de entrada "input()" y comparacion)

"""
Se le pedira al usuario que nos diga su 
color favorito y lo vamos a comparar
para ver si es azul, o si es otro color.
"""

color = input("Hola usuario :3. Dinos cual es tu color favorito? ") #Variable input() type<'str'>

#Codicionales
if color.lower() == "azul":
    print("El azul tambien es mi color favorito <3")
else:
    print(f"{color.capitalize()} es un color muy bonito :3")

""" 
En la seccion de condicionales (if, else), 
a demas de que comparamos la informacion que 
nos da el usuario en la variable "color"
con las condiciones de si es igual a "azul"
se imprime un mensaje y si no, otro.

Tambien queria explicar la funcion 
"lower() y capitalize()" que estas en si, 
condicionan al texto introducido a ser de una 
manera especifica, en el caso de lower()
condiciona a el texto a estar siempre en 
minusculas, y capitalize() condiciona al 
texto introducido a que la primera letra
de la palabra o frase, siempre sea en 
mayuscula.
"""

#Reto 7 (reto creativo: Calculadora perzonalizada)

""" 
Haz un mini programa que:

1. Pida dos numeros 
2. Pida una operacion (+, -, *, /)
3. Devuelva el resultado 
"""
#Bienvenida
print("""
Bienvenido a tu calculadora personalizada :3.
Que operacion de gustaria hacer hoy?
""")

#Eleccion. variable input(), type<'str'>
op = input("""
suma: + ; resta: - ; multiplicacion: * ; division: / ?
Escoja colocando el simbolo de su operacion :3 
""")

num_1 = int(input("Ahora digame su primer numero al calcular :3 ")) #variable input(), type<'int'>
num_2 = int(input("Ahora digame el sugundo :3 ")) #variable input(), type<'int'>

#condicionales 
if op == "+":
    print("El resultado es:", num_1 + num_2)
elif op == "-":
    print("El resultado es:", num_1 - num_2)
elif op == "*":
    print("El resultado es:", num_1 * num_2)
elif op == "/":
    print("El resultado es:", num_1 / num_2)
else:
    print("Operacion no valida. Lo sentimo xP")

"""
Seccion de condicionales:
se encargan de que, en base a la eleccion del
usuario almacenada en las variables (op, num_1, num_2)
estas comprobaran si la eleccion del usuario 
cumple con las codiciones de cada "if, elif y else"
y en base a eso, realizara una operacion o otra.

nota: Quice hacer que el programa 
fuera mas interactivo, por eso puse mas
comentarios al usuario :3
"""

"""" 
Tengo una duda, en el ejercicio de ejemplo
del reto 7, en vez de poner "int()" en el
input que pide los numeros al usuario, pone
"float()" y no entiendo el por que. Puede 
que sea por que quiere que todos los 
valores numericos dados por el usuario
sean decimales? O por que estamos usando 
varias operaciones incluyendo "/"?
Tengo que solventar la duda.
"""