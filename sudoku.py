import numpy as np
import pandas as pd

class Sudoku:
    def __init__(self,matrix):

        try:
            self.sudoku_matrix = np.zeros([9,9]) + np.array(matrix)
        except:
            raise "Matriz de tamanho errado."
        aux_possibility_matrix_dict = {}
        for i in range(0,9):
            aux_possibility_matrix_dict[i]=[list(range(1,10))]

        self.possibility_matrix = pd.DataFrame(aux_possibility_matrix_dict, index=np.arange(9))
        print(self.possibility_matrix[[0,1,2,3,4,5]])
        self.matrix_to_possibility_transfer()
        print(self.possibility_matrix[[0,1,2,3,4,5]])
        print("")

    def matrix_to_possibility_transfer(self):
        for idx_x, row_x in enumerate(self.sudoku_matrix):
            for idx_y, element_x_y in enumerate(row_x):
                if(element_x_y != 0):
                    self.possibility_matrix[idx_y][idx_x] = [element_x_y]


    def access_index(self, quadrand, _x, _y):
        return(self.sudoku_matrix[x][y])

    def access_possibility_index(self, _x, _y):
        return(self.possibility_matrix[9*x][9*y])

    def get_quadrant(self, full_matrix, _x, _y):
        # print(type(full_matrix))
        # print(full_matrix)
        # print(full_matrix[_x*3:(_x*3)+3])
        aux = []
        for x in full_matrix[_x*3:(_x*3)+3]:
            aux2 =x[_y*3:(_y*3)+3]
            aux.extend([aux2 ])
        return aux

    # def set_element_in_array(self, modified_array, _x, _y):
    #     self.possibility_matrix =

    def clear_quadrants_from_quadrand_element(self):
        for idx_x, matrix_row in enumerate(self.sudoku_matrix):
            for idx_y, matrix_element in enumerate(matrix_row):
                if(matrix_element != 0):
                    quadrant_x = idx_x//3
                    quadrant_y = idx_y//3
                    aux_quadrant = self.get_quadrant(
                                        self.possibility_matrix.to_numpy(),
                                        quadrant_x,
                                        quadrant_y
                                    )
                    for possibility_idx_x, possibility_element_x in enumerate(
                                                                        aux_quadrant
                                                                    ):
                        print([x for x,y in enumerate(possibility_element_x)])
                        for possibility_idx_y, possibility_element_y in enumerate(possibility_element_x):
                            aux = possibility_element_y.copy()
                            print("looking for element ", idx_x, idx_y, " no indice (pssblt) ",possibility_idx_x+quadrant_x*3, possibility_idx_y+quadrant_y*3, aux)
                            if(matrix_element in list(aux) and [idx_x, idx_y] != [possibility_idx_x+quadrant_x*3, possibility_idx_y+quadrant_y*3]):
                                print(self.possibility_matrix[[0,1,2,3,4,5]])
                                aux_list = self.possibility_matrix[possibility_idx_y+quadrant_y*3][possibility_idx_x+quadrant_x*3].copy()
                                aux_list.remove(matrix_element)
                                self.possibility_matrix[possibility_idx_y+quadrant_y*3][possibility_idx_x+quadrant_x*3] = aux_list
                                print(self.possibility_matrix[[0,1,2,3,4,5]])
                                print("---------------------------------------------")
                                print("")


base_matrix =  [[0, 0, 7, 0, 0, 0, 2, 0, 8],
                [0, 8, 9, 0, 7, 3, 0, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 1, 7],
                [8, 0, 0, 0, 0, 6, 0, 2, 0],
                [0, 0, 0, 2, 1, 0, 0, 4, 0],
                [6, 4, 0, 0, 0, 9, 0, 0, 0],
                [5, 0, 0, 6, 0, 0, 8, 0, 0],
                [0, 9, 0, 3, 4, 0, 1, 0, 0],
                [4, 0, 0, 0, 2, 7, 3, 0, 0]]

sudoku_obj = Sudoku(base_matrix)

print(sudoku_obj.get_quadrant(sudoku_obj.sudoku_matrix,0,2))
sudoku_obj.clear_quadrants_from_quadrand_element()
print(sudoku_obj.get_quadrant(sudoku_obj.sudoku_matrix,0,2))

# print(sudoku_obj.get_quadrant(sudoku_obj.sudoku_matrix,1,1))


