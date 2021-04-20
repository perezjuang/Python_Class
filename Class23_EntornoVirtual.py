'''
Descargar el Script de Python  https://pip.pypa.io/en/stable/installing/

y ejecutar python get-pip.py


python -m pip install -U pip
pip --version


mkdir server01
pwd
cd server01

pip install virtualenv
pip install --upgrade --force virtualenv 

virtualenv venv
Linux/Mac venv/bin/activate
        You need to run

        . venv/bin/activate
        or

        source venv/bin/activate

        echo $PATH
        export PATH=$PATH:/place/with/the/file
        export PATH=$PATH:/home/pi/.local/bin

windows venv\Scripts\activate.bat

Instalar dependencias del archivo requirements
pip freeze

pip install -r requirements.txt
#https://pypi.org/search/?q=requests

Variables de Entorno
C:\Users\JuanGabrielPérezGuer\AppData\Local\Programs\Python\Python38-32;
C:\Users\JuanGabrielPérezGuer\AppData\Local\Programs\Python\Python38-32\Scripts

C:\Program Files (x86)\Python38-32\Scripts\;
C:\Program Files (x86)\Python38-32\






py3 ========================================

python3 -m pip install --upgrade pip





Guía rápida (cheat sheet) de virtualenv y pip
🎯 Instalar virtualenv:

$> pip install virtualenv
🎯 Crear entorno virtual:

$> virtualenv env
🎯 Crear entorno virtual especificando el intérprete:

$> virtualenv -p ruta/interprete/python env
🎯 Crear entorno virtual heredando las librerías del sistema (no recomendado):

$> virtualenv --system-site-packages env
🎯 Activar el entorno virtual en Linux/Mac:

$> source env/bin/activate
🎯 Activar el entorno virtual en Windows:

$> env\Scripts\activate.bat
🎯 Salir del entorno virtual:

$> deactivate
🎯 Instalar un paquete/librería (por ejemplo, flask):

$> pip install flask
🎯 Instalar una versión concreta de un paquete/librería:

$> pip install flask==1.0.1
🎯 Actualizar la versión de un paquete/librería:

$> pip install flask -U
🎯 Desinstalar una librería:

$> pip uninstall flask
🎯 Listar todas las librerías:

$> pip list
🎯 Listar todos los paquetes/librerías en formato requirements.txt:

$> pip freeze
🎯 Crear/Actualizar el fichero requirements.txt:

$> pip freeze > requirements.txt
🎯 Mostrar la información de un paquete/librería:

$> pip show flask



'''

https://jupyter.org/install.html
https://jupyter.org/

windows
anaconda
jupyter-notebook
jupyter


pip install nbopen
python -m nbopen.install_win