from matplotlib import pyplot as plt
from Cursor import CursorDelPool
from Sentencias import SentenciasSQL
import seaborn as sns
from scipy.optimize import fsolve
import numpy as np
import pandas as pd
import os

class Conexión:
    def __init__(self, archivos=None, nombre_tabla=None):
        if archivos is None:
            archivos_en_carpeta = os.listdir()
            archivos_validos = [i for i in archivos_en_carpeta if os.path.isfile(i) and i.endswith('.csv')]
            if archivos_validos:
                self.archivos = archivos_validos
            else:
                raise ValueError("No hay archivos válidos en la carpeta actual.")
        else:
            self.archivos = archivos

        self.nombre_tabla = nombre_tabla

    def crear_tabla(self):
        with CursorDelPool() as cursor:
            for i, j in enumerate(self.archivos):
                nombre_tabla = self.nombre_tabla[i]
                df = pd.read_csv(j)
                columnas = [f'"{i.lower()}" VARCHAR(255)' for i in df.columns]
                cursor.execute(SentenciasSQL._TABLA.format(nombre_tabla, ', '.join(columnas)))

                for _, row in df.iterrows():
                    values = [f"'{i}'" for i in row.values.tolist()]
                    cursor.execute(SentenciasSQL._INSERTAR.format(nombre_tabla, ', '.join([f'{i.lower()}' for i in df.columns]), ', '.join(values)))
                              
        print(f"La tabla '{self.nombre_tabla}' ha sido creada y los datos han sido insertados.")
    
    def combinar_tablas(self):
        dfs = []
        for archivo in self.archivos:
            df = pd.read_csv(archivo)
            dfs.append(df)

        df_combinado = pd.concat(dfs, axis=0, join='inner')
        df_combinado = df_combinado.drop_duplicates(subset=df_combinado.columns[:3])
        return df_combinado

    def crear_tabla_combinada(self, df_combinado):
        with CursorDelPool() as cursor:
            nombre_tabla = self.nombre_tabla
            columnas = [f'"{i.lower()}" VARCHAR(255)' for i in df_combinado.columns]
            cursor.execute(SentenciasSQL._TABLA.format(nombre_tabla, ', '.join(columnas)))

            for _, row in df_combinado.iterrows():
                values = [f"'{i}'" for i in row.values.tolist()]
                cursor.execute(SentenciasSQL._INSERTAR.format(nombre_tabla, ', '.join([f'{i.lower()}' for i in df_combinado.columns]), ', '.join(values)))

        print(f"La tabla '{self.nombre_tabla}' ha sido creada y los datos han sido insertados.")

    def crear_grafico_regresion(self, columna_x, columna_y):
        with CursorDelPool() as cursor:
            conn = cursor.connection
            df = pd.read_sql(SentenciasSQL._SELECCIONAR.format(columna_x, columna_y, self.nombre_tabla), conn)

        print(f'Los datos son los siguientes: {df}')

        df[columna_x] = pd.to_numeric(df[columna_x], errors='coerce')
        df[columna_y] = pd.to_numeric(df[columna_y], errors='coerce')

        sns.regplot(x=columna_x, y=columna_y, data=df)
        plt.title(f'Regresión lineal entre {columna_x} y {columna_y}')
        plt.show()

    def obtener_nombres_tablas(self):
        with CursorDelPool() as cursor:
            cursor.execute(SentenciasSQL._LISTAR_TABLAS)
            tablas = [tabla[0] for tabla in cursor.fetchall()]
        return tablas
    
class FuncionMatematica():
    
    def encontrar_cortes_x(self, f):
        roots = fsolve(f, [1])
        return roots
    
    def graficar_funcion_y_cortes(self, f):
        x = np.linspace(-10, 10, 1000)
        y = f(x)
        plt.plot(x, y)

        roots = self.encontrar_cortes_x(f)
        plt.scatter(roots, np.zeros_like(roots))

        plt.grid()
        plt.show()