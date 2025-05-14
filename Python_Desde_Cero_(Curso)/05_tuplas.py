#Ejercicio 1

""" 
Crea una tupla con los valores
(10, 20, 30, 40, 50) e imprimila.
"""

my_tupla = (10, 20, 30, 40, 50) #variable type<'tuple'>

#imprime los elementos de "my_tupla"
print(my_tupla) #print((10, 20, 30, 40, 50))

""" 
En este ejercicio nos indican crear una tupla,
y puede que a simple vista, te preguntes que,
cual es la diferencia entre una tupla y una lista?
Bueno, siendo breves, una lista es un conjuntos de 
elementos los cuales podemos acceder a ellos o,
modificarlos a gusto, ya que una lista es "mutable".
En cambio una tupla, aun que en esta tambien podemos
acceder a sus elementos, no la podemos modificar a gusto
como una lista, ya que esta no es "mutable"
"""

#Ejercicio 2

""" 
Acccede al segundo elemento de la tupla
(100, 200, 300, 400, 500) y muestralo.
"""

tupla_0 = (100, 200, 300, 400, 500) #variable type<'tuple'>

#imprime el elemento seleccionado de la tupla
print(tupla_0[1]) #print(200)

""" 
En este ejercicio hacemos lo siguiente.
1. Creamos una tupla "(100, 200, 300, 400, 500)"
2. Y seleccionamos un elemento de esta, que 
en este caso es el segundo elemento "1" = 200
"""

#Ejercicio 3

""" 
Intenta modificar el primer elemento de la 
tupla (1, 2, 3) a 10 y observa el resultado
"""

#tupla_1 = (1, 2, 3) #variable type<'tuple'>

#modificamos unos de los elementos de la tupla
#tupla_1[0] = 10 #modificador

#imprime los valores de la tupla
#print(tupla_1) #TypeError: 'tuple' object does not support item assignment

""" 
Por que pasa esto? bueno como ya habiamos
\indicado mas arriba, las tuplas no son
mutabla, por lo que al intentar modificarlas
como si fuera una lista, nos marcara error, 
asi como vemos en la terminal.
"""

#Experimentacion

""" 
Si realemente queremos modificar unos de 
los elementos de la tupla, lo que podemos 
hacer es lo siguiente:
"""

tupla_1 = list((1, 2, 3,)) #variable "tupla". type<'list'>

#modificador de elemento
tupla_1[0] = 10

#imprime los elementos de tupla_1
print(tupla_1) #print([10, 2, 3])

""" 
Como vemos ahora, nuestra tupla ha sido
modificada, pero esta deja de ser una tupla.
Esta es una manera de que si realmente es 
necesario hacer esa modificacion.

Pero en la practica no es algo recomendable
ya que para eso estan los distintos tipos de
funciones y de datos, para que cada uno se 
encargue de algo en especifico. Pero no viene
mal saber como modificar un dato que es no mutable.
"""

#Ejercicio 4

""" 
Cuenta cuantas veces aparece el numero 3
en la tupla (1, 2, 3, 3, 4, 5, 3)
"""

tupla_2 = (1, 2, 3, 3, 4, 5, 3) #variable type<'tuple'>

#imprime la cantidad de un elemento
print(tupla_2.count(3)) #print(3)

""" 
En este ejercicio realizamos una tupla
con indices o elementos repetidos, y 
con la funcion count() le indicamos
que queremos saber cuantos "3"
(que en este caso se repite), hay en 
nuestra tupla.

Nota, algo que debemos de tener en cuenta 
es que debemos llamar nuestra funcion de 
una manera en especifico.

Yo intente hacerlo de verias maneras, ya que
al principio no me acordaba con exactitud como
hacer esta funcion.

1. Hice esto:

tuple_2.count[3]
print(tuple_2) #print(TypeError: 'builtin_function_or_method' object is not subscriptable)

Al hacer esto, nos marca un TypeError, ya que 
primero, los "[]" se usan mas que todo para 
editar, acceder y crear listas, y eso no es
lo que buscamos,

2. Hice esto:

tuple_2.count(3)
print(tuple_2) #print(1, 2, 3, 3, 4, 5, 3)

Al hacer esto, es como si la funcion fuera
invisible, el interprete la omite y lo que hace
es imprimirnos la tupla en si.

Mi conclusion de por que pasa esto es por que, 
al uno realizar esta funcion "count()" afuera 
del print() es como si la funcion no estuviera
declarada, y como es una funcion que nos da un
dato, esta al estar afuera del print no nos da 
el dato aun que la funcion si se haya aplicado.

Me lo imagino de esta forma. Digamos que tenemos
una variable, adentro de ella esta un dato que 
pedimos "3", la creamos y todo esta correcto
pero se nos olvido llamarla en el print() lo 
que nos deja sin este dato. Este caso es algo
parecido a este ejemplo. Puede que me este
equivocando, asi que, lo corregire y veremos 
si nuestro razonamiento es correcto.

3. La manera correcta:

print(tupla_2.count(3)) #print(3) es la cantidad de veces que se repite el elemento
"""

#Experimentacion

tupla_02 = (1, 2, 3, 3, 4, 5, 3).count(3) #variable type<'tuple'> con count()

#imprime la cantidad del indice repetido
print(tupla_02) #print(3)

""" 
Como podemos ver en este caso, lo hice 
juntando todo en la misma variable,
lo que hicimos funciona y tiene el mismo 
resultado, pero, puede que no sea lo mas 
ideal a la hora de querer aplicar una 
funcion a una tupla, ya que puede que 
nuestro codigo no sea vea limpio.

Pero es divertido ver las distinas manera
de hacer una misma funcion jeje
"""

#Ejercicio 5

""" 
Encuentra el indice de la primera 
aparicion de la cadena "python" en
tupla ("Java", "Python", "JavaScript", "Python").
"""

tupla_3 = ("Java", "Python", "JavaScript", "Python") #variable type<'tuple'>

#imprime el indice de "Python"
print(tupla_3.index("Python")) #print(1)

""" 
En este ejercicio usamos la funcion
"index()" para saber el indice de unos
de los valores que se encuentran en nuestra
tupla en este caso "Python".

Como ya sabemos el indice es la posicion
en la que se encuentra cada elemento de nuestra
lista o tupla, y como ya hemos comprobado
el indice de toda lista o tupla comienza
en 0 para arriba, siendo el 0 como el 1 cuando
uno cuenta normalmente, por eso el indice de
"Python" es el 1.
"""

#Ejercicio 6

""" 
Concatena dos tupla: (1, 2, 3,) y (4, 5, 6)
e imprime la tupla resultante.
"""

tupla_04 = (1, 2, 3) #variable type<'tuple'>

tupla_4 = (4, 5, 6) #variable type<'tuple'>

con_tupla = tupla_04 + tupla_4 #variable de concatenacion

#imprime la tupla resultante
print(f"Tupla resultante: {con_tupla}") #print(1, 2, 3, 4, 5, 6)

""" 
En este ejercicio, hicimos algo simple
realizamos dos tuplas, cada una en una 
variable diferente, para luego hacer una
variable que almacene la concatenacion de
las dos tuplas creadas, e imprimimos el 
resultado de la concatenacion con un f-string
para añadirle un comentario al imprimir el
resultado.
"""

#Ejercicio 7

""" 
Crea una subtupla con los elementos desde
la posicion 2 hasta la 4 (sin incluir la 4)
de la tupla (10, 20, 30, 40, 50).
"""

tupla_5 = (10, 20, 30, 40, 50) #variable type<'tuple'>

sub_tupla = tupla_5[2 : 4] #variable, slice de tupla_5, type<'tuple'>

#imprime el slice de tupla_5
print(sub_tupla) #print(30, 40) 

""" 
Como ya hemos visto en las listas el operador ":"
nos sirve para optener un pedazo de una lista o
tupla en base a los parametros que le indicamos.

Este operador nos ayuda a poder extraer lo que nos
pedian en el enuncido, por eso, creamos la tupla
y luego una variable en donde se va almacenar la
informacion que bucamos usando el operador ":" 
(sub_tupla) e imprimimos la variable.

Nota: Me gustaria agregar que, yo tenia la duda
sobre que era este signo ":" , yo sabia lo que hacia
pero no sabia determinar que era, al principio lo veia 
como una funcion, pero eso no tiene mucho sentido
ya que una funcion tiene nombre, la cual llamamos por
parentesis "()", entonce pense que, debe de ser un
operador, pero tenias mis dudas, asi que investigue y
si es un operador, ya que este signo ":" ya viene 
integrado en la sintaxis de python, por lo cual lo
convierte en un operador asi como "+, -, <" solo
que este solo se usa entre los corchetes como un
slicing. 

Por eso, como conclusion queria dejar esto:

Una funcion es algo que tiene nombre adentro del
lenguanje de programacion, la cual llamamos entre
los parentesis "()" para usarla

Un operador, es una herramienta que ya viene adentro
del lenguaje y se usan segun lo que requieren, en el 
caso de : (como slicing) se tiene que usar simpre 
entre [:] para que este funcione.
"""

#Ejercicio 8

""" 
Convierte la tupla ("rojo", "verde", "azul") en una lista,
y cambia el segundo elemento a "amarillo" y vuelve a 
convertirla en una tupla. Imprime la tupla resultante.
"""

tupla_6 = ("rojo", "verde", "azul") #variable type<'list'>

#imprime la tupla sin cambios
print(f"Tupla sin cambios: {tupla_6}") #print("rojo", "verde", "azul")

#se llama a tupla_6 y se aplica la funcion list() a tupla_6
tupla_6 = list(tupla_6) #variable type<'list'>

tupla_6[1] = "amarillo" #aplica el cambio al 2do elemento

#cambia el dato de la variable con la funcion tuple()
tupla_6 = tuple(tupla_6) #variable type<'tuple'>

#imprime la tupla con los combios realizados
print(F"Tupla con cambio: {tupla_6}") #print("rojo", "amarillo", "azul")

""" 
En este ejercicio aplicamos algo de lo que
hablamos en el ejercicio 3, en donde
explicamos como seria posible combiar
un elemento de una tupla al ser esta 
inmutable.

En este caso lo que hicimos fue crear nuestra
tupla, pero en vez de aplicarle la funcion 
list() ahi mismo donde esta la tupla, quise que 
se diferenciara una tupla de la otra, y por eso
aplique la funcion list(), llamando la variable
tupla_6 y aplicarle la funcion list() y asi hacer
el cambio, luego de eso volver a convertir en tupla
la variable y asi imprimir la tupla (tupla_6) con 
los cambios que realizamos, asi como vemos en el 
codigo.

Nota: algo que me gustaria agregar, es que al hacer 
esto, hay que asegurarnos de aplicarle la funcion
list(), en este caso, a la variable llamandola y 
aplicarle el cambio.

Para que se me entienda, yo hice esto:

tupla_6 = ("rojo", "verde", "azul")

tuplist = list(tupla_6)

tupla_6[1] = "amarillo"

list_tup = tuple(tupla_6)

print(tuple_6) #print(TypeError: 'tuple' object does not support item assignment)

Obviamente esta mal.

1. al cree una variable (tuplist) en donde 
adentro de esta aplique el cambio a la 
variable principal (tupla_6)

2.le aplico al indice que quiero el cambio

3. Creo otra variable en donde le aplico
la funcion tuple() a la variable principal
"tupla_6" 

4. imprimo la variable principal.

Y bueno, esto esta mal, es evidente, ya
que estamos usando demasiadas variable,
aun que adentro de ellas aclaramos que
el cambio es para la principal (tupla_6),
pero al hacer esto, es como si estuvieramos
hablando claramento, te digo que quiero "x"
pero eso esta adentro de otro nombre que 
no conocemos, y sucesivamente vamos cambiando 
el contexto principal, que es la primera 
variable declarada (tupla_6), todo mal... xD

La moraleja que quiero dejar en este ejercicio es
que es mejor trabajar de manera simple y clara,
sin nublar nuestro codigo haciendolo confuso,
declaramos una variable, y queremos aplicar varios
cambios asi que trabaja con la misma variable.

Aun que pudieramos hacer que todo ese engorro funcione
no es optimo, y hace nuestro codigo deficiente ya que 
este debe de ser claro y legible. Al final trae confuciones
y es mas propenso a errores, y tambien por eso, hacer 
estas practicas como hacer el cambio de dato de una
lista o tupla, no es lo mas optimo ya que tenemos que ser
cuidadosos con la menera en que se hace, se puede hacer, si,
siempre que sea algo muy necesario, pero no es lo mejor.

conslusion: Crea un codigo simple y limpio, donde los parametros
de lo que quieres hacer esten claro, simple no significa que no
sea complejo, significa un buen manejo y 
entendimiento, haciendo que a la hora de trabajar en equipo todos
entiendan lo que se esta haciendo.
"""

#Ejercicio 9

""" 
Elimina una tupla llamada my_tuple usando del
y luego intenta imprimirla para ver el resultado.
"""

my_tuple = ("jheremy", 21, "España") #variable type<'tupla'>

#imprime la tupla
print(f"Se imprime la tupla: {my_tuple}") #print("jheremy", 21, "España")

#del(my_tuple[0]) #TypeError: 'tuple' object doesn't support item deletion

del(my_tuple) 

#print(my_tuple) #print(NameError: name 'my_tuple' is not defined. Did you mean: 'my_tupla'?)

""" 
Lo que pasa en el caso de usar la funcion del()
con una tupla es que, esta al ser inmutable no
permite eliminar uno de los elementos de esta,
señalando el indice en la funcion, al contrario
de las listas, que si son mutable. Asi que si 
queremos usar la funcion del() en tuplas, solo
nos permite elmininar la variable tupla entera, 
haciendo que a la hora de imprimirla esta no 
exista
"""

#Comparacion con list

my_list = ["jheremy", 21, "España"] #variable type<'list'>

#imprime my_list
print(f"Se imprime la lista: {my_list}") #print(["jheremy", 21, "España"])

#funcion que elimida un elemento de la lista
del(my_list[1])

#imprime la lista modificada
print(my_list) #print(['jheremy', 'España'])

#usando asi la funcion del(), elimina la variable "lista"
#del(my_list)

#print(my_list) #print(NameError: name 'my_list' is not defined)

#Ejercicio 10

""" 
Crea una tupla con un solo elemento, 
(el numero 100) e imprimela. Asegurate
de usar la sintaxis correcta para 
crear una tupla con un solo elemento.
"""


tupla_7 = (100,)

print(type(tupla_7))
print(tupla_7)