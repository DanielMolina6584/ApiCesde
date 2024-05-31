import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
usuario = os.getenv("DB_USER")
contraseña = os.getenv("DB_PASSWORD")
base_de_datos = os.getenv("DB_DATABASE")

class BaseDeDatos:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host=host,
            user=usuario,
            password=contraseña,
            database=base_de_datos
        )
        self.cursor = self.conexion.cursor()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()