#Ejercicio 1

suma = 15 + 25 #variable type<'int'> con op "+"
resta = 50 - 22 #variable type<'int'> con op "-"
multiplicacion = 8 * 7 #variable type <'int'> con op "*"
division = 100 / 20 # variable type<'float'> con op "/"

#se imprimio cada variable en un f_string
print(f"la suma es {suma}, la resta es {resta}, las multiplicacion es {multiplicacion} y la division es {division}")

""" 
Nota: puede que quede la duda de por que
el operador de "/" es de tipo float?
Me puse a probar y siempre da como resultado 
valores de tipo float, mi conclusion es,
por que este tipo de dato maneja decimales,
por ende, aun que el resultado deberia de ser entero,
este operador siempre arroja decimales.
"""

#Ejercicio 2

divi = 37 % 5 #variable type<'int'> 
remainder = divi #variable. Almacena el resultado de "divi"

#se imprime la variable con el resultado 
print(f"El resto de nuestra division es {remainder}")

""" 
A mi al principio me confundio mucho este 
operador, pero es muy sencillo. El operador
modulo ('%') consiste en darte el restante de
una divicion. Por ejemplo: Tenemos (5/2) 
en la tabla de multiplicar del 2 , el 2 no tiene 5
pero el que mas se le acerca es el 2 * 2 = 4
por ende modulo nos da el valor que nos falta para
llegar a "5" que es "1"
"""

#Ejercicio 3

num = 7 #variable type<'int'>

#se concatena el valor de "num" cambiando su tipo a "str"
print(f"Este es mi numero favorito {str(num)} :3")

""" 
Se le cambia el tipo de dato a "num" ya que
las concatenaciones solo se pueden hacer 
con datos de tipo "str".
"""

#Correccion 

num = 7
conversion = str(7)

print("Este es mi numero favorito " + conversion + " :3")

""" 
Nota: Ambas versiones estan bien, pero el detalle es que 
en el f_string no es necesario usar en su linea el "str()"
ya que el f_string ya hace la conversion del dato "int".
"""

#Ejercicio 4

word_r = "python " * 10 #variable type<'str'> con operador "*"

print(word_r)

""" 
Se uso el operador "*" para que nuestro "str" 
se multiplique por 10 (En este caso) dando
como resultado que "python" se imprima 10 veces
"""

#Ejercicio 5

a = 12 #variable type<'int'>
b = 8 #variable type<'int'>

resultado = a > b #variable de operacion type<'bool'>

#se imprime el resultado de la operacion 
print(f"El resultado de nuestra comparacion es {resultado}")



#Ejercicio 6

fruit_1 = "apple" #variable type<'str'>
fruit_2 = "banana" #varible type<'str'>

compa_1 = fruit_1 > fruit_2 #print(False)
compa_2 = fruit_1 < fruit_2 #print(True)
compa_3 = fruit_1 == fruit_2 #print(False)
compa_4 = fruit_1 >= fruit_2 #print(False)
compa_5 = fruit_1 <= fruit_2 #print(True)

#se imprimen cada una de las variables 
print(f"Los valores de nuestra comparacion son: {compa_1}, {compa_2}, {compa_3}, {compa_4}, {compa_5} ")

#Ejercicio 7

c = 10
d = 5
e = 20

op = c > d and c < e #operacion type<'bool'> con operador "and"

#se imprime la operacion
print(f"Nuestra operacion comparativa dio como resultado {op}")


""" 
El operador "and" sirve para comparar dos
operaciones, como en este caso, pero este
da True solo si ambas parte son verdaderas.
"""
#Ejercicio 8

op_2 = 7 < 3 or 7 > 5 #variable type<'bool'> con operador "or"

#se impriome la operacion 
print(f"La comparacion es {op_2}")

""" 
En el caso del operador "not" . A este 
le basta con que solo haya uno cierto
para decirte True
"""

#Ejercicio 9

op_3 = not(15 > 20) #variable type<'bool'> con una negacion

#se imprime la operacion 
print(f"El resultado de la negacion es {op_3}")

""" 
En el caso del "not" este sirve para negar
lo que esta pasando en la operacion. Que 
quiere decir, si tengo una operacion donde 
digo que 15 es mayor que 20 y uso el operador
"not" este me dira que es True, ya que estamos
diciendo que lo que estoy haciendo no es verdad,
pero sin el "not" me dira que es False ya que 15 
no es mayor a 20.
"""

#Ejercicio 10

op_4 = (5 * 3) + 2 #variable operacional type<'int'>

result = op_4 > 10 and op_4 < 20 #variable comparativa type<'bool'>

#se imprime el resultado de la operacion comparativa
print(f"El resultado de nuestra operacion es {result}")
