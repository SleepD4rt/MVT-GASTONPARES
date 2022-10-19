# MVT-GASTONPARES

Desarrollado en Windows 10.

Proyecto entregable para CODERHOUSE, actividad "Nuestro primer MVT".

Realizar un:
```bash
git clone https://github.com/SleepD4rt/MVT-GASTONPARES.git
```
Ya cuenta con una base de datos para mostrar su contenido. 

Teniendo Django instalado y el sever en ejecución, dirigirse a la url del servidor y va a mostar una pantalla de inicio basica.

si se quiere agregar un miembro nuevo se debe utilizar el siguiente comando reemplazando el contenido dentro de <str:>
```bash
(DEFAULT)
127.0.0.1:8000:create_family_member/<str:name>/<str:last_name>/<str:birth_day>/<str:sex>/<str:height>/<str:profession>

Ejemplo:  127.0.0.1:8000:create_family_member/Gastón/Pares/2000-02-02/M/1,75/Programador
```

Le faltaria setear el ambiente de desarrollo "venv" y para ejecutar el proyecto sin alterar otros.

Para eso seguir las siguiente instruciones tras clonar el proyecto.

En consola situarse en el directorio del proyecto:
```bash
cd MVT-GASTONPARES/blog
```

crear el entorno venv:
```bash
python -m venv venv
venv/Scrips/activate
```

instalar Django:
```bash
pip install django
```

crear un super usuario en caso de querer explorar la url admin:
```bash
python manage.py createsuperuser
```

Escribir si se quiere un nombre de usuario, puede darle Enter, es opcional introducir un nombre de usuario. Lo mismo para el email.
Contraseña una sencilla como para probarlo. si es sencilla le va a salir un cartel de advertencia ignorelo tipeando "y" y pulse Enter.

ejecutar el servidor:

```bash
python manage.py runserver
```