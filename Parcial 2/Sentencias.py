class SentenciasSQL:
    _SELECCIONAR = 'SELECT {}, {} FROM {}'
    _INSERTAR = 'INSERT INTO {} ({}) VALUES({})'
    _ACTUALIZAR = 'UPDATE {} SET {} WHERE {} = %s'
    _ELIMINAR = 'DELETE FROM {} WHERE {} = %s'
    _TABLA = 'CREATE TABLE {} ({})'
    _CONSULTA = 'SELECT {} FROM {}'