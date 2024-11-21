"""

Tipos de datos avanzados



Listas   []

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



Tuplas  ()

Las tuplas en Python, representadas por el tipo tuple, son colecciones ordenadas e INMUTABLES
de elementos que pueden ser de diferentes tipos de datos. Se definen usando paréntesis (. . . ) EN LUGAR DE CORCHETES y,
una vez creadas, sus elementos no pueden ser modificados ni eliminados.

Ejemplo de uso de variables de tipo tuple

"""
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