#Tipos de datos basicos
#datos enteros
#Un dato entero en Python, representado por el tipo int, es un tipo de dato numérico que almacena valores sin decimales, tanto positivos como negativos, y puede ser de cualquier tamaño sin límite de precisión.
"""
a = 4
b = 7
c = a + b
print(f"El valor de a es: {a}")
print(f"El valor de b es: {b}")
print(f"El valor de c es: {c}")
print(f"El tipo de a es: {type(a)}")
print(f"El tipo de b es: {type(b)}")
print(f"El tipo de c es: {type(c)}")



#calculo con num enteros
# Definir 2 números enteros
num1 = 15
num2 = 4


# Realizar operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division_entera = num1 // num2  #con // dividen division entera(nada de decimales)
modulo = num1 % num2
# Imprimir los resultados
print(f"El tipo de suma es: {type(suma)} y su valor es {suma}")
print(f"El tipo de resta es: {type(resta)} y su valor es {resta}")
print(f"El tipo de multiplicacion es: {type(multiplicacion)} \
y su valor es {multiplicacion}")
print(f"El tipo de division_entera es: {type(division_entera)} \
y su valor es {division_entera}")
print(f"El tipo de modulo es: {type(modulo)} y su valor es {modulo}")


"""



#Flotantes
"""
Un flotante en Python, representado por el tipo float, es un tipo de dato numérico que almacena
valores con decimales, permitiendo representar números fraccionarios y realizar cálculos con
precisión decimal.
"""

"""
a = 4
b = 7.2
c = a + b
print(f"El valor de a es: {a}")
print(f"El valor de b es: {b}")
print(f"El valor de c es: {c}")
print(f"El tipo de a es {type(a)} y su valor es {a}")
print(f"El tipo de b es {type(b)}y su valor es {b}")
print(f"El tipo de c es {type(c)}y su valor es {c}")
"""

#VAMOS A CONVERTIR CELCIUS A FARENHEIT
"""
celsius = 24.8
farenheit = celsius * 9/5 +32

print(f"La temperatura en grados es {farenheit}")
print(f"El tipo de dato de la variable farenheit  es {type(farenheit)}")
"""
"""
Complejos
Un número complejo en Python, representado por el tipo complex, es un tipo de dato numérico
que almacena valores con una parte real y una parte imaginaria, permitiendo realizar cálculos
en el plano complejo. Los números complejos se escriben en la forma a + bj, donde a es la
parte real y b es la parte imaginaria.

Ejemplo de uso de variables de tipo COMPLEX
"""
"""
z1 = 4 + 2j
z2= 1+3j
z3=z1+z2

print(f"El tipo de z1 es {type(z1)} y El valor de z1 es {z1}")
print(f"El tipo de z1 es {type(z2)} y El valor de z1 es {z2}")
print(f"El tipo de z1 es {type(z3)} y El valor de z1 es {z3}")

z1 = 2 + 3j
z2 = 4 -2j

suma = z1 + z2
resta = z1 - z2
multiplicacion = z1 * z2
division = z1 / z2

print(f"Suma : {suma}")
print(f"Resta : {resta}")
print(f"Multiplicacion : {multiplicacion}")
print(f"Division : {division}")





Booleanos
Los booleanos en Python, representados por el tipo bool, son un tipo de dato que puede tener
uno de dos valores: True o False. Se utilizan principalmente para representar condiciones y
controlar el flujo de ejecución en estructuras de control como condicionales y bucles.
Ejemplo de uso de variables de tipo bool


a = 4
b = 3
c = a == b  #== es para comparacion

print(f"el valor de a es : {a}")
print(f"el valor de b es : {b}")
print(f"el valor de a y b son iguales : {c}")
print(f"el tipo de a es : {type(a)}")
print(f"el tipo de b es : {type(b)}")
print(f"el tipo de c es : {type(c)}")


verificar si un pasword es correcto

pasword_correcto = "h20"
pasword_prueba = "h201"

verificacion = pasword_correcto == pasword_prueba

print(f"El valor de verificacion es {verificacion}")
print(f"El tipo de verificacion es {type(verificacion)}")










Cadenas de caracteres (Strings)
Los strings en Python, representados por el tipo str, son secuencias de caracteres utilizadas
para almacenar y manipular texto. Se pueden definir usando comillas simples ‘Texto’ o dobles
“Texto”.
Ejemplo utilizando variables de tipo str
"""
a = "Mi nombre es: "
b = "Ivan Vaz"
c = a + b
print(f"El valor de a es: {a}")
print(f"El valor de b es: {b}")
print(f"El valor de c es: {c}")
print(f"El tipo de a es: {type(a)}")
print(f"El tipo de b es: {type(b)}")
print(f"El tipo de c es: {type(c)}")

nombre1 = "Jose"
curso1 = "python"
print(f"Este curso de {curso1} fue creado por {nombre1}")