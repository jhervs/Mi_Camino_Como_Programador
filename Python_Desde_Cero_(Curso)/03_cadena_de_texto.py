#Ejercicio 1

""" 
Declarar una variable text con la
frase "aprendiendo python", y muestra
el resultado en una sola linea.
"""
text = "Aprendiendo python" #variable type<'str'>

#imprime la longitud del texto
print(f"La longitud de la variable 'text' es: {len(text)}")

#Ejercicio 2

""" 
Concatena dos cadenas: hola y python
y muestra el resultado en una sola
linea.
"""

c_a = "hola" #variable type<'str'>
c_b = "python" #variable type<'str'>

#imprime la concatenacion
print(f"Concatenacion: {c_a} {c_b} ")

#Ejercicio 3

""" 
Crea una cadena que incluya un salto
de linea, y luego imprimela para ver
el resultado.
"""

print("Tengo sueño, neccesito una gran siestita u-u \n Y hoy justo se fue la luz en Madrid. \n ha sido un dia agotador...")

"""imprime una cadena teniendo
saltos de linea con la funcion "\n"
"""
#Ejercicio 4

""" 
Usa el formateo de cadena con
f-string para imprimir tu 
nombre, apellido, y edad en una 
cadena de texto.
"""

name = "Jheremy" #variable type<'str'>
surname = "Villafranca" #variable type<'str'>
age = 21 #variable type<'int'>

#imprime cada variable con un f-string
print(f"Hola mi nombre es {name} {surname} y tengo {age} años")

#Ejercicio 4.1 (Usando format())

#variables en una linea 
name, surname, age = "Jheremy", "Villafranca", 21 #type<'str'>

#se imprime las variables usando la funcion format()
print("Hola mi nombre es {} {} y tengo {} años".format(name, surname, age ))

#Ejercicio 5 

""" 
Desempaqueta los caracteres de la palabra 
python en variables separadas y luego 
imprimelos uno por uno
"""

word = "python" #variable type<'str'>

#desempaquetado de variable "word"
a, b, c, d, e, f = word

print(a) #print(p)
print(b) #print(y)
print(c) #print(t)
print(d) #print(h)
print(e) #print(o)
print(f) #print(n)

""" 
El desempaquetado consiste en separar 
cada valor o letra (en este caso)
para asi tener acceso a ellas y poder
imprimirlas, como es en este ejemplo
se desempaqueto la palabra python
en cada una de las letras que tiene
y asi poder imprimirlas por separado 
"""

#Ejercicio 6

""" 
Extrae un slice de la palabra programacion
para obtener los caracteres desde la posicion
3 hasta 7
"""

word_2 = "programacion" #variable type<'str'>

pedazo = word_2 [3:8] #variable divisora, type<'str'>

#imprime un slice de la variable "word_2" ([3:7])
print(pedazo)

""" 
Nota: En el ejercicio nos
piden los indices del 3 al 7
antes de corregir habia puesto
[3:7] pero lo que pasa es que 
al hacer eso no se estaba 
mostrando el indice 7 si no
hasta el 6, por lo que al hacer
este tipo de ejercicio hay que 
tener en cuenta esto y sumarle
1 mas al valor de la derecha
asi ([3:8])

"""

#Ejercicio 7

""" 
Invierte la cadena "python" usando 
slicing y muestra el resultado 
"""

reversed_word = word[::-1] #variable con reversa, type<'str'>

#imprime la variable word pero alreves
print(reversed_word) #print(nohtyp)

""" 
Apesar de entiendo la funcion 
no entiendo muy bien como 
funcionan los numeros que van
junto con la funcion (::). Se
que son los que indican el
pedazo que se esta agarrando de
la cadena pero, no lo tengo claro
"""

#Ejercicio 8

""" 
Convierte la cadena "aprendiendo python"
en mayusculas usando el metodo adecuado
e imprimela.
"""

word_3 = "Aprendiendo python" #variable type<'str'>

#imprime la variable word_3 en mayusculas
print(word_3.upper()) #print(APRENDIENDO PYTHON)

""" 
En este ejercicio concistia en 
usar la funcion upper() para 
convertir la variable word_3
en mayusculas.

Nota: Tenemos que asegurarnos de
colocar primero la variable o
dato, y despues se coloca la 
funcion que le queremos aplicar
ejemplo:

word_3.upper()
"""

#Ejercicio 9

count_word = word_3.count("n") #variable type<'str'> con contador
#imprime lo indicado en la funcion .count()
print(count_word) #print(3)

""" 
Lo que hace la funcion "count()"
es contar valores. como en este caso 
que le indicamos que nos contara
cuantas "n" habia en la frase
Aprendiendo python, siendo la 
respuesta = 3
"""
#Ejercicio 10

""" 
Verifica si la cadena "12345"
es numerica usando el metodo
adecuado e imprimir el resultado.
"""

cadena = "12345" #variable type<'str'>

#imprime True o False, si la variable es numerica o no
print(cadena.isnumeric())

""" 
La funcion "isnumeric()" consiste
en indicarnos con (True o False)
si la variable es valor numerico
o no.
"""

