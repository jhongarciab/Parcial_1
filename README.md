# Parcial \#1
## Marzo, 2023
Parcial número 1:

- Construya un programa que tenga una clase matriz (puede hacerlo con base en lo realizado en clase) que tenga un método implementado para 
solucionar un sistema de ecuaciones por el método Gauss-Jordan. La dimensión de la matriz es arbitraria y el programa debe decir si tiene 
solución única, infinitas soluciones o única solución. La clase debe tener un atributo llamado is valid que es una lista cuyo primer elemento 
es un Booleando indicando si todos los elementos de la matriz son números o hay algún dato inválido. Si el booleano es True, el segundo elemento 
de la lista sería una liusta vacía, si es False, el segundo elemento de la lista será una lista con los Indices de los elementos de la matriz 
que están incorrectos. Ayuda: Si desea hagalo con un N máximo de 5

- Organice el ejemplo desarrollado en clase (el de matrices) para que los vectores puedan ser ingresados como una sola lista y no como lista de listas.
Defina el producto entre matrices, vectores y escalares usando __mul__ y __rmul__ y defina un método para calcular la transpuesta de una matriz y otro uno para
determinar si es simétrica.