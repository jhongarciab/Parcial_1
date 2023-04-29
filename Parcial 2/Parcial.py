import psycopg2
import csv
import os


class LeerArchivos:
    def __init__(self, *args, **kwargs):
        self.ruta = kwargs.get('ruta', '.')
        self.archivos = args or self.obtener_archivos()

    def obtener_archivos(self):
        return os.listdir(self.ruta)

    def procesar_archivos(self, procesar_linea):
        for archivo in self.archivos:
            with open(os.path.join(self.ruta, archivo), newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Ignorar la primera línea (encabezado)
                for linea in reader:
                    datos = procesar_linea(linea)
                    self.insertar_en_bdd(datos)

    def insertar_en_bdd(self, datos):
        with psycopg2.connect(dbname='nombre_base_de_datos', user='usuario', password='contraseña', host='localhost') as conn:
            with conn.cursor() as cur:
                cur.execute('CREATE TABLE IF NOT EXISTS persona (id SERIAL PRIMARY KEY, nombre TEXT, apellido TEXT, mail TEXT)')
                cur.execute('INSERT INTO persona (nombre, apellido, mail) VALUES (%s, %s, %s)', datos)
            conn.commit()

    @classmethod
    def from_files(cls, *args, **kwargs):
        instancia = cls(*args, **kwargs)
        instancia.procesar_archivos(lambda linea: tuple(linea))  # Cada línea del archivo es una tupla con los valores a insertar
        return instancia

conexion = psycopg2.connect(
    host='127.0.0.1',
    user='postgres',
    password='admin1',
    database='Test_db'
)

cursor = conexion.cursor()

cursor.execute('SELECT version()')

resultado = cursor.fetchone()

print(resultado)