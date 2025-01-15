"""
Operadores
Los operadores en Python son símbolos especiales que se usan para realizar operaciones sobre
valores y variables. Estos operadores se pueden clasificar en varias categorías según el tipo de
operación que realizan.
Tipos de Operadores en Python

• Operadores Aritméticos:
– Se usan para realizar operaciones matemáticas comunes

• Operadores de Asignación:
– Se usan para asignar valores a las variables

• Operadores de Comparación:
– Se usan para comparar dos valores

• Operadores Lógicos:
– Se usan para comparar dos valores

• Operadores de Identidad:
– Se usan para comparar los objetos; no si son iguales, sino si son el mismo objeto en
memoria

• Operadores de Pertenencia:
– Se usan para probar si una secuencia se presenta en un objeto





Operadores aritméticos
Se usan para realizar las siguientes operaciones matemáticas comunes:
• Suma: +
– Ejemplo: 1 + 2 (Resultado = 3)
• Resta: -
– Ejemplo: 3 - 2 (Resultado = 1)
• Multiplicación: *
– Ejemplo: 2 * 4 (Resultado = 8)
• División: /
– Ejemplo: 9 / 2 (Resultado = 4.5)
• Exponenciación (Calcula la potencia de un número): Se utiliza **
– Ejemplo: 2 ** 3 (2
3 = 8, Resultado = 8)
• División entera (Calcula la parte entera de la división de 2 números): Se utiliza
//
– Ejemplo: 10 // 3 (El 3 cabe 3 veces en el 10 y sobra 1, Resultado = 3)
• Módulo (Calcula el residuo de dividir 2 números): Se utiliza el símbolo %
– Ejemplo: 10 % 3 (El 3 cabe 3 veces en el 10 y sobra 1, Resultado = 1)





# Suma
a = 3
b = 2

suma = a + b
print(f"Suma: {a} + {b} = {suma}")
#Resta
1
a = 3
b = 2
resta = a - b
print(f"Resta: {a} - {b} = {resta}")
# Multiplicación
a = 3
b = 2
multiplicacion = a * b
print(f"Multiplicación: {a} * {b} = {multiplicacion}")

# División
a = 10
b = 3
division = a / b
print(f"División: {a} / {b} = {division}")
# Exponenciación
a = 3
b = 2
potencia = a ** b
print(f"Exponenciación: {a} ** {b} = {potencia}")
# División entera
a = 10
b = 3
division_entera = a // b
print(f"División entera: {a} // {b} = {division_entera}")
# Modulo
a = 10
b = 3
modulo = a % b     
# el modulo es el residuo que queda de la division
print(f"Modulo: {a} % {b} = {modulo}")




#Operadores de asignación   (esta madre lo que hace es hacer la operacion en la misma variable y reasignarlo ahi mismo )
Se usan para asignar valores a las variables:
• Asignación : Se utiliza =
– Ejemplo: a = 3 (Se asigna el valor de 3 a la variable a)
• Suma y asignación : Se utiliza +=
– Ejemplo: a += 2 (Se incrementa el valor de a en 2)
• Resta y asignación : Se utiliza -=
– Ejemplo: a -= 2 (Decrementa el valor de a en 2)
• Multiplicación y asignación : Se utiliza *=
– Ejemplo: a = 2 ( a* se multiplica por 2 y el resultado se guarda de nuevo en a)
• División y asignación : Se utiliza /=
– Ejemplo: a /= 2 (a se divide entre 2 y el resultado se guarda de nuevo en a)
• Exponenciación y asignación : Se utiliza **=
– Ejemplo: a **= 2 (a se eleva a la segunda potencia y el resultado se guarda de
nuevo en a)
• División entera y asignación : Se utiliza //=
– Ejemplo: a //= 2 (a se divide entre 2 y la parte entera de la división se guarda de
nuevo en a)
• Módulo y asignación : Se utiliza %=
– Ejemplo: a %= 2 (Se calcula el residuo de dividir a entre 2 y este residuo se guarda
en a)





a = 5
print (f"Asignacion: a = {a}")

#suma y asignacion

a = 5
a += 3
print(f"a += 3 = {a}")

#resta y asignacion

a = 5
a -= 3
print(f"a -= 3 = {a}")

#multiplicacion y asignacion

a = 5
a *= 3
print(f"a *= 3 = {a}")

#division y asignacion

a = 5
a /= 2
print(f"a /= 2 = {a}")


# esponenciacion y asignacion

a = 5
a **= 2
print(f"a **= 2 = {a}")

#division entera y asignacion

a = 5
a //= 2
print(f"a //= 2 = {a}")

#modulo y asignacion

a = 5
a %= 2
print(f"a %= 2 = {a}")






Operadores de comparación
Se usan para comparar dos valores:
• Igual a : ==
– Ejemplo: a == b (Compara si a es igual a b. Si son iguales, se obtiene un True. Si
no son iguales, se obtiene un False)
• No igual a : !=
– Ejemplo: a != b (Compara si a es diferente de b. Si son diferentes, se obtiene un
True. Si son iguales, se obtiene un False)
• Mayor que : >
– Ejemplo: a > b (Compara si a es mayor a b. Si a es mayor, se obtiene un True. Si a
es menor, se obtiene un False)
• Menor que : <
– Ejemplo: a < b (Compara si a es menor a b. Si a es menor, se obtiene un True. Si
a es mayor, se obtiene un False)
• Mayor o igual que : Se utiliza >=
– Ejemplo: a >= b (Compara si a es mayor o igual a b. Si a es mayor o igual a b, se
obtiene un True. Si a es menor a b, se obtiene un False)
• Menor o igual que : Se utiliza <=
– Ejemplo: a <= b (Compara si a es menor o igual a b. Si a es menor o igual a b, se
obtiene un True. Si a es mayor a b, se obtiene un False)

"""

