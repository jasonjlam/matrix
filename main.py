from matrix import *
from graphics import *
import random

print("Image time")
createPixels(200,200,256)
for x in range(0, 255):
    color = [x, x, 255-x]
    image = newMatrix(4,0)
    print (x)
    for x in range(0, 3):
        print(x)
        addEdge(image, random.randrange(200), random.randrange(200),1, random.randrange(200), random.randrange(200),1)
    drawEdges(image, color)

for x in range(0, 255):
    color = [0, 255-x, x]
    image = newMatrix(4,0)
    print (x)
    for x in range(0, 3):
        print(x)
        addEdge(image, random.randrange(200), random.randrange(200),1, random.randrange(200), random.randrange(200),1)
    drawEdges(image, color)

writeImage("image.ppm")

print("Initializing empty matrix")
mat1 = newMatrix()
printMatrix(mat1)
print("Making it an identity matrix")
identity(mat1)
printMatrix(mat1)
print("Adding a column of (1,2,3)")
addPoint(mat1, 1,2,3)
printMatrix(mat1)
print("Adding a column of (0,1,0)")
addPoint(mat1, 0,1,0)
printMatrix(mat1)
print("Multiplying by identity matrix")
mat2 = newMatrix()
identity(mat2)
printMatrix(mat2)
addPoint(mat2, 0, 3, 4)
addPoint(mat2, 0, 3, 4)
addPoint(mat2, 0, 3, 4)
matrixMulti(mat2, mat1)
printMatrix(mat1)
print("Multiplying by a non-identity matrix")
mat3 = newMatrix(4,0)
addPoint(mat3, 1,2,3)
addPoint(mat3, 1,2,3)
addPoint(mat3, 1,2,3)
addPoint(mat3, 1,2,3)
printMatrix(mat3)
matrixMulti(mat3,mat1)
printMatrix(mat1)
print("Adding edges")
addEdge(mat1, 0, 1, 0, 5, 23, 0)
addEdge(mat1, 75, 1, 0, 92, 5, 0)
printMatrix(mat1)
