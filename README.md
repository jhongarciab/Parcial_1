<h1 align="center">Parcial 1</h1>

**Programa de Física, Universidad del Quindío, Marzo, 2023.**

**Estudiante:** Jhon Sebastian García Barrera.

1. Construya un programa que tenga una clase matriz (puede hacerlo con base en lo realizado en clase) que tenga un método implementado para solucionar un sistema de ecuaciones por el método Gauss-Jordan. La dimensión de la matriz es arbitraria y el programa debe decir si tiene solución única, infinitas soluciones o única solución. La clase debe tener un atributo llamado is valid que es una lista cuyo primer elemento es un Booleando indicando si todos los elementos de la matriz son números o hay algún dato inválido. Si el booleano es True, el segundo elemento de la lista sería una liusta vacía, si es False, el segundo elemento de la lista será una lista con los Indices de los elementos de la matriz que están incorrectos. Ayuda: Si desea hagalo con un N máximo de 5
2. Organice el ejemplo desarrollado en clase (el de matrices) para que los vectores puedan ser ingresados como una sola lista y no como lista de listas.Defina el producto entre matrices, vectores y escalares usando __mul__ y __rmul__ y defina un método para calcular la transpuesta de una matriz y otro uno para determinar si es simétrica.

<h1 align="center">Bitácora</h1>

El primer día se llevó a cabo el código para matrices cuadradas desde 2x2 hasta 5x5. Un código largo (400 líneas aprox.) pero no difícil, el cual fue una pérdida de tiempo ya que no era útil, pues, el método Gauss-Jordan se puede aplicar no necesariamente a matrices cuadradas y además de eso, solo con un n de 2 hasta 5, por lo que se definió las matrices nxm, con suma y resta de una manera arbitraria usando for anidados. Hasta ahora ha sido lo más demorado, el hecho de entender bien la lógica para desarrollar esa definición desde cero.
Se implementó mul y rmul para llevar a cabo las multiplicaciones entre matrices y escalares, primero fue esto ya que para el método G-J es necesario la multiplicación.

Por ahora la proyección es primero definir un método para intercambiar filas, luego hacer gauss por aparte y luego hacer el jordan. Lo que se lleva hasta ahora no ha sido probado en ejemplos, voy suponiendo que el código funciona de buena manera así, después nos ocupamos de los errores que vayan saliendo. Hecho el intercambio de filas, al empezar con Gauss fue necesario primero añadir un método para encontrar el pivote, pues es necesario para seguir. Hecho Gauss, voy a proceder a hacer pruebas tanto de imprensión, suma, resta, multiplicación, intercambio de líneas y luego Gauss, para no tener problemas en un futuro con errores en conjunto.

El primer error sale a la luz, al momento de sumar y restar, la suma funcionó de manera correcta pero la resta no funcionó. El problema no se debía directamente al código, pasaba que si se imprimía una primero que la otra, esa última no servía, aún no se soluciona esto. Al final el problema sí estuvo en el código, lo que hice fue modificar tanto el código de add como el de sub, añadiendo una nueva lista donde se agregarían los valores calculados de la nueva matriz y ya funcionó.