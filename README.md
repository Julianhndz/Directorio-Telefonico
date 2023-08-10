### Directorio Telefonico

Este proyecto esta realizado como practica de Python y Django, por lo cual solamente funciona en local. Para poder probarlo, sigue las instrucciones en consola.

# Clonar repositorio
```sh
git clone https://github.com/Julianhndz/Directorio-Telefonico.git
```
# Crear entorno virtual e instalación de requerimientos

- Estando en la ruta donde se clono el repositorio:

```sh
# Ejecuta este comando para crear el entorno virtual en Windows:
py -m venv venv
# En Unix o MacOs:
python3 -m venv venv
# Luego se debe realizar la activación del entorno virtual. En Windows:
.\venv\Scripts\activate
# En Unix o MacOs:
source venv/bin/activate
# Instalación de requerimientos:
pip install -r requirements.txt # En caso de no funcionar intentar con pip3.

```

# Correr servidor

- Estando en la carpeta raiz donde se clono el repositorio:

```sh
cd directory/
# Comando para correr el servidor en local (Por defecto -> http://localhost:8000 )
# En Windows:
py manage.py runserver # En caso de no funcionar comando 'py', intentar con 'pyhton'
# En Unix o MacOs:
python3 manage.py runserver
```

- Luego de seguir estos pasos podras ingresar al localhost en tu navegador preferido donde podras crear tu sesion y guardar y gestionar tus contacto (Actualizar/Eliminar).