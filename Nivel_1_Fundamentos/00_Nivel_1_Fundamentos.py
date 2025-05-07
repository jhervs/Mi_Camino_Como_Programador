#reto 1

""" 
crea dos variables: una con tu comida favorita
y otra con tu bebida favorita. Concatenalo con 
+ y un F_string (f"").
"""

comida = "shawarma" #variable type<'str'>
bebida = "aquarius" #variable type<'str'>

#variable con concatenacion type<'str'>
pedido = "Voy a pedir un " + comida + " con un " + bebida + " para beber"

#se imprimio la variable pedido
print(pedido)

#se imprimio las variable comida y bebida en un F_string
print(f"Voy a pedir un {comida} con un {bebida} para beber")

""" 
En este primer reto, quise poner dos ejemplo 
de como hacer lo mismo, en una almacene los
valores de las variable comida y bebida en la
variable pedido concatenandolas junto con 
una frase. Y en el otro ejemplo hice una 
concatenacion de las dos variable ya 
mencionas en un f_string :3.
"""

#Reto 2

""" 
Crea dos variable ('str') y has 
una frase con las dos variables
"""

animal = "gato" #variable type<'str'>
color = "negro" #variable type<'str'>

#se imprime las dos varibles concatenandolas con un f_string
print(f"tengo un {animal} {color} muy lindo <3")


#Reto 3

""" 
Solicita al usuario su nombre
con input() y guardalo en una 
variable y has una frase con 
su nombre
"""
#se le pide al usuario con un input() su nombre

name = input("Dime cual es tu nombre? :3 ") #variable input(). type<'str'>

#se imprime el valor de name con una frase
print(f"Hola {name}! Espero que estes teniendo un lindo dia <3")

#Reto 4

""" 
Pide dos datos al usuario con input()
como su edad y su color favorita y
crea una frase con las variables
"""

edad = input("Que edad tienes? ") #variable input(). type<'str'>
color_f = input("Cual es tu color favorito ") #variable input(). type<'str'>

#se imprime concatenando las dos variables
print(f"Ooh! tienes {edad} años y te gusta el color {color_f}, muy lindo color <3")

""" 
Puede que al ver la variable edad
surjan dudas ya que ingresamos un 
valor int, y yo coloque es es de 
tipo str. Lo que pasa es que en el
input todo lo que tu ingreses en el
sale como "str", por eso si uno 
necesita el valor int, hay que hacer
una conversion de datos.
"""

#Reto 5

""" 
Declara dos variable numericas con
valores enteros, realiza una suma y
luego imprimes su resultado y su tipo
"""

a = 6 #variable type<'int'>
b = 10 #variable type<'int'>
op = a + b #print(16) type<'int'>

#se imprime la variable "op"
print(f"El resultado de la operacion es {op}")
#se imprime el tipo de dato de la variable "op"
print("El tipo de dato de nuestra operacion es ", type(op))

#reto 6

""" 
"Calculadora para usuarios"
1. Pide al usuario que iingrese dos numeros con input()
2. Convierte esos valos en enteros con 'int()'
3. sumalos
4. imprime
"""
#imprimi una cadena de texto con la funcion \n (bienvenida al usuario)
print("Hola Usuario, bienvenido a tu calculadora personal.\nQue quieres calcular hoy? <3")

"""
La funcion \n consiste en saltar de linea,
a que me refiero? A que desde que inicia
la funcion (Que), hasta que termina el
string (hoy?), todo ese pedazo de string
se va a mostrar en el terminal abajo de la 
linea principal del string (string = texto).

"""

u_num_1 = int(input("Dime, cual va ser tu primer numero? ")) #variable input() con int(). type<'int'>
u_num_2 = int(input("Cual va ser tu segundo numero? ")) #variable input() con int(). type<'int'>

op_1 = u_num_1 + u_num_2 #variable operacional

#se imprime la variable "op_1"
print(f"Estes es el resultado de tu operacion {op_1}")
#se imprime el tipo de dato de la variable "op_1"
print("Operacion de", type(op_1))

""" 
Aqui se pone en practica lo que mencione
en el reto 4, donde tenemos que usar
un conversor de dato "int()" para hacer
que los valores numericos salga de tipo 
"int" y asi poder realizar la operacion
que teniamos realizar.
"""

#Reto 7

""" 
Crea un programa que le pida al usuario:
1. Su nombre
2. Su edad
3. Su Color Favorito
4. Una ciudad que sueñe con visitar
"""
#bienvenia al usuario
print("Hola usuario. Empecemos a editar tu perfil ") 

name_1 = input("Dime cual es tu nombre usuario? :3 ") #variable input(), type<'str'>
edad_1 = input(f"Cuantos años tienes {name_1}? ") #variable input(), type<'str'>
color_fa = input(f"Tambien me gustaria saber cual es tu color favorito {name_1}? ") #variable input(), type<'str'>
city = input(f"Y cual es la ciudad con la que sueñas visitar {name_1}? ") #variable input(), type<'str'>

#se imprime la introduccion
print(f"Hola {name_1} <3. veo que tienes {edad_1} años :3")
#se imprime la cortecia
print("Es un placer para mi conocerte y saber mas de ti.")
#se imprime la conclusion
print(f"Sueñas con visitar {city}, eso es genial! <3")

""" 
En la parte final de este reto
dividi en tres parte la frase en
varior print(). Tengo la duda de si
habra una manera de hacer eso sin
usar tres veces el print()?
"""

#Respuesta

print(f"""
Hola {name} <3. Veo que tienes {edad_1} años :3,
es un placer conocerte y saber mas de ti ;3
sueñas con visitar {city}, eso es genial!! <3
""")
