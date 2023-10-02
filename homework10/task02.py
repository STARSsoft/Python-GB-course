'''
Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.
'''

class Matrix_:
    
    def __init__(self,rows,cols) -> None:
        self.rows=rows
        self.cols=cols
        self.matrix=[[0 for j in range(cols)] for i in range(rows)]

    def set_value(self,r,c,val):
        self.matrix[r][c]=val

    def get_value(self,r,c):

        return self.matrix[r][c]
 
    def transpose(self):

        transposed = Matrix_(self.cols,self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set_value(j,i,self.matrix[i][j]) 
        return transposed

    def print_matrix(self):
        for row in self.matrix:
            for elmt in row:
                print(elmt, end=" ")
            print()

if __name__=="__main__":
    my_matrix =Matrix_(2,4)
    my_matrix.set_value(0,0,1)
    my_matrix.set_value(0,1,2)
    my_matrix.set_value(0,2,3)
    t_m=my_matrix.transpose()
    my_matrix.print_matrix()
    t_m.print_matrix()