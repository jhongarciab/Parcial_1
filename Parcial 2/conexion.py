import psycopg2
import sys

class ConexionBD:
    def __init__(self, nombre_bd='Test_db', usuario='postgres', password='Xevaxtiam1', host='127.0.0.1', puerto='5432'):
        self.nombre_bd = nombre_bd
        self.usuario = usuario
        self.password = password
        self.host = host
        self.puerto = puerto

    def conectar(self):
        return psycopg2.connect(
            host=self.host, port=self.puerto, user=self.usuario, password=self.password, dbname=self.nombre_bd
        )