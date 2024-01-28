import random

# a = int(input("Введіть кількість строк матриці "))
# b = int(input("Введіть кількість стовпців матриці "))

# m = []
#
# for i in range(3):
#     l = []
#     for j in range(3):
#         s = "введіть значення матриці для значення {} {} ".format(i+1, j+1)
#         l.append(int(input(s)))
#     m.append(l)

class Matrix:
    def __init__(self, matrix = None):
        if matrix == None:
            self.matrix = []

            for i in range(3):
                l = []
                for j in range(3):
                    l.append(random.randint(-100, 100))
                self.matrix.append(l)
        else:
            self.matrix = matrix

    def printMatrix(self):
        for row in self.matrix:
            for i in row:
                print('{}\t\t'.format(i), end='')
            print()

    def isDiagonal(self):
        isDiagonal = len(self.matrix) == len(self.matrix[0])
        for i in range(len(self.matrix)):
            if not isDiagonal:
                break
            for j in range(len(self.matrix[i])):
                if not isDiagonal:
                    break
                if isDiagonal and ((j == i and self.matrix[i][j] == 0) or (j != i and self.matrix[i][j] != 0)):
                    isDiagonal = False
        return isDiagonal

    def isTrangle(self):
        isTrangel = len(self.matrix) == len(self.matrix)
        for i in range(len(self.matrix)):
            if not isTrangel:
                break
            for j in range(len(self.matrix[i])):
                if not isTrangel:
                    break
                if isTrangel and (j < i and self.matrix[i][j] != 0):
                        isTrangel = False
        return isTrangel

    def addMatrix(self, matrix = None):
        a1 = len(self.matrix)
        b1 = len(self.matrix[0])

        mtx = Matrix().getMatrix() if matrix == None else matrix.getMatrix()

        a2 = len(mtx)
        b2 = len(mtx[0])

        a_min = min(a1, a2)
        a_max = max(a1, a2)

        b_min = min(b1, b2)
        b_max = max(b1, b2)
        if a_min < a_max:
            if a1 < a_max:
                empty_row = [0 for x in range(a_max)]
                self.matrix.append(empty_row)
            else:
                empty_row = [0 for x in range(a_max)]
                mtx.append(empty_row)

        newMatrix = []
        for i in range(a_max):
            row = []
            for j in range(b_min):
                row.append(self.matrix[i][j] + mtx[i][j])
            if b_min < b_max:
                for j in range(b_min, b_max):
                    try:
                        row.append(self.matrix[i][j])
                    except:
                        row.append(mtx[i][j])

            newMatrix.append(row)
        return newMatrix

    def transponentMatrix(self):
        newMatrix = []
        for i in range(len(self.matrix[0])):
            newMatrix.append([0 for x in range(len(self.matrix))])

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                newMatrix[j][i] = self.matrix[i][j]

        return newMatrix

    def getMatrix(self):
        m = []
        for row in self.matrix:
            newRow = []
            for i in row:
                newRow.append(i)
            m.append(newRow)
        return m

traingel = [
    [1, 0, 0, ],
    [0, 1, 0, ],
    [0, 0, 1, ],
    [9, 9, 9, ],
]

traingelM = Matrix(traingel)
traingelM.printMatrix()
print(traingelM.isDiagonal())
print(traingelM.isTrangle())

diagonal = [
    [1, 2, 3, 4,],
    [0, 1, 4, 5,],
    [0, 0, 1, 6,],
]

diagonalM = Matrix(diagonal)
diagonalM.printMatrix()
print(diagonalM.isDiagonal())
print(diagonalM.isTrangle())
print(diagonalM.transponentMatrix())
print(diagonalM.addMatrix(traingelM))
print(diagonalM.transponentMatrix())
print('=' * 20)
randomMatrix = Matrix()
randomMatrix.printMatrix()
print(randomMatrix.isDiagonal())
print(randomMatrix.isTrangle())
print(randomMatrix.addMatrix())
print(randomMatrix.transponentMatrix())


