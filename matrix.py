#This is my matrix class.
#The objects of this class are matrixes with (n, n+1) dimentions

class matrix:
    def __init__(self, n):
        self.matrix = self.get_matrix(n)

    def get_matrix(self, n):
        matrix = [[None for j in range(n+1)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        return matrix

    def printm(self):
         for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end = ' ')
            print('\n')

    def get_rows(self):
        return len(self.matrix)

    def get_cols(self):
        return len(self.matrix) + 1

    #this function adds the i-th row d*(j-th row)
    def mull_add(self, i, j, d):
        for k in range(self.get_cols()):
                t = d * float(self.matrix[j][k])
                self.matrix[i][k] = self.matrix[i][k] + t;

    #this function swaps the i-th row with a row under it,
    #which i-th element is nonzero
    def swap_with_nonzero_row(self, i):
        for j in range(i + 1, self.get_rows()):
            if(self.matrix[j][i] != 0):
                for k in range(self.get_cols()):
                     temp = self.matrix[i][k]
                     self.matrix[i][k] = self.matrix[j][k]
                     self.matrix[j][k] = temp

    #this function returns true if there is a row in the matrix like this-
    #(0, 0, ..., 0, t) where t is nonzero
    def exists_wrong_row(self):
        for i in range(self.get_rows()):
            zero = True
            for j in range(self.get_rows()):
                if(self.matrix[i][j] != 0):
                    zero = False
                    break
            if(zero == True and self.matrix[i][self.get_rows()] != 0):
                return True
        return False

    #this function returns true if there is a row in the matrix like this-
    #(0, 0, ..., 0) 
    def exists_zero_row(self):
        for i in range(self.get_rows()):
            zero = True
            for j in range(self.get_cols()):
                if(self.matrix[i][j] != 0):
                    zero = False
                    break
            if(zero == True):
                return True
        return False

    def get(self, i, j):
        return self.matrix[i][j]

    def set(self, i, j, d):
        self.matrix[i][j] = d
    def neg(self, i, j):
        return - self.matrix[i][j]
