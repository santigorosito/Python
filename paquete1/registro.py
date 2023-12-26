import json
import os

ruta = "/drive/MyDrive/pre_entrega"

with open (ruta + "/primerJson", "w") as file:
    json.dump(usuarios, file,indent=4)

usuarios = {}

def registro(usuarios):
    usuario = input("Ingrese su nombre de usuario: ")
    contrasenia = input("Ingrese su contraseña: ")
    return usuario, contrasenia

def almacenar_sesiones(diccionario, usuario, contrasenia):
    diccionario[usuario] = contrasenia

usuarios = {}
nombre_usuario, contrasenias1 = registro(usuarios)
almacenar_sesiones(usuarios, nombre_usuario, contrasenias1)

from json import drive
drive.mount('/content/drive')

def leerRegistro(usuarios):
    print(usuarios)

print("Usuarios almacenados son:")
leerRegistro(usuarios)

registro = open(ruta+ "/usuario.txt", "a")

registro.write(str(usuarios))
registro.close()

def login(usuarios):
    login_user = input("Ingrese su nombre de usuario: ")
    login_pass = input("Ingrese su contraseña: ")

    if login_user not in usuarios:
        return "No se ha encontrado el usuario"

    if login_pass != usuarios[login_user]:
        return "Contraseña incorrecta"

    return "Ha iniciado sesión"

resultado_login = login(usuarios)

print(resultado_login)