#try:
	# Código a ejecutar
#except:
	# Código para 'cachar' o 'recibir' el error y hacer algo
#else:
	# Código cuando el try SÍ sirva y NO se ejecute el except
#finally:	
	# Código que SIEMPRE se va a ejecutar, independientemente se ejecute el except o el else





'''
try:
    # código que puede lanzar una excepción
except Exception, ex:
    # procesamiento de la excepción cuya información
    # es accesible a través del identificador ex

try: 
    f = open('myfile.txt') 
    s = f.readline() 
    i = int(s.strip()) 
except IOError as (errno, strerror): 
    print "I/O error({0}): {1}".format(errno, strerror) 
except ValueError: 
    print "Could not convert data to an integer." 
except: 
    print "Unexpected error:", sys.exc_info()[0] 
    raise 

try: 
    print "Performing an action which may throw an exception." 
except Exception, error: 
    print "An exception was thrown!" 
    print str(error) 
else: 
    print "Everything looks great!" 
finally: 
    print "Finally is called directly after executing the try statement whether an exception is thrown or not." 


import math
 
number_list = [10,-5,1.2,'apple']
 
for number in number_list:
    try:
        number_factorial = math.factorial(number)
    except TypeError:
        print("Factorial is not supported for given input type.")
    except ValueError:
        print("Factorial only accepts positive integer values.", number," is not a positive integer.")
    else:
        print("The factorial of",number,"is", number_factorial)
    finally:
        print("Release any resources in use.")

'''




# -*- coding: utf-8 -*-

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(raw_input('Escribe el nombre de un país: ')).lower()

    try:
        print('La población de {} es: {} millones'.format(country, countries[country]))
    except KeyError:
        print('No tenemos el dato de la población de {}'.format(country))