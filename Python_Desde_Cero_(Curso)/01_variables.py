#Ejercicio 1

name = "Jheremy" #se creo una varial con valor <'str'>
age = 21 #se creo una variable con valor <'int'>
height = 1.82 #se creo una variable con valor <'float'>

print(name)
print(age)
print(height)

""" 
se ha impreso en el terminal 
cada una de las variables
"""

#Ejercicio 2

age = str(age)

print(f"cuantos años tengo = {age}")
print("Dime tu edad. Tengo " + age + " años de edad")
print(type(age))

""" 
A pesar de que mi primer ejemplo esta bien
no lo hice la manera mas eficiente. 
Era mejor forzar el tipo de dato de una vez
en el print, como se ve en la correccion
"""

#Correccion

#se usa un f_string para concatenar
print(f"tengo {str(age)} años de edad") 

#Ejercicio 3

is_student = True #se creo una variable con valor <'bool'>
#se imprime la variable
print(is_student) #true. <'bool'>

#Ejercicio 4

#se creo una variable type<'str'> (full_name)
name_2 = "Jheremy De Jesus Villafranca Seijas"
#se impriome la variable con el operador 'len()'
print(len(name_2))

""" 
len() Consiste en contar los caracteres
o valores de una variable
"""

#Ejercicio 5

#se crearon tres variables en una linea
name_3, la_name, city_n = "Jheremy", "Villafranca", "El Tigre"
#se imprimio las variables type<'str'>
print("Mi nombre es " + name_3 +" " + la_name + " y vengo de " + city_n)

#Ejercicio 6

#se creo una variable con un input
color = input("dime tu color favorito ") 
#se imprime el valor que le dio el usuario a la variable (color)
print(f"Que lindo color, tambien me gusta el color {color} <3")


""" 
El operador o funcion imput, consiste en 
realizarle una peticion al usuario para
que escriba en la terminal y ese valor
se le otorga a la variable que tiene el 
input.
"""

#Ejercicio 7

fruit = "banana" #variale <'str'>
#se  imprime la primera version de la variable
print(fruit)

fruit = "sandia"#change variable <'str'>
#se imprime la nueva version de la variable
print(fruit)

#Ejercicio 8

price = 12.5 #variable type<'float'>
#se imprime la variable cambiando su dato a <'int'>
print(int(price))

""" 
Lo que pasa o se busca demostras es que
python es un lenguaje de tipado debil o
flexible. Tu declaras una variable de un
tipo de dato y si la vuelves a declarar
con otro dato o valor, al final se va 
cambiar sin problema.
"""

#Ejercicio 9

#variable type<'str'>
address_len = "calle benito 16, Madrid"
#se imprime laa variable con el operador len()
print(len(address_len))

#Coreccion

address = "calle benito 16, Madrid"
address_len = len(address)
print(address_len)

#Ejercicio 10

#se forza el tipado de la variable "phone"
phone: int = 9999999999
phone = 19.2 #se cambia el dato a <'float'>
#se imprime con la funcion type
print(type(phone))

""" 
En mi ejemplo quise hacer ver que 
aun que fuerce el tipado en una variable
con declarar la variable otra vez con 
otro valor o dato, y este se va cambiar.
"""

#Correccion

phone: int = 99999999
print(type(phone))

phone = 919191919
print(type(phone))

""" 
Este es el resultado "correcto"
pero yo no lo entiendo el por que
de este.
"""
