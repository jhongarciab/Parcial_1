while True:
  tamaño = input("¿Con qué tamaño de matriz quiere trabajar? (2x2 hasta 5x5) Nota: Escriba salir para terminar: ")

  if tamaño == "salir":
        break

  elif tamaño == "2x2":
    class Matriz:
      def _init_(self, lista):
        self.a00=lista[0][0]
        self.a01=lista[0][1]
        self.a10=lista[1][0]
        self.a11=lista[1][1]

      def _str_(self):
        return "|{:^5} {:^5}|\n|{:^5} {:^5}|".format(self.a00, self.a01, self.a10, self.a11)

      def _add_(self, otro):
        a00 = self.a00 + otro.a00
        a01 = self.a01 + otro.a01
        a10 = self.a10 + otro.a10
        a11 = self.a11 + otro.a11
        return Matriz([[a00, a01], [a10, a11]])

      def _sub_(self, otro):
        a00 = self.a00 - otro.a00
        a01 = self.a01 - otro.a01
        a10 = self.a10 - otro.a10
        a11 = self.a11 - otro.a11
        return Matriz([[a00, a01], [a10, a11]])

      def _mul_(self, otro):
        a00 = self.a00 * otro
        a01 = self.a01 * otro
        a10 = self.a10 * otro
        a11 = self.a11 * otro
        return Matriz([[a00, a01], [a10, a11]])

      def _rmul_(self, otro):
        a00 = self.a00 * otro
        a01 = self.a01 * otro
        a10 = self.a10 * otro
        a11 = self.a11 * otro
        return Matriz([[a00, a01], [a10, a11]])

  elif tamaño == "3x3":
    class Matriz:
      def _init_(self, lista):
        self.a00=lista[0][0]
        self.a01=lista[0][1]
        self.a02=lista[0][2]
        self.a10=lista[1][0]
        self.a11=lista[1][1]
        self.a12=lista[1][2]
        self.a20=lista[2][0]
        self.a21=lista[2][1]
        self.a22=lista[2][2]

      def _str_(self):
        return "|{:^5} {:^5} {:^5}|\n|{:^5} {:^5} {:^5}|\n|{:^5} {:^5} {:^5}|".format(self.a00, self.a01, self.a02, self.a10, self.a11, self.a12, self.a20, self.a21, self.a22)

      def _add_(self, otro):
        a00 = self.a00 + otro.a00
        a01 = self.a01 + otro.a01
        a02 = self.a02 + otro.a02
        a10 = self.a10 + otro.a10
        a11 = self.a11 + otro.a11
        a12 = self.a12 + otro.a12
        a20 = self.a20 + otro.a20
        a21 = self.a21 + otro.a21
        a22 = self.a22 + otro.a22
        return Matriz([[a00, a01, a02], [a10, a11, a12], [a20, a21, a22]])

      def _sub_(self, otro):
        a00 = self.a00 - otro.a00
        a01 = self.a01 - otro.a01
        a02 = self.a02 - otro.a02
        a10 = self.a10 - otro.a10
        a11 = self.a11 - otro.a11
        a12 = self.a12 - otro.a12
        a20 = self.a20 - otro.a20
        a21 = self.a21 - otro.a21
        a22 = self.a22 - otro.a22
        return Matriz([[a00, a01, a02], [a10, a11, a12], [a20, a21, a22]])

      def _mul_(self, otro):
        a00 = self.a00 * otro
        a01 = self.a01 * otro
        a02 = self.a02 * otro
        a10 = self.a10 * otro
        a11 = self.a11 * otro
        a12 = self.a12 * otro
        a20 = self.a20 * otro
        a21 = self.a21 * otro
        a22 = self.a22 * otro
        return Matriz([[a00, a01, a02], [a10, a11, a12], [a20, a21, a22]])

      def _rmul_(self, otro):
        a00 = self.a00 * otro
        a01 = self.a01 * otro
        a02 = self.a02 * otro
        a10 = self.a10 * otro
        a11 = self.a11 * otro
        a12 = self.a12 * otro
        a20 = self.a20 * otro
        a21 = self.a21 * otro
        a22 = self.a22 * otro
        return Matriz([[a00, a01, a02], [a10, a11, a12], [a20, a21, a22]])

  elif tamaño == "4x4":
      class Matriz:
        def _init_(self, lista):
          self.a00=lista[0][0]
          self.a01=lista[0][1]
          self.a02=lista[0][2]
          self.a03=lista[0][3]
          self.a10=lista[1][0]
          self.a11=lista[1][1]
          self.a12=lista[1][2]
          self.a13=lista[1][3]
          self.a20=lista[2][0]
          self.a21=lista[2][1]
          self.a22=lista[2][2]
          self.a23=lista[2][3]
          self.a30=lista[3][0]
          self.a31=lista[3][1]
          self.a32=lista[3][2]
          self.a33=lista[3][3]

        def _str_(self):
          return "|{:^5} {:^5} {:^5} {:^5}|\n|{:^5} {:^5} {:^5} {:^5}|\n|{:^5} {:^5} {:^5} {:^5}|\n|{:^5} {:^5} {:^5} {:^5}|".format(self.a00, self.a01, self.a02, self.a03, self.a10, self.a11, self.a12, self.a13, self.a20, self.a21, self.a22, self.a23, self.a30, self.a31, self.a32, self.a33)


        def _add_(self, otro):
          a00 = self.a00 + otro.a00
          a01 = self.a01 + otro.a01
          a02 = self.a02 + otro.a02
          a03 = self.a03 + otro.a03
          a10 = self.a10 + otro.a10
          a11 = self.a11 + otro.a11
          a12 = self.a12 + otro.a12
          a13 = self.a13 + otro.a13
          a20 = self.a20 + otro.a20
          a21 = self.a21 + otro.a21
          a22 = self.a22 + otro.a22
          a23 = self.a23 + otro.a23
          a30 = self.a30 + otro.a30
          a31 = self.a31 + otro.a31
          a32 = self.a32 + otro.a32
          a33 = self.a33 + otro.a33
          return Matriz([[a00, a01, a02, a03], [a10, a11, a12, a13], [a20, a21, a22, a23], [a30, a31, a32, a33]])

        def _sub_(self, otro):
          a00 = self.a00 - otro.a00
          a01 = self.a01 - otro.a01
          a02 = self.a02 - otro.a02
          a03 = self.a03 - otro.a03
          a10 = self.a10 - otro.a10
          a11 = self.a11 - otro.a11
          a12 = self.a12 - otro.a12
          a13 = self.a13 - otro.a13
          a20 = self.a20 - otro.a20
          a21 = self.a21 - otro.a21
          a22 = self.a22 - otro.a22
          a23 = self.a23 - otro.a23
          a30 = self.a30 - otro.a30
          a31 = self.a31 - otro.a31
          a32 = self.a32 - otro.a32
          a33 = self.a33 - otro.a33
          return Matriz([[a00, a01, a02, a03], [a10, a11, a12, a13], [a20, a21, a22, a23], [a30, a31, a32, a33]])

        def _mul_(self, otro):
          a00 = self.a00 * otro
          a01 = self.a01 * otro
          a02 = self.a02 * otro
          a03 = self.a03 * otro
          a10 = self.a10 * otro
          a11 = self.a11 * otro
          a12 = self.a12 * otro
          a13 = self.a13 * otro
          a20 = self.a20 * otro
          a21 = self.a21 * otro
          a22 = self.a22 * otro
          a23 = self.a23 * otro
          a30 = self.a30 * otro
          a31 = self.a31 * otro
          a32 = self.a32 * otro
          a33 = self.a33 * otro
          return Matriz([[a00, a01, a02, a03], [a10, a11, a12, a13], [a20, a21, a22, a23], [a30, a31, a32, a33]])

        def _rmul_(self, otro):
          a00 = self.a00 * otro
          a01 = self.a01 * otro
          a02 = self.a02 * otro
          a03 = self.a03 * otro
          a10 = self.a10 * otro
          a11 = self.a11 * otro
          a12 = self.a12 * otro
          a13 = self.a13 * otro
          a20 = self.a20 * otro
          a21 = self.a21 * otro
          a22 = self.a22 * otro
          a23 = self.a23 * otro
          a30 = self.a30 * otro
          a31 = self.a31 * otro
          a32 = self.a32 * otro
          a33 = self.a33 * otro
          return Matriz([[a00, a01, a02, a03], [a10, a11, a12, a13], [a20, a21, a22, a23], [a30, a31, a32, a33]])

  elif tamaño == "5x5":
      class Matriz:
        def _init_(self, lista):
          self.a00=lista[0][0]
          self.a01=lista[0][1]
          self.a02=lista[0][2]
          self.a03=lista[0][3]
          self.a04=lista[0][4]
          self.a10=lista[1][0]
          self.a11=lista[1][1]
          self.a12=lista[1][2]
          self.a13=lista[1][3]
          self.a14=lista[1][4]
          self.a20=lista[2][0]
          self.a21=lista[2][1]
          self.a22=lista[2][2]
          self.a23=lista[2][3]
          self.a24=lista[2][4]
          self.a30=lista[3][0]
          self.a31=lista[3][1]
          self.a32=lista[3][2]
          self.a33=lista[3][3]
          self.a33=lista[3][4]
          self.a40=lista[4][0]
          self.a41=lista[4][1]
          self.a42=lista[4][2]
          self.a43=lista[4][3]
          self.a43=lista[4][4]

        def _str_(self):
          return "|{:^5} {:^5} {:^5} {:^5} {:^5}|\n|{:^5} {:^5} {:^5} {:^5} {:^5}|\n|{:^5} {:^5} {:^5} {:^5} {:^5}|\n|{:^5} {:^5} {:^5} {:^5} {:^5}|\n|{:^5} {:^5} {:^5} {:^5} {:^5}".format(self.a00, self.a01, self.a02, self.a03, self.a04, self.a10, self.a11, self.a12, self.a13, self.a14, self.a20, self.a21, self.a22, self.a23, self.a24, self.a30, self.a31, self.a32, self.a33, self.a34, self.a40, self.a41, self.a42, self.a43, self.a44)

        def _add_(self, otro):
          a00 = self.a00 + otro.a00
          a01 = self.a01 + otro.a01
          a02 = self.a02 + otro.a02
          a03 = self.a03 + otro.a03
          a04 = self.a04 + otro.a04
          a10 = self.a10 + otro.a10
          a11 = self.a11 + otro.a11
          a12 = self.a12 + otro.a12
          a13 = self.a13 + otro.a13
          a14 = self.a14 + otro.a14
          a20 = self.a20 + otro.a20
          a21 = self.a21 + otro.a21
          a22 = self.a22 + otro.a22
          a23 = self.a23 + otro.a23
          a24 = self.a24 + otro.a24
          a30 = self.a30 + otro.a30
          a31 = self.a31 + otro.a31
          a32 = self.a32 + otro.a32
          a33 = self.a33 + otro.a33
          a34 = self.a34 + otro.a34
          a40 = self.a40 + otro.a40
          a41 = self.a41 + otro.a41
          a42 = self.a42 + otro.a42
          a43 = self.a43 + otro.a43
          a44 = self.a44 + otro.a44
          return Matriz([[a00, a01, a02, a03, a04], [a10, a11, a12, a13, a14], [a20, a21, a22, a23, a24], [a30, a31, a32, a33, a34], [a40, a41, a42, a43, a44]])

        def _sub_(self, otro):
          a00 = self.a00 - otro.a00
          a01 = self.a01 - otro.a01
          a02 = self.a02 - otro.a02
          a03 = self.a03 - otro.a03
          a04 = self.a04 - otro.a04
          a10 = self.a10 - otro.a10
          a11 = self.a11 - otro.a11
          a12 = self.a12 - otro.a12
          a13 = self.a13 - otro.a13
          a14 = self.a14 - otro.a14
          a20 = self.a20 - otro.a20
          a21 = self.a21 - otro.a21
          a22 = self.a22 - otro.a22
          a23 = self.a23 - otro.a23
          a24 = self.a24 - otro.a24
          a30 = self.a30 - otro.a30
          a31 = self.a31 - otro.a31
          a32 = self.a32 - otro.a32
          a33 = self.a33 - otro.a33
          a34 = self.a34 - otro.a34
          a40 = self.a40 - otro.a40
          a41 = self.a41 - otro.a41
          a42 = self.a42 - otro.a42
          a43 = self.a43 - otro.a43
          a44 = self.a44 - otro.a44
          return Matriz([[a00, a01, a02, a03, a04], [a10, a11, a12, a13, a14], [a20, a21, a22, a23, a24], [a30, a31, a32, a33, a34], [a40, a41, a42, a43, a44]])

        def _mul_(self, otro):
          a00 = self.a00 * otro
          a01 = self.a01 * otro
          a02 = self.a02 * otro
          a03 = self.a03 * otro
          a04 = self.a04 * otro
          a10 = self.a10 * otro
          a11 = self.a11 * otro
          a12 = self.a12 * otro
          a13 = self.a13 * otro
          a14 = self.a14 * otro
          a20 = self.a20 * otro
          a21 = self.a21 * otro
          a22 = self.a22 * otro
          a23 = self.a23 * otro
          a24 = self.a24 * otro
          a30 = self.a30 * otro
          a31 = self.a31 * otro
          a32 = self.a32 * otro
          a33 = self.a33 * otro
          a34 = self.a34 * otro
          a40 = self.a40 * otro
          a41 = self.a41 * otro
          a42 = self.a42 * otro
          a43 = self.a43 * otro
          a44 = self.a44 * otro
          return Matriz([[a00, a01, a02, a03, a04], [a10, a11, a12, a13, a14], [a20, a21, a22, a23, a24], [a30, a31, a32, a33, a34], [a40, a41, a42, a43, a44]])

        def _rmul_(self, otro):
          a00 = self.a00 * otro
          a01 = self.a01 * otro
          a02 = self.a02 * otro
          a03 = self.a03 * otro
          a04 = self.a04 * otro
          a10 = self.a10 * otro
          a11 = self.a11 * otro
          a12 = self.a12 * otro
          a13 = self.a13 * otro
          a14 = self.a14 * otro
          a20 = self.a20 * otro
          a21 = self.a21 * otro
          a22 = self.a22 * otro
          a23 = self.a23 * otro
          a24 = self.a24 * otro
          a30 = self.a30 * otro
          a31 = self.a31 * otro
          a32 = self.a32 * otro
          a33 = self.a33 * otro
          a34 = self.a34 * otro
          a40 = self.a40 * otro
          a41 = self.a41 * otro
          a42 = self.a42 * otro
          a43 = self.a43 * otro
          a44 = self.a44 * otro
          return Matriz([[a00, a01, a02, a03, a04], [a10, a11, a12, a13, a14], [a20, a21, a22, a23, a24], [a30, a31, a32, a33, a34], [a40, a41, a42, a43, a44]])

  else:
    print("Ingreso no válido.")