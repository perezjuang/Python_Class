'''
Luego de revisar un aporte del compañero BryanBQV y de hacer pruebas pude notar que no es necesario instalar gunicorn.

Las instrucciones para configurar el entorno de desarrollo de Google Cloud con python 3.7.7 en Windows las encuentran en https://cloud.google.com/appengine/docs/standard/python3/quickstart

A continuación les presento todos los pasos que seguí:

Crear en la carpeta del proyecto los siguientes archivos:
main.py:

# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
defhola():
    return'Hola, alumnos de Platzi!'

if __name__ == '__main__':
    app.run()
app.yaml:

service: default
runtime: python37

handlers:
- url: .*
script: auto
secure: always
appengine_config.py:

from google.appengine.ext import vendor
vendor.add('lib')
requirements.txt:

Flask==1.1.2
Descargar el instalador del SDK de Cloud desde https://cloud.google.com/sdk/docs/ y realizar la instalación.

Instalar Git

Ejecutar el siguiente comando para instalar el componente de gcloud que incluye la extensión de App Engine extension para Python 3.7:

gcloud components install app-engine-python

Crear el entorno virtual con python 3.7:

virtualenv -p C:\Users(usuario)\AppData\Local\Programs\Python\Python37\python.exe venv

Iniciar el entorno virtual venv:

venv\Scripts\activate.bat

Instalar Flask con pip:

pip install flask

Crear el archivo requirements.txt con lo siguiente:

Flask==1.1.2

Ejecutar el siguiente comando para instalar en la carpeta lib todas las librerías de Flask:

pip3 install -r requirements.txt -t lib

Ejecutar el siguiente comando para autenticarse:

gcloud auth login

En caso que se requiera cambiar el project id se debe ejecutar la siguiente instrucción:

gcloud config set project PROJECT_ID

Ejecutar uno de los siguientes comandos para subir el código a App Engine:

Comando 1 (Se ejecuta cuando se requiere especificar el PROJECT_ID):

gcloud app deploy --project PROJECT_ID

Comando 2 (Se ejecuta cuando no se requiere especificar el PROJECT_ID):

gcloud app deploy

'''