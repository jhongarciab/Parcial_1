import pandas as pd
import os
import psycopg2

class Conexión:
    def __init__(self, archivos=None, nombre_tabla=None):
        if archivos is None:
            archivos_en_carpeta = os.listdir()
            archivos_validos = [i for i in archivos_en_carpeta if os.path.isfile(i) and i.endswith('.csv')]
            if archivos_validos:
                print(f"No se ha especificado ningún archivo. Se usarán todos los archivos válidos en la carpeta actual.")
                self.archivos = archivos_validos
            else:
                raise ValueError("No hay archivos válidos en la carpeta actual.")
        else:
            self.archivos = archivos

        self.nombre_tabla = nombre_tabla
        self.nombre_bd = 'Test_db'
        self.usuario = 'postgres'
        self.password = 'Xevaxtiam1'
        self.host = '127.0.0.1'
        self.puerto = '5432'

    def crear_tabla(self):
        with psycopg2.connect(host=self.host, port=self.puerto, user=self.usuario, password=self.password, dbname=self.nombre_bd) as conn:
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

mi_objeto = Conexión(
    nombre_tabla="tabla11",
)
mi_objeto.crear_tabla()