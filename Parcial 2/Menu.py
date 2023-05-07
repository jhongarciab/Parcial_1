from Main import Base
from Main import FuncionMatematica
import os

while True:
    print('--------- Menú ---------')
    print('1. Ingresar archivos')
    print('2. Crear gráfico de regresión')
    print('3. Crear gráfico de función matemática')
    print('4. Salir')
    opcion = input('Ingrese una opción: ')

    if opcion == '1':
        archivos_en_carpeta = os.listdir()
        archivos_validos = [i for i in archivos_en_carpeta if os.path.isfile(i) and i.endswith('.csv')]

        if archivos_validos:
            print("Archivos disponibles en la carpeta actual:")
            for i, archivo in enumerate(archivos_validos):
                print(f"{i+1}. {archivo}")
            
            numeros_archivos = input('Ingrese los números de los archivos que desea utilizar separados por coma (o presione Enter para usar todos los archivos disponibles): ')
            if numeros_archivos == '':
                nombres_archivos = archivos_validos
            else:
                nombres_archivos = [archivos_validos[int(i)-1] for i in numeros_archivos.split(',')]
            
            nombre_tabla = input('Ingrese el nombre de la tabla: ').split(',')
            conexion = Base(nombres_archivos, nombre_tabla)

            combinar = input('¿Desea combinar los archivos? (s/n): ')
            if combinar == 's':
                df_combinado = conexion.combinar_tablas()
                conexion.crear_tabla_combinada(df_combinado)
            else:
                conexion.crear_tabla()
        else:
            print("No hay archivos válidos en la carpeta actual.")

    
    elif opcion == '2':
        print("Tablas disponibles:")
        conexion = Base()
        tablas = conexion.obtener_nombres_tablas()
        for i, tabla in enumerate(tablas):
            print(f"{i+1}. {tabla}")
        opcion_tabla = input('Ingrese el número de la tabla que desea utilizar: ')
        nombre_tabla = tablas[int(opcion_tabla)-1]
        conexion = Base(nombre_tabla=nombre_tabla)
        columna_x = input('Ingrese el nombre de la primera columa: ')
        columna_y = input('Ingrese el nombre de la segunda columna: ')
        conexion.crear_grafico_regresion(columna_x, columna_y)

    elif opcion == '3':
        fm = FuncionMatematica()
        funcion_str = input('Ingrese la función que desea graficar: ')
        funcion = eval('lambda x: ' + funcion_str)
        fm.graficar_funcion_y_cortes(funcion)

    elif opcion == '4':
        break

print("¡Hasta luego!")