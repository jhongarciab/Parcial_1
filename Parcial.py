#Defino clase matriz, con vector por si es solo una fila, suma y resta.
class Matriz:
  def __init__(self, valores):
    self.valores = valores
    n = len(valores)
    m = len(valores[0])
    self.shape = [n, m]

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
      print("Tamaños distintos. No es posible la suma")
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

#Primero aplicar Gauss, para la matriz escalonada, luego Jordan:
  def gauss(self):
    for i in range(self.shape[0]):
      pivote = self.pivote(i)
      for j in range(i + 1, self.shape[0]):
        multiplicador = self.valores[j][i] / pivote
        for k in range(i, self.shape[1]):
          self.valores[j][k] -= multiplicador * self.valores[i][k]

V1 = Matriz([[2, 2, 3], [4, 5, 6], [7, 8, 9]])
print("La matriz 1 es: ")
print(V1)
V2 = Matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("La matriz 2 es: ")
print(V2)
print("La suma es: ")
print(V1+V2)
print("La resta es: ")
print(V1-V2)
print("La multiplicación es: ")
print(V2*V1)
print("La multiplicación por un escalar es: ")
V3 = V1.escalar(2)
print(V3)
print("La matriz 1 después de aplicar Gauss es: ")
V1.gauss()
print(V1)
print("La matriz 2 después de aplicar Gauss es: ")
V2.gauss()
print(V2)

