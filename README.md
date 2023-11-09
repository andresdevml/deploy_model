# Despliegue de modelo ML mediante REST API  🧑‍💻

Uno de los aspectos fundamentales del desarrollo de modelos predictivos, es colocar a disposición este modelo para un servicio. En este caso lo haremos mediante la programación de una API implementada con Flask. 

# Herramientas  🛠️

* Flask
* Pickle
* Numpy
* Docker


# Server 👂

La api fue programada en el script _**server.py**_. En el mismo se programa la respuestas de la api ante una petición. En caso de ser necesario también se agrega el Dockerfile para desplegar la api desde un contenedor. 

# Request 🫴

Para probar el correcto funcionamiento de la api, se codifica en el script _**request.py**_, una petición a la api y se verifica que el resultado obtenido sea el correcto.  
