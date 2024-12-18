"""

Tipos de datos avanzados

---------------------------------------------------------

Listas   [] Datos ordenados y modificables

Las listas en Python, representadas por el tipo list, son colecciones ordenadas y mutables de
elementos que pueden ser de diferentes tipos de datos. Se definen utilizando corchetes [. . . ] y
permiten almacenar, acceder, modificar y eliminar elementos de forma flexible.


a = [1,2,3]
b = [4,5,6]
c = a + b

print(f"el valor de a es :{a} y el tipo es {type(a)}")
print(f"el valor de b es :{b} y el tipo es {type(b)}")
print(f"el valor de c es :{c} y el tipo es {type(c)}")




lista = [5,5.34,2+2j,True,"manzana"]
print(f"El tipo de la lista es : {type(lista)}")
print(f"El primer elemento es : {lista[0]} y su tipo es :{type(lista[0])}") #las listas empiezan a partir de 0
print(f"El segundo elemento es : {lista[1]} y su tipo es :{type(lista[1])}")
print(f"El tercero elemento es : {lista[2]} y su tipo es :{type(lista[2])}")
print(f"El cuarto elemento es : {lista[3]} y su tipo es :{type(lista[3])}")
print(f"El quinto elemento es : {lista[4]} y su tipo es :{type(lista[4])}")


------------------------------------------------------------------------------------


Tuplas  ()   Datos ordenados y  no modificables

Las tuplas en Python, representadas por el tipo tuple, son colecciones ordenadas e INMUTABLES
de elementos que pueden ser de diferentes tipos de datos. Se definen usando paréntesis (. . . ) EN LUGAR DE CORCHETES y,
una vez creadas, sus elementos no pueden ser modificados ni eliminados.

Ejemplo de uso de variables de tipo tuple


a = (1,2,3)
b = (4,5,6)
c = a+b
print (f"El valor de a es: {a} y el tipo es {type(a)}")
print (f"El valor de b es: {b}by el tipo es {type(b)}" )
print (f"El valor de c es: {c} y el tipo es {type(c)}")

tupla = (5,5.55,2+2j,True,"Manzana")
print(f"El tipo de tupla es: {type(tupla)}")
print(f"La primera posicion de la tupla es {tupla[0]} y su tipo es : {type(tupla[0])}")
print(f"La segunda posicion de la tupla es {tupla[1]} y su tipo es : {type(tupla[1])}")
print(f"La tercera posicion de la tupla es {tupla[2]} y su tipo es : {type(tupla[2])}")
print(f"La cuarta posicion de la tupla es {tupla[3]} y su tipo es : {type(tupla[3])}")
print(f"La quinta posicion de la tupla es {tupla[4]} y su tipo es : {type(tupla[4])}")



--------------------------------------------------------------------------------------------------


Conjunto {set} Datos desordenados y modificables

Los conjuntos en Python, representados por el tipo set, son colecciones desordenadas de
elementos únicos y mutables. Se definen utilizando llaves {. . . } y permiten realizar operaciones
matemáticas como unión, intersección y diferencia, además de eliminar elementos duplicados.
Ejemplo de uso de variables de tipo set


a = {1,2,3}
b= {4,5,6}
c = a.union(b) #union se usa para sumar en conjuntos

print (f"El valor de a es: {a} y el tipo es {type(a)}")
print (f"El valor de b es: {b}by el tipo es {type(b)}" )
print (f"El valor de c es: {c} y el tipo es {type(c)}")

Ejemplo: crear un conjunto que contenga un elemento de cada tipo básico

conjunto = {5,5.55,2+2j,True,"Manzana"}
print(f"El tipo de conjunto es:")


-----------------------------------------------------------------------------------------------------


--------------------------------------------------Diccionarios


Los diccionarios en Python, representados por el tipo dict, son colecciones desordenadas de
pares clave-valor. Cada clave es única y se utiliza para acceder a su valor asociado. Se definen
utilizando llaves { } con pares separados por dos puntos (clave: valor).
Ejemplo de uso de variables de tipo dict

los diccionarios necesitamos colocar la clave de acceso al valor para poder acceder


diccionario = {"nombre" : "Juan paco",  #RPimero va la clave y luego el contenido, ponte vrga
               "edad" : 29,
               "ciudad" : "merida"}

print (f"nombre : {diccionario["nombre"]}")
print (f"y tiene  : {diccionario["edad"]} años")
print (f"vive en : {diccionario["ciudad"]}")
print (f"El tipo de diccionario es : {type(diccionario)}")


persona = {
    "nombre": "Jorge",
    "edad": 29,
    "estatura " : 1.70,
    "estudiando" : True,    
}

print(f"El tipo de valor asociado a la clave nombre es : {type(persona['nombre'])}")
print(f"El tipo de valor asociado a la clave edad es : {type(persona['edad'])}")
print(f"El tipo de valor asociado a la clave estatura es : {type(persona['estatura '])}")
print(f"El tipo de valor asociado a la clave estudiando es : {type(persona['estudiando'])}")








---------------------------------Casting---------------------------------
El casting en Python se refiere a la conversión de una variable de un tipo de dato a otro. Esto
se puede hacer de manera explícita utilizando las funciones de casting incorporadas. Es útil
cuando necesitas convertir un tipo de dato para realizar ciertas operaciones que requieren ese
tipo específico.
Funciones Comunes de Casting en Python:

• int( ) : Convierte un valor a un entero
• float( ) : Convierte un valor a un número de punto flotante
• str( ) : Convierte un valor a una cadena de caracteres
• bool( ) : Convierte un valor a un booleano
• list( ) : Convierte un valor a una lista
• tuple( ) : Convierte un valor a una tupla
• set( ) : Convierte un valor a un conjunto
• dict( ) : Convierte un valor a un diccionario





"""
#Ejemplo 1: Convertir cadena a entero



cadena = "123"

numero_entero = int(cadena)

print(f"El valor de numero entero es : {numero_entero} y su tipo es {type(numero_entero)}")




#convertir entero a flotante

numero_ent = 10

numero_flotante = float(numero_ent)

print(f"El valor de numero flotante es : {numero_flotante} y su tipo es {type(numero_flotante)}")


#convertir flotante a cadena

numero_float = 123.456

cadena = str(numero_float)

print(f"El valor de cadena es : {cadena} y su tipo es {type(cadena)}")


#convertir numeor a booleano

num = 2 # el unico valor que resultara false es el 0
booleano = bool(num)

print(f"El valor de booleano es : {booleano} y su tipo es {type(booleano)}")


#convertir cadena a lista

cadena = "hola"
lista = list(cadena)
print(f"El valor de lista es : {lista} y su tipo es {type(lista)}")

#convertir lista a tupla

lista = [1,2,3]

tupla = tuple(lista)

print(f"El valor de tupla es : {tupla} y su tipo es {type(tupla)}")


# convertir lista a conjunto

lista = [1,2,3]

conjunt = set(lista)

print(f"El valor de conjunto es : {conjunt} y su tipo es {type(conjunt)}")


#convertir lista de tuplas a diccionario

tuplas_list = [("clave1", "valor1"),("clave2", "valor2"),("clave3", "valor3")]

diccionario = dict(tuplas_list)

print(f"El valor de diccionario es : {diccionario} y su tipo es {type(diccionario)}")



