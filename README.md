# German Lopez Bucar y Federico Gennaro

En este blog podes encontrar los mejores restarurantes de argentina, una vez registrado podras : 

- Agregar un nuevo posteo
- Actulizar un posteo existente
- Eliminar un posteo

## Checkear que tengas Python

Para comenzar primero tienen que asegurarse que tienen instalado python.

En windows tiene que abrir una terminal cmd o powershell.

```PS
PS C:\> python --version
Python 3.X.X 
```

En Linux/Mac tiene que abrir una terminal bash

```bash
$ python --version
Python 3.X.X 
```

Si les aparece la versión pueden seguir. Caso contrario descarguen python desde este [link](https://www.python.org/downloads/).

## Instalar django

En una terminal cmd o powershell desde windows:

```PS
C:\> pip install django
```

Linux/Mac:

```bash
$ pip install django
```

## Clonar el projecto con git

windows:

```PS
C:\> git clone https://github.com/FedeGennaro/mi_proyecto_final
```

Linux/Mac:
```bash
$ git clone https://github.com/FedeGennaro/mi_proyecto_final
```

## Correr el Servidor

Los siguinetes comandos son analogos en Mac/Linux/Windows:

```bash
python manage.py migrate
```
La consola mostrara las migraciones de la base de datos que se realizaron.

Luego arrancamos el servidor web

```bash
python manage.py runserver
```
Listo ya tenes corriendo el blog.

ahora Hace click en el siguiente link para ver el ejemplo corriendo: 

[http://localhost:8000/](http://localhost:8000/)