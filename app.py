import os

from flask import Flask, jsonify
from proveedor import LinkedInLogin


"""

El protocolo a utilizar para hacer login con los 3 provedores sera ** OAuth 2.0 **, es decir que el proceso
para cada uno de los proovedores sera el mismo.
"""

#Definición de variables de entorno, usa aqui tus API keys.

# Linkedin
os.environ["LINKEDIN_LOGIN_CLIENT_ID"] = "77ptwpfx5vzj42"
os.environ["LINKEDIN_LOGIN_CLIENT_SECRET"] = "AQWxfrErEAanZAmp_RXql_2X953Ey6OAdvbfNAHNM-0TMEKXogcLndeWqtmjCInl6impRypzPA1g64bvzNfcFiQlkaPM1vuWReVZwjnS60qUcih6MlBnrCK5D0F5dCYiKvAM9W1pNhpiM1gG_JzmNvXzW54Mv40vta-dwumi0FZ2sDvmkWkMfLs54JI5KsWYu_8YP3au6FzEHjmnr-frq-fLJlRg3d4p0ACBz2ughjJm16Mb1J0LBtZt-X_9zgIHxKLGDbm-rLmbrK2THsZ5vBI2KPxL9zqyeSMGGOfcjkiWRJ09i0CQBS9Uc1dT-I7zCD4cRbAmXoNvrJW_t0VhIKvhn6i1Ug"



# Configuracion de la app

app = Flask(__name__)
app.config.update(
  SECRET_KEY="x34sdfm34",
)

"""
Se crea un tupla de llave-valor que luego se itera en el diccionario app.config donde se alamcena
el par de tokens de cada proveedor para uso gobal en la app.
"""

for config in (

  "LINKEDIN_LOGIN_CLIENT_ID",
  "LINKEDIN_LOGIN_CLIENT_SECRET",


):app.config[config] = os.environ[config]


# Se instancia cada una de clases con las configuraciones repectivas para cada proveedor.

linkedin_login = LinkedInLogin(app)

# Definicion de la ruta raiz

"""
En la ruta raiz se retorna un HTML con enlaze a las 3 opciones de login
"""

@app.route("/")
def index():
    return """
<html>
<button><a href="{}">Login con Linkedin</a> <br></button>

""".format(linkedin_login.authorization_url())


"""
Luego que alguna opción de login es selecionada se responde con una fallo o con exito
para el cual se responde con el JSON retornado por el API de cada proveedor utilizando la funcion 'jsonify'

"""
@linkedin_login.login_success
def login_success(token, profile):
    return jsonify(token, profile)

@linkedin_login.login_failure
def login_failure(e):
    return jsonify(error=str(e))

if __name__ == "__main__":
    app.run(debug=True)