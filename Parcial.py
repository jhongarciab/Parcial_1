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
    if self.shape[0] == 1:
      lista = []
      for i in range(self.shape[1]):
        lista.append(self.valores[0][i] + otra.valores[0][i])
      respuesta = Matriz([lista])
      return respuesta
    elif self.shape != otra.shape:
      print("Tamaños distintos. No es posible la suma")
    else: 
      respuesta = self.valores
      for i in range(self.shape[0]):
        for j in range(self.shape[1]):
          respuesta[i][j] = self.valores[i][j] + otra.valores[i][j]
      respuesta = Matriz(respuesta)
      return respuesta

  def __sub__(self, otra):
    if self.shape[0] == 1:
      lista = []
      for i in range(self.shape[1]):
        lista.append(self.valores[0][i] - otra.valores[0][i])
      respuesta = Matriz([lista])
      return respuesta
    elif self.shape != otra.shape:
      print("Tamaños distintos. No es posible la resta")
    else: 
      respuesta = self.valores
      for i in range(self.shape[0]):
        for j in range(self.shape[1]):
          respuesta[i][j] = self.valores[i][j] - otra.valores[i][j]
      respuesta = Matriz(respuesta)
      return respuesta

#Ahora defino mul y rmul para poder hacer las operaciones entre matrices al momento de G-J
  def __mul__(self, otra):
    if self.shape[0] != otra.shape[1]:
        print("Las matrices no pueden multiplicarse")
        return None
    resultado = [[0]*otra.shape[1] for _ in range(self.shape[0])] #Matriz llena de 0 con las mismas dimensiones para llevar a cabo las mult.
    for i in range(self.shape[0]):
        for j in range(otra.shape[1]):
            for k in range(self.shape[1]):
                resultado[i][j] += self.valores[i][k]*otra.valores[k][j]
    return Matriz(resultado)

  def __rmul__(self, otra):
    if self.shape[0] != otra.shape[1]:
        print("Las matrices no pueden multiplicarse")
        return None
    resultado = [[0]*otra.shape[1] for _ in range(self.shape[0])] #Matriz llena de 0 con las mismas dimensiones para llevar a cabo las mult.
    for i in range(self.shape[0]):
        for j in range(otra.shape[1]):
            for k in range(self.shape[1]):
                resultado[i][j] += self.valores[i][k]*otra.valores[k][j]
    return Matriz(resultado)
  
  def intercambio(self, fila1, fila2):
     self.valores[fila1], self.valores[fila2] = self.valores[fila2], self.valores[fila1]

#Primero aplicar Gauss, luego Jordan:
  def gauss(matriz):
    for i in range(len(matriz)):
      pivote = matriz[i][i]
      if pivote == 0:
        continue
      for j in range(i+1) 
     
