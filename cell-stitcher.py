import shutil
import numpy as np

def move(src, dest):
    shutil.move(src, dest)

def rotate_CW():
    Rmatrix = np.matrix( ((0,1), (-1, 0)) )


def shift(coords, direction):
    if direction == right:
        x = coords[0] + cells_in_x
    if direction == left:
        x = coords[0] - cells_in_x
    if direction == down:
        y = coords[1] + cells_in_y
    if direction == up:
        y = coords[1] - cells_in_y

cells_in_x = 3
cells_in_y = 3

#Testmatrix = np.matrix([[(1,1), (2,1), (3,1)], [(1,2), (2,2), (3,2)], [(1,3), (2,3), (3,3)]])
Testmatrix2 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Rmatrix = np.matrix( ((0, 1), (-1, 0)) )
print(Rmatrix)
print(Testmatrix2)
print(Rmatrix*Testmatrix2)

#a = np.matrix([[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]])
#b = np.matrix([1, 2, 3])

#print(a)
#print(b)
#print(a*np.transpose(b))