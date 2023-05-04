from conexion import ConexionBD
import pandas as pd
import os
import psycopg2

class Conexion:
    def __init__(self, archivos=None, nombre_tabla=None):
        self.archivos = archivos or self.obtener_archivos_validos()
        self.nombre_tabla = nombre_tabla or input("Ingrese el nombre de la tabla: ")
        self.conexion_bd = ConexionBD()
    
    def obtener_archivos_validos(self):
        archivos_en_carpeta = os.listdir()
        archivos_validos = [i for i in archivos_en_carpeta if os.path.isfile(i) and i.endswith('.csv')]
        if archivos_validos:
            print(f"No se ha especificado ningún archivo. Se usarán todos los archivos válidos en la carpeta actual.")
            return archivos_validos
        else:
            raise ValueError("No hay archivos válidos en la carpeta actual.")

    def crear_tabla(self):
        with self.conexion_bd.conectar() as conn:
            with conn.cursor() as cursor:
                for i in self.archivos:
                    df = pd.read_csv(i)
                    columnas = [f'"{i.lower()}" VARCHAR(255)' for i in df.columns]
                    cursor.execute(f"CREATE TABLE {self.nombre_tabla} ({', '.join(columnas)})")

                    for _, row in df.iterrows():
                        values = [f"'{i}'" for i in row.values.tolist()]
                        cursor.execute(f"INSERT INTO {self.nombre_tabla} ({', '.join([f'{i.lower()}' for i in df.columns])}) VALUES ({', '.join(values)})")

                conn.commit()
        print(f"La tabla '{self.nombre_tabla}' ha sido creada y los datos han sido insertados.")
