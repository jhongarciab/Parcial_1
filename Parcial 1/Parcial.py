#Defino clase matriz, con vector por si es solo una fila, suma y resta.
class Matriz:
  def __init__(self, valores, n, m):
    self.valores = [valores[i:i+m] for i in range(0, n*m, m)]
    self.shape = [n, m]
    self.is_valid = self.validar_matriz()

  def validar_matriz(self):
    indices_invalidos = []
    for i in range(self.shape[0]):
      for j in range(self.shape[1]):
        if type(self.valores[i][j]) not in [int, float]:
          indices_invalidos.append((i,j))
    if len(indices_invalidos) == 0:
      return [True, []]
    else:
      return [False, indices_invalidos]

  def __str__(self):
    if self.shape[0] == 1:
      respuesta = self.vector_(0)
      return respuesta
    else:
      respuesta = ""
      for i in range(self.shape[0]-1):
        respuesta = respuesta + self.vector_(i) + "\n"
      respuesta = respuesta + self.vector_(self.shape[0]-1)
      return respuesta
    
  def vector_(self, fila):
    respuesta = "|"
    for i in range(self.shape[1]-1):
      respuesta = respuesta + str(self.valores[fila][i])
      respuesta = respuesta + " "
    respuesta = respuesta + str(self.valores[fila][-1]) + "|"
    return respuesta

  def __add__(self, otra):
    if self.shape != otra.shape:
      print("Tamaños distintos. No es posible la suma")
    
    resultado = []
    for i in range(self.shape[0]):
      fila = []
      for j in range(self.shape[1]):
        fila.append(self.valores[i][j] + otra.valores[i][j])
      resultado.append(fila)
    return Matriz([elem for fila in resultado for elem in fila], self.shape[0], self.shape[1])

  def __sub__(self, otra):
    if self.shape != otra.shape:
      print("Tamaños distintos. No es posible la resta")
    else:
      resultado = []
      for i in range(self.shape[0]):
        fila = []
        for j in range(self.shape[1]):
          fila.append(self.valores[i][j] - otra.valores[i][j])
        resultado.append(fila)
      return Matriz([elem for fila in resultado for elem in fila], self.shape[0], self.shape[1])

#Método para multiplicar por un escalar
  def escalar(self, e):
    if type(e) in [int, float]:
      resultado = [[0]*self.shape[1] for _ in range(self.shape[0])]
      for i in range(self.shape[0]):
        for j in range(self.shape[1]):
          resultado[i][j] = self.valores[i][j] * e
      return Matriz([elem for fila in resultado for elem in fila], self.shape[0], self.shape[1])
    else:
      print("Lo ingresado no es un escalar")
  
#Ahora defino mul y rmul para poder hacer las operaciones entre matrices al momento de G-J
  def __mul__(self, otra):
    if self.shape[1] != otra.shape[0]:
      print("Las matrices no pueden multiplicarse")
    resultado = [[0]*otra.shape[1] for _ in range(self.shape[0])] #Matriz llena de 0 con las mismas dimensiones para llevar a cabo las mult.
    for i in range(self.shape[0]):
      for j in range(otra.shape[1]):
        for k in range(self.shape[1]):
          resultado[i][j] += self.valores[i][k]*otra.valores[k][j]
    return Matriz([elem for fila in resultado for elem in fila], self.shape[0], otra.shape[1])

  def __rmul__(self, otra):
    if self.shape[1] != otra.shape[0]:
      print("Las matrices no pueden multiplicarse")
    resultado = [[0]*self.shape[1] for _ in range(otra.shape[0])] #Matriz llena de 0 con las mismas dimensiones para llevar a cabo las mult.
    for i in range(otra.shape[0]):
      for j in range(self.shape[1]):
        for k in range(otra.shape[1]):
          resultado[i][j] += otra.valores[i][k]*self.valores[k][j]
    return Matriz([elem for fila in resultado for elem in fila], self.shape[0], otra.shape[1])

#Defino el intercambio de filas y luego para encontrar el pivote  
  def intercambio(self, fila1, fila2):
     self.valores[fila1], self.valores[fila2] = self.valores[fila2], self.valores[fila1]

  def pivote(self, fila):
    for j in range(self.shape[1]):
      if abs(self.valores[fila][j]) > 0:
        return self.valores[fila][j]

#Gauss_Jordan unificada:
  def gauss_jordan(self):
    for i in range(self.shape[0]):
      pivote = self.pivote(i)
      for j in range(i + 1, self.shape[0]):
        multiplicador = self.valores[j][i] / pivote
        for k in range(i, self.shape[1]):
          self.valores[j][k] -= multiplicador * self.valores[i][k]
          
    for i in range(self.shape[0]-1, -1, -1):
      pivote = self.pivote(i)
      for j in range(i-1, -1, -1):
        multiplicador = self.valores[j][i] / pivote
        for k in range(i, self.shape[1]):
          self.valores[j][k] -= multiplicador * self.valores[i][k]

#Método para verificar si el sistema tiene una solución, infinitas o no tiene sol.   
  def tipo_sol(self):  
    num_variables = self.shape[1]-1
    pivotes = []
    for i in range(self.shape[0]):
      fila_de_ceros = True
      for j in range(num_variables):
        if self.valores[i][j] != 0:
          fila_de_ceros = False
          break
      if not fila_de_ceros:
        pivotes.append(j)

    if len(pivotes) == num_variables:
      return "El sistema tiene solución única"
    elif len(pivotes) < num_variables:
      return "El sistema tiene infinitas soluciones"
    elif len(pivotes) < num_variables and self.valores[i][-1] != 0:
      return "El sistema no tiene solución"
    
#Defino el vector resultado para el G-J.
  def vector_sol(self):
    self.gauss_jordan()
    n = self.shape[0]
    m = self.shape[1]
    x = [0] * n  #Lista de longitud 0 inicializada con ceros para almacenar las soluciones de los sistemas
    for i in range(n):
        if self.valores[i][i] != 0:
            x[i] = self.valores[i][m-1] / self.valores[i][i]
    return f"La solución del sistema es: {x}"

#Defino el método para la transpuesta.
  def transpuesta(self):
    resultado = [[0]*self.shape[0] for i in range(self.shape[1])]
    for i in range(self.shape[0]):
      for j in range(self.shape[1]):
        resultado[j][i] = self.valores[i][j]
    return Matriz([elem for fila in resultado for elem in fila], self.shape[0], self.shape[1])

#Defino el método para la simetría.
  def simetrica(self):
    transpuesta = self.transpuesta()
    if self.shape != transpuesta.shape:
        print("La matriz no es simétrica")
        return
    for i in range(self.shape[0]):
        for j in range(self.shape[1]):
            if self.valores[i][j] != transpuesta.valores[i][j]:
                print("La matriz no es simétrica")
                return
    print("La matriz es simétrica")

while True:
    print("---- Menú ----")
    print("1. Sumar/Restar matrices")
    print("2. Multiplicación entre matrices o por escalar")
    print("3. Solución de sistemas mediante Gauss-Jordan")
    print("4. Transpuesta de una matriz")
    print("5. Simetría de una matriz")
    print("6. Salir")

    seleccion = input("Seleccione una opción: ")

    if seleccion == "1":
        print("---- Suma/Resta de matrices ----")
        print("Ingrese la primera matriz")
        print("Ingrese el número de filas y columnas de la primera matriz")
        num_filas1 = int(input("Filas: "))
        num_columnas1 = int(input("Columnas: "))
        print("Ingrese los valores de la primera matriz separados por comas")
        valores1 = [int(x) for x in input().split(',')]
        matriz1 = Matriz(valores1, num_filas1, num_columnas1)
        print("Ingrese la segunda matriz")
        print("Ingrese el número de filas y columnas de la segunda matriz")
        num_filas2 = int(input("Filas: "))
        num_columnas2 = int(input("Columnas: "))
        print("Ingrese los valores de la segunda matriz separados por comas")
        valores2 = [int(x) for x in input().split(',')]
        matriz2 = Matriz(valores2, num_filas2, num_columnas2)
        print("La matriz 1 es: ")
        print(matriz1)
        print("La matriz 2 es: ")
        print(matriz2)
        print("¿Qué desea hacer?")
        print("1. Sumar")
        print("2. Restar")
        seleccion = input("Seleccione una opción: ")
        if seleccion == "1":
            print("La suma de las matrices es: ")
            print(matriz1 + matriz2)
        elif seleccion == "2":
            print("La resta de las matrices es: ")
            print(matriz1 - matriz2)
        else:
            print("Opción inválida, intente de nuevo.")

    elif seleccion == "2":
        print("---- Multiplicación de matrices ----")
        print("Ingrese el número de filas y columnas de la primera matriz")
        num_filas1 = int(input("Filas: "))
        num_columnas1 = int(input("Columnas: "))
        print("Ingrese los valores de la primera matriz separados por comas")
        valores1 = [int(x) for x in input().split(',')]
        matriz1 = Matriz(valores1, num_filas1, num_columnas1)
        print("Ingrese la segunda matriz")
        print("Ingrese el número de filas y columnas de la segunda matriz")
        num_filas2 = int(input("Filas: "))
        num_columnas2 = int(input("Columnas: "))
        print("Ingrese los valores de la segunda matriz separados por comas")
        valores2 = [int(x) for x in input().split(',')]
        matriz2 = Matriz(valores2, num_filas2, num_columnas2)
        print("La matriz 1 es: ")
        print(matriz1)
        print("La matriz 2 es: ")
        print(matriz2)
        print("¿Qué desea hacer?")
        print("1. Multiplicar")
        print("2. Multiplicar por escalar")
        seleccion = input("Seleccione una opción: ")
        if seleccion == "1":
            print(matriz1 * matriz2)
        elif seleccion == "2":
            e = int(input("Ingrese el escalar: "))
            print("¿Qué matriz desea multiplicar por el escalar?")
            print("1. Matriz 1")
            print("2. Matriz 2")
            seleccion = input("Seleccione una opción: ")
            if seleccion == "1":
                print(matriz1.escalar(e))
            elif seleccion == "2":
                print(matriz2.escalar(e))
        else:
            print("Opción inválida, intente de nuevo.")

    elif seleccion == "3":
        print("---- Gauss-Jordan de una matriz ----")
        print("Ingrese el número de filas y columnas de la matriz")
        num_filas = int(input("Filas: "))
        num_columnas = int(input("Columnas: "))
        print("Ingrese los valores de la matriz separados por comas")
        valores = [int(x) for x in input().split(',')]
        matriz = Matriz(valores, num_filas, num_columnas)
        print("La matriz es: ") 
        print(matriz)
        print(matriz.gauss_jordan())
        print(matriz.vector_sol())
        print(matriz.tipo_sol())

    elif seleccion == "4":
        print("---- Transpuesta de una matriz ----")
        print("Ingrese el número de filas y columnas de la matriz")
        num_filas = int(input("Filas: "))
        num_columnas = int(input("Columnas: "))
        print("Ingrese los valores de la matriz separados por comas")
        valores = [int(x) for x in input().split(',')]
        matriz = Matriz(valores, num_filas, num_columnas)
        print("La matriz es: ") 
        print(matriz)
        print("La transpuesta de la matriz es: ")
        print(matriz.transpuesta())

    elif seleccion == "5":
        print("---- Simetría de una matriz ----")
        print("Ingrese el número de filas y columnas de la matriz")
        num_filas = int(input("Filas: "))
        num_columnas = int(input("Columnas: "))
        print("Ingrese los valores de la matriz separados por comas")
        valores = [int(x) for x in input().split(',')]
        matriz = Matriz(valores, num_filas, num_columnas)
        print("La matriz es: ")
        print(matriz)
        S = matriz.simetrica()
        print(S)
        
    elif seleccion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente de nuevo.")