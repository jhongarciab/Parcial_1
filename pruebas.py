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

        valores_suma = []
        for i in range(self.shape[0]):
            fila_suma = []
            for j in range(self.shape[1]):
                fila_suma.append(self.valores[i][j] + otra.valores[i][j])
            valores_suma.append(fila_suma)
        return Matriz([elem for fila in valores_suma for elem in fila], self.shape[0], self.shape[1])
    
    def __sub__(self, otra):
        if self.shape != otra.shape:
            print("Tamaños distintos. No es posible la resta")
            return None

        valores_suma = []
        for i in range(self.shape[0]):
            fila_suma = []
            for j in range(self.shape[1]):
                fila_suma.append(self.valores[i][j] - otra.valores[i][j])
            valores_suma.append(fila_suma)
        return Matriz([elem for fila in valores_suma for elem in fila], self.shape[0], self.shape[1])
    
    def escalar(self, e):
        if type(e) in [int, float]:
            resultado = [[0]*self.shape[1] for _ in range(self.shape[0])]
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    resultado[i][j] = self.valores[i][j] * e
            return Matriz([elem for fila in resultado for elem in fila], self.shape[0], self.shape[1])
        else:
            print("Lo ingresado no es un escalar")
            return None
        
    def __mul__(self, otra):
        if self.shape[1] != otra.shape[0] and otra.shape[1] != self.shape[0]:
            print("Las matrices no pueden multiplicarse")
            return None
        resultado = [[0]*otra.shape[1] for _ in range(otra.shape[0])] #Matriz llena de 0 con las mismas dimensiones para llevar a cabo las mult.
        for i in range(self.shape[0]):
            for j in range(otra.shape[1]):
                for k in range(self.shape[1]):
                    resultado[i][j] += self.valores[i][k]*otra.valores[k][j]
        return Matriz([elem for fila in resultado for elem in fila], self.shape[0], otra.shape[1])

    def __rmul__(self, otra):
        if self.shape[1] != otra.shape[0] and otra.shape[1] != self.shape[0]:
            print("Las matrices no pueden multiplicarse")
            return None
        resultado = [[0]*self.shape[1] for _ in range(otra.shape[0])] #Matriz llena de 0 con las mismas dimensiones para llevar a cabo las mult.
        for i in range(otra.shape[0]):
            for j in range(self.shape[1]):
                for k in range(otra.shape[1]):
                    resultado[i][j] += otra.valores[i][k]*self.valores[k][j]
        return Matriz([elem for fila in resultado for elem in fila], otra.shape[0], self.shape[1])



print("La matriz es: ")
A = Matriz([1, 2, 3 ,4, 1, 3], 2, 3)
print(A)
print("La matriz es: ")
B = Matriz([1, 2, 3 ,4, 1, 3], 3, 2)
print(B)

print("La matriz-suma es: ")
c = A - B
print(c)

print("La matriz-suma es: ")
d = A + B
print(d)

print("La multiplicación por escalar es: ")
f = A.escalar(2)
print(f)

print("La multiplicación entre matrices es: ")
j = B * A
print(j)


