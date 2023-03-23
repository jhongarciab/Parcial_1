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
      return None
    else:
      resultado = []
      for i in range(self.shape[0]):
        fila = []
        for j in range(self.shape[1]):
          fila.append(self.valores[i][j] + otra.valores[i][j])
        resultado.append(fila)
      return Matriz(resultado)

  def __sub__(self, otra):
    if self.shape != otra.shape:
      print("Tamaños distintos. No es posible la resta")
      return None
    else:
      resultado = []
      for i in range(self.shape[0]):
        fila = []
        for j in range(self.shape[1]):
          fila.append(self.valores[i][j] - otra.valores[i][j])
        resultado.append(fila)
      return Matriz(resultado)

#Método para multiplicar por un escalar
  def escalar(self, e):
    if type(e) in [int, float]:
      resultado = [[0]*self.shape[1] for _ in range(self.shape[0])]
      for i in range(self.shape[0]):
        for j in range(self.shape[1]):
          resultado[i][j] = self.valores[i][j] * e
      return Matriz(resultado)
    else:
      print("El argumento pasado no es un número")
      return None
  
#Ahora defino mul y rmul para poder hacer las operaciones entre matrices al momento de G-J
  def __mul__(self, otra):
    if self.shape[1] != otra.shape[0]:
        print("Las matrices no pueden multiplicarse")
        return None
    resultado = [[0]*otra.shape[1] for _ in range(self.shape[0])] #Matriz llena de 0 con las mismas dimensiones para llevar a cabo las mult.
    for i in range(self.shape[0]):
        for j in range(otra.shape[1]):
            for k in range(self.shape[1]):
                resultado[i][j] += self.valores[i][k]*otra.valores[k][j]
    return Matriz(resultado)

  def __rmul__(self, otra):
    if self.shape[1] != otra.shape[0]:
        print("Las matrices no pueden multiplicarse")
        return None
    resultado = [[0]*otra.shape[1] for _ in range(self.shape[0])] #Matriz llena de 0 con las mismas dimensiones para llevar a cabo las mult.
    for i in range(self.shape[0]):
        for j in range(otra.shape[1]):
            for k in range(self.shape[1]):
                resultado[i][j] += self.valores[i][k]*otra.valores[k][j]
    return Matriz(resultado)

#Defino el intercambio de filas y luego para encontrar el pivote  
  def intercambio(self, fila1, fila2):
     self.valores[fila1], self.valores[fila2] = self.valores[fila2], self.valores[fila1]

  def pivote(self, fila):
    respuesta = self.valores[fila][fila]
    return respuesta

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
    resultado = [[0]*self.shape[0] for _ in range(self.shape[1])] #Se define la matriz transpuesta
    for i in range(self.shape[0]):
      for j in range(self.shape[1]):
        resultado[j][i] = self.valores[i][j] #Se intercambian las filas y columnas
    return Matriz(resultado)

m1 = Matriz([1,2,3,4], 2, 2)
print(m1)

m2 = Matriz([1,0,0,1], 2, 2)
print(m2)

m3 = m1 + m2
print(m3)


