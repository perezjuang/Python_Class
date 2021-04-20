'''Diccionarios en Python
Un diccionario es un mapa de valores, los cuales deben tener una llav. Los diccionarios se declaran con (llaves) {} o con la función dict()

Cuando iteramos en diccionarios podemos hacerlo a través de las llaves, valores o ítems.

Declarar diccionarios
'''
mi_diccionario = {}
mi_diccionario['primer_elemento'] = 'hola'
mi_diccionario['segundo_elemento'] = 'adios'




calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 10
calificaciones['web'] = 8

#Iterar en llaves

for key in calificaciones.keys():
    print(key)

#Iterar en valores

for value in calificaciones.values():
    print(value)
#
# Iterar en ítems

for key, value in calificaciones.iteritems():
    print('llave: {}, valor: {}'.format(key, value))


##Validar phython3 

for key,value in calificaciones.items():
    print("llave {} y valor {}".format(key,value))


suma_de_calificafiones = 0
for calificacion in calificaciones.values():
    suma_de_calificafiones += calificacion

promedio = suma_de_calificafiones / len( calificaciones.values() )
