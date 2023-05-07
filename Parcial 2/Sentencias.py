class SentenciasSQL:
    _SELECCIONAR = 'SELECT {}, {} FROM {}'
    _INSERTAR = 'INSERT INTO {} ({}) VALUES({})'
    _ACTUALIZAR = 'UPDATE {} SET {} WHERE {} = %s'
    _ELIMINAR = 'DELETE FROM {} WHERE {} = %s'
    _TABLA = 'CREATE TABLE {} ({})'
    _CONSULTA = 'SELECT {} FROM {}'
    _LISTAR_TABLAS = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
    _LISTAR_COLUMNAS = "SELECT column_name FROM information_schema.columns WHERE table_name = '{}'"