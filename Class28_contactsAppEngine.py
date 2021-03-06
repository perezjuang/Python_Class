'''

Las instrucciones para configurar el entorno de desarrollo de Google Cloud con python 3.7.7 en Windows las encuentran en https://cloud.google.com/appengine/docs/standard/python3/quickstart, y las instrucciones para
instalar y usar la librería ndb para Google Cloud Datastore las encuentran en https://googleapis.dev/python/python-ndb/latest/index.html.

Los pasos para configurar el proyecto con python 3.7.7 en windows son los siguientes:

Paso 1: Crear en la carpeta del proyecto los siguientes archivos:

main.py:

# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash, redirect
from contact_model import Contact
from google.cloud import ndb

app = Flask(__name__)
app.secret_key = 'some_secret'
app.debug = True


@app.route(r'/', methods=['GET'])
defcontact_book():
    client = ndb.Client()
    with client.context():
        contacts = Contact.query().fetch()
    return render_template('contact_book.html', contacts=contacts)


@app.route(r'/add', methods=['GET', 'POST'])
defadd_contact():
    
    if request.form:
        client = ndb.Client()
	with client.context():
	    contact = Contact(name=request.form.get('name'), phone=request.form.get('phone'), email=request.form.get('email'))
	    contact.put()
	    flash('¡Se añadió el contacto!')

    return render_template('add_contact.html')


@app.route(r'/contacts/<uid>', methods=['GET'])
defcontact_details(uid):
    client = ndb.Client()
    with client.context():
        contact = Contact.get_by_id(int(uid))

	ifnot contact:
            return redirect('/', code=301)

    return render_template('contact.html', contact=contact)

@app.route(r'/delete', methods=['POST'])
defdelete_contact():
    client = ndb.Client()
    with client.context():
	contact = Contact.get_by_id(int(request.form.get('uid')))
	contact.key.delete()
    return redirect('/contacts/{}'.format(contact.key.id()))

if __name__ == '__main__':
    app.run()
contact_model.py:

from google.cloud import ndb

classContact(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()
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

Flask == 1.1.2
google-cloud-ndb == 1.1.2
Paso 2: Crear dentro de la carpeta del proyecto la carpeta templates y dentro de ella crear los siguientes archivos:

index.html:

<!doctype html>
<html>
  <head>
    <metacharset="utf-8">
    <title>Agenda de contactos</title>  
  </head>
  <body>
    <h1>Agenda de contactos</h1>
    {% block body %}{% endblock %}
  </body>
</html>
contact_book.html:

{% extends 'index.html' %}
{% block body %}
  <ul>
    {% for contact in contacts %}
      <li>
        {{ contact.name }}<ahref="/contacts/{{ contact.key.id() }}">Ver más</a>
      </li>
    {% endfor %}
  </ul>
  <ahref="/add">añadir contacto</a>
{% endblock %}	
add_contact.html:

{% extends 'index.html' %}

{% block body %}

  {% with messages = get_flashed_messages() %}
    {% if messages %}
      {% for message in messages %}
        <p>{{ message }}</p>
      {% endfor %}
    {% endif %}
  {% endwith %}

<formaction="/add"method="post">
  <fieldset>
    <legend>Añadir nuevo contacto</legend>

    <labelfor="name">Nombre</label>
    <inputid="name"name="name"type="text">

    <labelfor="phone">Teléfono</label>
    <inputid="phone"name="phone"type="text">

    <labelfor="email">Email</label>}
    <inputid="email"name="email"type="email">

    <buttontype="submit"name="button">Añadir</button>
  </fieldset>

</form>
<p>
  <ahref="/">Regresar</a>
</p>
{% endblock %}
contact.html:

{% extends 'index.html' %}

{% block body %}

  <h2>{{ contact.name }}</h2>
  <p>Teléfono: {{ contact.phone }}</p>
  <p>Email: {{ contact.email }}</p>

  <hr>
  <formaction="/delete"method="post">
    <inputtype="hidden"name="uid"value="{{ contact.key.id() }}">
    <buttontype="submit">Eliminar</button>
  </form>

  <p>
    <ahref="/">Regresar</a>
  </p>

{% endblock %}
Paso 3: Descargar el instalador del SDK de Cloud desde https://cloud.google.com/sdk/docs/ y realizar la instalación.

Paso 4: Ejecutar el siguiente comando para instalar el componente de gcloud que incluye la extensión de App Engine extension para Python 3.7:

gcloud components install app-engine-python
Paso 5: Crear el entorno virtual con python 3.7:

virtualenv -p C:\Users\sopor\AppData\Local\Programs\Python\Python37\python.exe venv
Paso 6: Iniciar el entorno virtual venv:

venv\Scripts\activate.bat
Paso 7: Actualizar pip a la última versión con el siguiente comando:

python -m pip install --upgrade pip
Paso 8: Instalar Flask con el siguiente comando:

pip install flask
Paso 9: Instalar ndb con el siguiente comando:

pip install google-cloud-ndb 
Paso 10: Ejecutar el siguiente comando para instalar en la carpeta lib todas las librerías de Flask y de Ndb:

pip install -r requirements.txt -t lib 
Paso 11: Crear una cuenta de servicio. Reemplaza [NAME] por el nombre de la cuenta.

gcloud iam service-accounts create [NAME]
Paso 12: Otorgar permisos a la cuenta de servicio. Reemplaza [PROJECT_ID] por el ID del proyecto.

gcloud projects add-iam-policy-binding [PROJECT_ID] --member "serviceAccount:[NAME]@[PROJECT_ID].iam.gserviceaccount.com" --role "roles/owner"
Paso 13: Genera el archivo de claves. Reemplaza [FILE_NAME] por un nombre para el archivo de claves.

gcloud iam service-accounts keys create [FILE_NAME].json --iam-account [NAME]@[PROJECT_ID].iam.gserviceaccount.com
Paso 14: Crear y/o configurar la variable de entorno GOOGLE_APPLICATION_CREDENTIALS con la ruta del archivo de claves creado en el paso anterior.

GOOGLE_APPLICATION_CREDENTIALS=[PATH]

Ejemplo:

GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\credentials.json
Paso 15: Ingrese a Google Cloud Platform y asegúrese de que tanto la “API de Cloud Datastore” como la “API de Google Cloud Firestore” estén habilitadas. El link para acceder es el siguiente:

https://console.cloud.google.com/apis/library?filter=category:database&project=[PROJECT_ID]
Paso 16: Ejecutar el siguiente comando para autenticarse:

gcloud auth login
Paso 17: En caso que se requiera cambiar el project id se debe ejecutar la siguiente instrucción:

gcloud config set project PROJECT_ID
Paso 18: Ejecutar uno de los siguientes comandos para subir el código a App Engine:

Comando 1 (Se ejecuta cuando se requiere especificar el PROJECT_ID):

gcloud app deploy --project PROJECT_ID
Comando 2 (Se ejecuta cuando no se requiere especificar el PROJECT_ID):

gcloud app deploy

''''