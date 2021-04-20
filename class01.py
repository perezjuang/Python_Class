
$ sudo apt-get install python3.1
$ sudo yum install python
$ python
 >>> 
 $ python archivo.py


Enteros (int): en este grupo están todos los números, enteros y long:
ejemplo: 1, 2, 3, 2121, 2192, -123

Booleanos (bool): Son los valores falso o verdadero, compatibles con todas las operaciones booleanas ( and, not, or ):
ejemplo: True, False

Cadenas (str): Son una cadena de texto :
ejemplos: “Hola”, “¿Cómo estas?”

Listas: Son un grupo o array de datos, puede contener cualquiera de los datos anteriores:
ejemplos: [1,2,3, ”hola” , [1,2,3] ], [1,“Hola”,True ]

Diccionarios: Son un grupo de datos que se acceden a partir de una clave:
ejemplo: {“clave”:”valor”}, {“nombre”:”Fernando”}

Tuplas: también son un grupo de datos igual que una lista con la diferencia que una tupla después de creada no se puede modificar.
ejemplos: (1,2,3, ”hola” , (1,2,3) ), (1,“Hola”,True) (Pero jamás podremos cambiar los elementos dentro de esa Tupla)

En Python trabajas con módulos y ficheros que usas para importar las librerías.

Funciones

def my_first_function():
	 return “Hello World!” 
my_first_function()

Variables
Las variables, a diferencia de los demás lenguajes de programación, no debes definirlas, ni tampoco su tipo de dato, ya que al momento de iterarlas se identificará su tipo. Recuerda que en Python todo es un objeto.

 A = 3 
 B = A
Listas
Las listas las declaras con corchetes. Estas pueden tener una lista dentro o cualquier tipo de dato.

 >>> L = [22, True, ”una lista”, [1, 2]] 
 >>> L[0] 
 22

Tuplas
Las tuplas se declaran con paréntesis, recuerda que no puedes editar los datos de una tupla después de que la has creado.

T = (22, True, "una tupla", (1, 2)) 
 T[0] 
 22

Diccionarios
En los diccionarios tienes un grupo de datos con un formato: la primera cadena o número será la clave para acceder al segundo dato, el segundo dato será el dato al cual accederás con la llave. Recuerda que los diccionarios son listas de llave:valor.

D = {"Kill Bill": "Tamarino", "Amelie": "Jean-Pierre Jeunet"} 
D["Kill Bill"]
 "Tamarino"

Conversiones

De flotante a entero:

 >>> int(4.3)
 4
De entero a flotante:

 >>> float(4) 
 4.0

De entero a string:

 >>> str(4.3) 
 "4.3"
De tupla a lista:

 >>> list((4, 5, 2)) 
 [4, 5, 2]

amigos=list()
amigos.append('Pedro')
amigos[0]
'Pedro'

amigos.append('Enrique')
amigos[1]
'Enrique'

DATA DataFrames


frame_test = pd.DataFrame([[200,201,202],
                            [100,501,202],
                            [300,251,502]],columns=[1999,2000,2001],index=['comida','bebida','extra'])

Índices y selección
Existen muchas formas de manipular los DataFrames y de seleccionar los elementos que queremos transformar.

Dictionary like:
df[`col1`] 
df[['col1', 'col3']]
Numpy like:
iloc = index location

df.iloc[:]
df.iloc[:,:]
Label based:
loc = location
df.loc[:]
df.loc[:,:]
Existe una gran diferencia en la forma en la que utilizamos estos slices porque varia de la forma tradicional de Python. loc va a incluir el final del que necesitamos.





Operadores Comunes
Longitud de una cadena, lista, tupla, etc.:

 >>> len("key") 
 3
Tipo de dato:

 >>> type(4) 
 < type int >
Aplicar una conversión a un conjunto como una lista:

 >>> map(str, [1, 2, 3, 4])
 ['1', '2', '3', '4']
Redondear un flotante con x número de decimales:

>>> round(6.3243, 1)
 6.3
Generar un rango en una lista (esto es mágico):

 >>> range(5) 
 [0, 1, 2, 3, 4]
Sumar un conjunto:

 >>> sum([1, 2, 4]) 
 7

Organizar un conjunto:

 >>> sorted([5, 2, 1]) 
 [1, 2, 5]

Conocer los comandos que le puedes aplicar a x tipo de datos:

 >>>Li = [5, 2, 1]
 >>>dir(Li)
 >>>['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

Información sobre una función o librería:

 >>> help(sorted) 
 (Aparecerá la documentación de la función sorted)

Clases
Clases es uno de los conceptos con más definiciones en la programación, pero en resumen sólo son la representación de un objeto. Para definir la clase usas class y el nombre. En caso de tener parámetros los pones entre paréntesis.
Para crear un constructor haces una función dentro de la clase con el nombre init y de parámetros self (significa su clase misma), nombre_r y edad_r:

class Estudiante(object): 
 	def __init__(self,nombre_r,edad_r): 
 		self.nombre = nombre_r 
 		self.edad = edad_r 

 	def hola(self): 
		return "Mi nombre es %s y tengo %i" % (self.nombre, self.edad) 
 
e = Estudiante(“Arturo”, 21) 
print e.hola() 


Métodos especiales
cmp(self,otro)
Método llamado cuando utilizas los operadores de comparación para comprobar si tu objeto es menor, mayor o igual al objeto pasado como parámetro.

len(self)
Método llamado para comprobar la longitud del objeto. Lo usas, por ejemplo, cuando llamas la función len(obj) sobre nuestro código. Como es de suponer el método te debe devolver la longitud del objeto.

init(self,otro)
Es un constructor de nuestra clase, es decir, es un “método especial” que llamas automáticamente cuando creas un objeto.

Condicionales IF

 if ( a > b ):
 	elementos 
 elif ( a == b ): 
 	elementos 
 else:
 	elementos


Bucle FOR

 for i in range(10):
 	print i


Bucle WHILE

x = 0 
while x < 10: 
 	print x 
 	x += 1


(+) Suma

(-) Resta

(asterisco) Multiplicación

(/) División

(//) División de enteros

(%) Operador de módulo

(doble asterisco) Potencias

(>) Mayor que

(<) Menor que

(==) Igual

(>=) Mayor igual

(<=) Menor igual

pi = 3.14159
radio =3
area = pi * radio**2
print(area)



=======================

def say_hello(age):
    if age > 18:
        print('Hola senor')
    else:
        print('Hola nino')

say_hello(20)
say_hello(14)




=====================================


# -*- coding: utf-8 -*-

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False

    return True


def run():
    number = int(raw_input('Escribe un número: '))
    result = is_prime(number)

    if result is True:
        print('Tu número es primo')
    else:
        print('Tu número NO es primo')


if __name__ == '__main__':
    run()



=========================================


https://docs.python.org/3/


PANDAS

¿Cómo trabajar con datos faltantes?
Los datos faltantes representan un verdadero problema sobre todo cuando estamos realizando agregaciones. Imagina que tenemos datos faltantes y los llenamos con 0, pero eso haría que la distribución de datos se modificaría radicalmente. Podemos eliminar los registros, pero la fuerza de nuestras conclusiones se debilita.

Pandas nos otorga varias funcionalidades para identificarlas y para trabajar con ellas. Existe el concepto que se llama NaN, cuando existe un dato faltante simplemente se rellena con un NaN y en ese momento podemos preguntar cuáles son los datos faltantes con .isna().

notna() para preguntar dónde hay datos completos.
dropna() para eliminar el registro.
Para reemplazar:

fillna() donde le damos un dato centinela
ffill() donde utiliza el último valor.


Función _fill_missing_titles

<def_fill_missing_titles(df):
    logger.info('Filling missing titles')
    missing_titles_mask = df['title'].isna()

    missing_titles = (df[missing_titles_mask]['url']
                      .str.extract(r'(?P<missing_titles>[^/]+)$')
                      .applymap(lambda title: title.split('-'))
                      .applymap(lambda title_word_list: ''.join(title_word_list))
                     )

    df.loc[missing_titles_mask, 'title'] = missing_titles.loc[:,'missing_titles']

    return df>





(va sin acentos)
En mi caso tenia que borrar mas de una expresion.
Tampoco es necesario pasar el body a lista, podemos hacer replace directamente (en este caso, si)

Opcion 1:

stripped_body2 = (el_universal
                    .apply(lambda row: row['body'], axis=1)
                    .apply(lambda body: body.replace('\n',''))
                    .apply(lambda body: body.replace('\r',''))
                )

stripped_body2
O usando expresiones regulares, MI FAVORITA:
Opcion 2:

import re

stripped_body3 = (el_universal
                    .apply(lambda row: row['body'], axis=1)
                    .apply(lambda body: re.sub(r'(\n|\r)+',r'', body))
                )

stripped_body3```


