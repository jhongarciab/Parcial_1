<h1 align="center">Parcial 2 😥</h1> 

1. Construya una clase que pueda recibir como argumentos al momento de definirla el nombre de uno o varios archivos y opcionalmente la ubicación de cada uno. Si no se ingresa la ruta de algun archivo el programa supone que es la ruta actual y lee todos los archivos de datos. Si no se le ingresa el nombre de ningún archivo, el programa debe generara la base de datos.

2. Las bases de datos que lee el programa las debe conseguir (O modificar alguna existente dividiendola en varios archivos) y deben tener varias columnas con el mismo nombre. Al leer las bases de datos se genera una única tabla de datos con las columnas comunes y los datos de todos los archivos. La tabla final no puede tener filas que tengan en común más de tres valores (Solo se dejaría uno de ellos por considerarse datos repetidos).

3. La clase debe tener un método que reciba condiciones para los datos numéricos y filtre los datos de la tabla con base en esa condición.

4.  La clase debe tener un método que reciba condiciones para los datos tipo cadena y filtre los datos de la tabla con base en esa condición.

5. La clase debe tener un método que calcule los coeficientes de regresión lineal para dos columnas elegidas por el usuario. (Si hace regresión multi-lineal gana puntos adicionales, si la hace multi-lineal con regularización, gana aún más puntos adicionales)

6. Grafique el resultado del numeral anterior. En scatter los valores de la tabla y en línea la regresión lineal.

7. Realice un método o una función que al recibir una función matemática definida a partir de una lambda, encuentre los cortes con el eje x, grafique la función y ponga en scatter los puntos solución.

8. Defina y use al menos dos decoradores

9. Use *args y **kwargs

10. Documente TODAS las funciones y métodos

<h1 align="center">Bitácora</h1>

Lo primero que se realizó fue la creación de la clase, en este caso 'Conexión', la cual recibe como parámetros el nombre de los archivos y la ruta de los mismos. En una primera instancia sólo se realizó para un archivo. La idea de este parcial es ir paso a paso y modificando el código al ritmo, por lo que luego del init de la clase, donde los siete argumentos, cinco eran fijos, ya que era la conexión local del servidor de PostgreSQL, los otros dos eran la ruta de los archivos, la cual debe ingresar la consola y el nombre que va a tener la tabla. 

Después de esto se creó el método 'crear_tabla', el cual se encarga de crear la tabla en la base de datos, lo primero que hace es la conexión, usando el with para evitar la fuga y asegurar el buen cierre del cursos a la hora de ejecutar las secuencias. Luego de esto, en el init, como es requisito del parcial que si no se le ingresa un archivo, pueda leer los archivos que hay en la misma carpeta, se añadió un condicional que si no se le ingresa un archivo, lea todos los archivos de la carpeta y en el def de crear tabla, se añadió un for que recorra todos los archivos que se encuentren en la carpeta, los lea y cree la tabla de cada uno.
