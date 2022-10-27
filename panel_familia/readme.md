# Mi Primer MVT Django

Ejemplo de MVT para la clase de Coder House python, en el mismo podes: 

- Crear 
- Leer
- Actulizar
- Eliminar

Checkear que tengas Python
Para comenzar primero tienen que asegurarse que tienen instalado, python.

En windows tiene que abrir una terminal cmd o powershell.

PS C:\> python --version
Python 3.X.X 
En Linux/Mac tiene que abrir una terminal bash

$ python --version
Python 3.X.X 
Si les aparece la versión todo OK pueden seguir. Caso contrario descarguen python desde este link.

Instalar django
En una terminal cmd o powershell desde windows:

C:\> pip install django
Linux/Mac:

$ pip install django
Si no arrojo errores esto es suficiente para poder correr el projecto.

Clonar el projecto con git
windows:

C:\> git clone https://github.com/FedeGennaro/mi_proyecto_final
Linux/Mac:

$ git clone https://github.com/FedeGennaro/mi_proyecto_final
Correr el Servidor
Los siguinetes comandos son analogos en Mac/Linux/Windows:

cd mi-primer-mvt
python manage.py migrate
La consola mostrara las migraciones de la base de datos que se realizaron.

Luego arrancamos el servidor web

python manage.py runserver

ahora Hace click en el siguiente link para ver el ejemplo corriendo:

http://localhost:8000/