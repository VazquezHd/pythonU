

# Tipos de datos




# Los programas consisten en código y datos, pero internamente en la memoria del ordenador
# son simplemente una secuencia de bits. La manera en que estos bits se interpretan depende del
# lenguaje de programación, el cual almacena no solo el dato en sí, sino también varios metadatos.
# Cada segmento de memoria en realidad contiene un objeto, por lo que se dice que en Python
# todo son objetos. Cada objeto tiene al menos los siguientes componentes:
# • Un tipo de dato almacenado: Indica la naturaleza del dato, como entero, cadena, lista,
# etc. Esto determina las operaciones que se pueden realizar con ese objeto. En Python, se
# puede obtener usando la función type(), que devuelve el tipo del objeto.
# • Un identificador único para distinguirlo de otros objetos: Es una referencia única en la
# memoria que permite diferenciar este objeto de todos los demás. En Python, se puede
# obtener usando la función id(), que devuelve la dirección de memoria del objeto.
# • Un valor que coincide con su tipo: Es el contenido real del objeto, consistente con su tipo
# de dato.


# Ejemplo



# Definimos una variable con un valor entero
numero = 42
# Obtenemos el tipo de dato del objeto
tipo_dato = type(numero)
# Obtenemos el identificador único del objeto
identificador = id(numero)
# Valor del objeto
valor = numero
# Imprimimos la información
#{} es para concatenar
#f es 
print(f'Tipo de dato: {tipo_dato}')
print(f'Identificador unico: {identificador}')
print(f'Valor: {valor}')


# Tipo de dato: <class 'int'>
# Identificador único: 140724404349128
# Valor: 42


# Tipos de datos básicos

# • Enteros
# • Flotantes
# • Complejos
# • Booleanos
# • Cadenas de carácteres (Strings)


# Tipos de datos avanzados


# • Listas
# • Tuplas
# • Conjuntos
# • Diccionarios


