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
        """
        Inicializa una instancia de la clase Conexión. Si no se especifican los archivos, se toman todos los archivos.
        """
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
        """
        Crea una tabla en la base de datos con el nombre especificado en la instancia de la clase Conexión
        y los datos de los archivos CSV especificados en la instancia de la clase Conexión.
        """
        with CursorDelPool() as cursor:
            for i, j in enumerate(self.archivos):
                nombre_tabla = self.nombre_tabla[i]
                df = pd.read_csv(j)
                columnas = [f'"{i.lower()}" VARCHAR(255)' for i in df.columns]
                cursor.execute(SentenciasSQL._TABLA.format(nombre_tabla, ', '.join(columnas)))
                for _, row in df.iterrows():
                    valores = [f"'{i}'" for i in row.values.tolist()]
                    cursor.execute(SentenciasSQL._INSERTAR.format(nombre_tabla, ', '.join([f'{i.lower()}' for i in df.columns]), ', '.join(valores)))
                              
        print(f"Las tablas '{', '.join(self.nombre_tabla)}' han sido creadas y los datos han sido insertados.")

    def combinar_tablas(self):
        """
        Combina los datos de los archivos CSV especificados en la instancia de la clase Conexión en un solo DataFrame.
        """
        dfs = []
        for i in self.archivos:
            df = pd.read_csv(i)
            dfs.append(df)
        df_combinado = pd.concat(dfs, axis=0, join='inner')
        df_combinado = df_combinado.drop_duplicates(subset=df_combinado.columns[:3])
        return df_combinado

    def crear_tabla_combinada(self, df_combinado):
        """
        Crea una nueva tabla en la base de datos y la inserta con los datos combinados
        en el DataFrame df_combinado.
        """
        with CursorDelPool() as cursor:
            for nombre_tabla in self.nombre_tabla:
                columnas = [f'"{i.lower()}" VARCHAR(255)' for i in df_combinado.columns]
                cursor.execute(SentenciasSQL._TABLA.format(nombre_tabla, ', '.join(columnas)))
                
                for _, row in df_combinado.iterrows():
                    valores = [f"'{i}'" for i in row.values.tolist()]
                    cursor.execute(SentenciasSQL._INSERTAR.format(nombre_tabla, ', '.join([f'{i.lower()}' for i in df_combinado.columns]), ', '.join(valores)))
            
        print(f"Las tablas '{', '.join(self.nombre_tabla)}' han sido creadas y los datos han sido insertados.")

    def crear_grafico_regresion(self, columna_x, columna_y, *args, **kwargs):
        """
        Crea un gráfico de regresión lineal usando seaborn. Los parámetros *args y **kwargs son pasados a la función.
        """
        with CursorDelPool() as cursor:
            conn = cursor.connection
            df = pd.read_sql(SentenciasSQL._SELECCIONAR.format(columna_x, columna_y, self.nombre_tabla), conn)
        print(f'Los datos son los siguientes: {df}')
        df[columna_x] = pd.to_numeric(df[columna_x], errors='coerce')
        df[columna_y] = pd.to_numeric(df[columna_y], errors='coerce')
        sns.regplot(x=columna_x, y=columna_y, data=df, *args, **kwargs)
        plt.title(f'Regresión lineal entre {columna_x} y {columna_y}')
        plt.show()

    def obtener_nombres_tablas(self):
        """
        Retorna una lista con los nombres de las tablas en la base de datos.
        """
        with CursorDelPool() as cursor:
            cursor.execute(SentenciasSQL._LISTAR_TABLAS)
            tablas = [tabla[0] for tabla in cursor.fetchall()]
        return tablas

    def obtener_nombres_columnas(self):
        """
        Retorna una lista con los nombres de las columnas de la tabla actual en la base de datos.
        """
        with CursorDelPool() as cursor:
            cursor.execute(SentenciasSQL._LISTAR_COLUMNAS.format(self.nombre_tabla))
            columnas = [columna[0] for columna in cursor.fetchall()]
        return columnas

class FuncionMatematica():
    """
    Clase que permite encontrar los cortes de una función matemática y graficarla.
    """
    def encontrar_cortes_x(self, f):
        raices = fsolve(f, [1])
        return raices
    
    def graficar_funcion_y_cortes(self, f):
        x = np.linspace(-10, 10, 1000)
        y = f(x)
        plt.plot(x, y)
        raices = self.encontrar_cortes_x(f)
        plt.scatter(raices, np.zeros_like(raices))
        plt.grid()
        plt.show()