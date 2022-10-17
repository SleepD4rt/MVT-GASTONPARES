# MVT-GASTONPARES

Desarrollado en Windows 10.

Proyecto entregable para CODERHOUSE, actividad "Nuestro primer MVT".


Realizar un git clone https://github.com/SleepD4rt/MVT-GASTONPARES.git

Ya cuenta con una base de datos para mostrar su contenido. 

Teniendo Django instalado y el sever en ejecución, dirigirse a la url del servidor y va a mostar una pantalla de inicio basica.

si se quiere agregar un miembro nuevo se debe utilizar el siguiente comando reemplazando el contenido dentro de <str:>

(DEFAULT)
127.0.0.1:8000:create_family_member/<str:name>/<str:last_name>/<str:birth_day>/<str:sex>/<str:height>/<str:profession>

Ejemplo:  127.0.0.1:8000:create_family_member/Gastón/Pares/2000-02-02/M/1,75/Programador
