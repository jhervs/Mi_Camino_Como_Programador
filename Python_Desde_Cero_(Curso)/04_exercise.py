#Ejercicio 1

""" 
Crea una lista con los numeros del
1 al 5 e imprimela.
"""

list_1 = [1, 2, 3, 4, 5] #variable type<'list'>

#imprime la lista creada
print(list_1) #print([1, 2, 3, 4, 5])

#Ejercicio 2

""" 
Accede e imprime el tercer elemento 
de la lista [10, 20, 30, 40, 50].
"""

list_2 = [10, 20, 30, 40, 50] #variable type<'list'>

#imprime el tercer elemento de la lista
print(list_2[2]) #print(30)

""" 
En esta parte del ejercicio hicimos
lo siguiente:

1. Creamos nuestra lista adentro de 
una variable (list_2)

2. En la funcion print() hicimos esto
"print(list_2[2])"

Esto, lo que hace es que le decimos
al interprete que queremos que de 
nuestra lista, nos de el tercer elemento.
Puede que se pregunten, pero por que hay 
un "2", bueno, lo que pasa es que, en los 
lenguajes de programacion los elementos o
indices se cuentan a partir del "0",
por lo que el primer elemento es el 0
el segundo el 1 y el tercero el 2, y asi
sucesivamente.

Nota: es importante que cuando queramos
llamar un elemento o indice de la lista
este en casille en corchetes "[]"
"""


#Ejercicio 3

""" 
Agrega el numero 6 al final de 
la lista [1, 2, 3, 4, 5] e imprimela
"""

#list_1.insert(6, 6) #funcion insert()

#imprime la lista (list_1)
#print(list_1) #print([1, 2, 3, 4, 5, 6])

""" 
En este ejercicio se usa la funcion insert()
para agregar un sexto elemento a nuestra 
lista (list_1).

Nota: Es importante que la accion que queremos
realizar se ponga entre parentesis

Duda: Puede que sea una pregunta absurda,
pero me pregunto que diferencia el uso de 
() y [] en los lenguajes de programacion
en este caso python? Me lo pregunto mas 
que todo es para tener claro cual se usa
en cierta situaciones y el por que?
No quiero solo suponer por que si.

Respuesta a duda:

| Símbolo | Se usa para...                 | Ejemplo                       |
| ------- | ------------------------------ | ----------------------------- |
| `[]`    | **Listas** y acceso por índice | `lista[0]` → primer valor     |
| `()`    | **Funciones** y **tuplas**     | `print("Hola")` – `(1, 2, 3)` |

🧠 Resumen:

() se usa para llamar funciones (print(), append(), etc.) o definir tuplas.

[] se usa para crear listas, acceder a posiciones,
o modificar datos dentro de listas.
"""
#Correccion 

list_1.append(6) #funcion append

#imprime los valores de list_1
print(list_1) #print([1, 2, 3, 4, 5, 6])

""" 
A pesar en el primer intento de este
ejercicio funciono correctamente,
es preferible usar la funcion append(),
ya que el elemento que le ingresemos 
lo agragara al final de la lista sin necesidad
de llamar la posicion de la lista, y asi 
evitamos que haya errores o confuciones
a la hora de corregir y editar, tambien
con la funcion append() el codigo es mas legible
"""

#Ejercicio 4

""" 
Inserta el numero 15 en la posicion 2 
de la lista [10, 20, 30, 40, 50].
"""

list_2.insert(1, 15) #funcion insert()

#imprime la lista (list_2)
print(list_2) #print([10, 15, 20, 30, 40, 50])

#Ejercicio 5

""" 
Elimina el primer valor 30 de la
lista [10, 20, 30, 30, 40, 50].
"""

list_3 = [10, 20, 30, 30, 40, 50] #variable type<'list'>

list_3.remove(30) #funcion remove()

#imprime los elementos de list_3
print(list_3) #print([10, 20, 30, 40, 50])

""" 
Este ejercicio es parecido al ejercicio
donde usamos la funcion insert(), pero
en vez de ingresar un elemento, estamos
removiendo un elemento de la lista  usando
la funcion remove()

Nota:Esta funcion elimina la primera 
ocurrencia (aparicion) del elemento
indicado en la funcion.
"""

#Ejercicio 6

""" 
Usa la funcion pop() para eliminar
el ultimo elemento de la lista 
[1, 2, 3, 4, 5] y almacenalo en una nueva
variable. Imprime la variable y la lista
"""
list_0 = [1, 2, 3, 4, 5] #variable type<'list'>

#list_0.pop() #funcion pop()

#imprime los valores de "list_0"
#print(list_0) #print([1, 2, 3, 4])

#my_pop = list_0.pop() #variable type<'int'>

#imprime el valor de la variable my_pop
#print(my_pop) #print(4)
#print(list_0) #print([1, 2, 3])

"""
En este ejercicio usamos la funcion pop(),
que realiza la funcion de remover o eliminar
"el ultimo elemento de nuestra lista".

Tambien almacenamos el valor eliminado en 
una variable "my_pop".

Dudas: Yo al realizar el ejercicio estuve
intentando que el elemento que apareciera
en la variable my_pop fuera el numero "5",
que es el elemento "4", pero no sucede asi, 
y me aparece el numero 4. Mi conclusion de 
esto es que al yo volver a nombrar en mi 
variable my_pop lo hecho en la linea anterior 
(list_0.pop()) como que se vuelve a repetir 
esta funcion eliminando otra vez el ultimo 
elemento del resultado anterior ([1, 2, 3, 4])
y asi dandome 4 en vez de 5.

No se si mi conclusion estara equivocada pero
eso es lo que pienso por ahora de esto.

Mi conclusion es acertada, pero mi codigo
tiene un fallo ya que no cumple con lo que 
trato de hacer y es por la repeticion de la
funcion pop()
"""

#Correccion

my_pop = list_0.pop(4) #variable type<'int'>, funcion pop()

#imprime los valores de list_0
print(list_0) #print([1, 2, 3, 4, 5])

#imprime el valor removido de list_0
print(my_pop) #print([5])

""" 
Ya ahora como moraleja, sabemos
que si repetimos una funcion dos
veces en el codigo que afecta a una
sola variable, esta sera modificada
dos veces por las funciones (pop())
aun que es algo un poco obvio jeje.

Lo importante es aprender de los errores 
y corregirlos para seguir avanzando :3
"""

#Ejercicio 7

""" 
Invierte la lista [100, 200, 300, 400, 500]
e imprimela 
"""
#Intento 1

list_4 = [100, 200, 300, 400, 500,] #variable type<'list'>

#imprime los elemento de la svariable list?
print(list_4.reverse()) #print(None)

""" 
En este primer intento yo intente 
usar ya de una vez la funcion reverse()
adentro del print() pero, no sucede lo 
que esperaba...

Yo lo que busco hacer es que los elementos
de mi variable list_5 se inviertan y se impriman, 
pero no sucede. Pienso que es por que al yo
introducir la funcion reverse() adentro del print()
la funcion print me exige definir la funcion reverse, 
y decir que es lo que quiero hacer con la funcion reverse, 
y por eso el print me dice (none), Ya que la funcion reverse()
no arroja ningun resultado, solo modifica la lista
"""

#Correccion 

list_4 = [100, 200, 300, 400, 500,] #varible type<'list'>

#se le aplica la funcion reverse()
list_4.reverse()

#imprime los elementos de la list_4
print(list_4) #print(500, 400, 300, 200, 100)

""" 
En este caso, aplicamos la funcion reverse()
primero a la variable list_4, para que esta se 
modifique, y luego la imprimimos con print()
y asi podremos ver en nuestra terminal la 
modificacion que hizo la funcion reverse()
a la variable "list_4"
"""

#Ejercicio 8

""" 
Oderna la lista [3, 1, 4, 2 5]
en orden ascendente e imprimela
"""

list_5 = [3, 1, 4, 2, 5] #variable type<'list'>

#se imprime los elementos de list_5
print(f"Se imprime la lista desordenada {list_5}") #print([3, 1, 4, 2, 5]) "desornados"

#se le aplica la funcion sort() a "list_5"
list_5.sort() #funcion sort() "ordena de manera acendente"

#imprime los elementos de list_5
print(f"Se imprime la lista ordenada {list_5}") #print([1, 2, 3, 4, 5]) "ordenados"

""" 
En este ejercicio, usamos la funcion sort()
para ordenar de manera acendente los elementos
o indices de la lista "list_5" 
"""

#Experimentacion 

va = [5, 3, 7, 1, 6, 2, 4] #variable type<'list'>

print(va.sort()) #print(None)

print(va.append(8)) #print(None)

""" 
Lo que trataba de comprobar es que 
cuando se usan funciones que modifican
la lista, estas se tiene que aplicar
primero a la lista, para despues
imprimirla, ya que si no se hace asi,
y se aplica directamente en el print(),
no de va arrojar resultado ya que estas
solo modifican la lista. Es como si
el print no supiera que la lista fue 
modificada y dice que no hay nada (None)
"""

#Ejercicio 9
""" 
Concatena las listas [1, 2, 3,]
y [4, 5, 6] y almacena el resultado
resultante.
"""

list_01 = [1, 2, 3] #variable type<'list'>
list_02 = [4, 5, 6] #variable type<'list'>

#variable de concatenacion
conca_list = list_01 + list_02 #variable type<'list'>

#imprime los elementos de la variable "conca_list"
print(conca_list) #print([1, 2, 3, 4, 5, 6])

""" 
En este ejercicio lo que hicimos fue 
crear dos listas, para despues 
concatenarlas en una variable (conca_list)
y asi imprimir el valor resultante de la
union de estas dos listas :3
"""

#Ejercicio 10

""" 
Crea una sublista con los elementos 
de la lista [10, 20, 30, 40, 50]
que van desde la posicion 1 hasta
la 3 (sin incluir la posicion 3).
"""
list_03 = [10, 20, 30, 40, 50] #variable type<'list'>
sub_list = list_03[0 : 3] #variable type<'list'>

#imprime los elementos de sub_list
print(sub_list) #print([10, 20, 30])

""" 
En este ejercicio lo que intui que queria
en base al enunciado, es que de la lista
[10, 20, 30, 40, 50] extrayeramos tres 
elementos de esta (del 1 al 3).

Para eso usamos una herramienta del 
lenguaje que nos ayude a dividir un 
pedazo de nuestra lista (:)
y le indicamos que quieria los elementos 
desde el 0 al 3.

En esta parte yo me quede un poco dudoso
ya que, yo lo haria asi a la primera
"list_03[0 : 2]" pero lo que pasa al hacer
esto es que al imprimer ese slice que indicamos
solo nos arroja dos elementos "[10, 20]",
ya que, como ya vimos en el 03_exercise,
hay que sumarle un numero mas al elemento
que pedimos en la derecha "[0 : 3]" para
que nos de los elementos que queremos.

Puede que te preguntes por que pasa esto?

Y bueno, yo concluyo que es por que 
el interprete al tu pedirle esto:

quiero que de esta lista [10, 20, 30, 40, 50]
me des los tres primeros elementos "[10, 20, 30]"
y como sabemos el primer elemento es 0,
tu haces esto [0 : 2], pero al hacer esto
el interprete te va a dar solo dos elementos
[10, 20] ya que esta no cuenta el elemento 2
que se indico, y por eso se le tiene que sumar
uno mas, para que te de el tercer elemento [0 : 3].

Por los momentos esa es mi conlusion antes de
hacer la correcion de todo.
"""