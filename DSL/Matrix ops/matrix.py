# Arithmetic operations on matrices
# taking simple input and converting into proper matrices, by specifying no. of rows and columns
# using numpy lib

import numpy as np

row1=int(input("Enter number of rows for first matrix: "))
col1=int(input("Enter number of columns for first matrix: "))

entries = list(map(int,input("\nEnter the elements of first matrix seperated by blankspace:\n").split()))    # splitting input(seperated by space) into elements
matrix1=(np.array(entries)).reshape(row1, col1) # rearranging entries(elements stored in entries var) into proper matrix
print("\nFirst matrix is :")
print(matrix1)

row2=int(input("\nEnter number of rows for second matrix: "))
col2=int(input("Enter number of columns for second matrix: "))

entries = list(map(int,input("\nEnter the elements of second matrix seperated by blankspace:\n").split()))    # splitting input(seperated by space) into elements
matrix2=np.array(entries).reshape(row2, col2)   # rearranging entries(elements stored in entries var) into proper matrix
print("\nSecond matrix is: ")
print(matrix2)

# for operations on matrices, dimensions of both matrices should be equal, checked by .ndim function
# Addition
def add():
    if matrix1.shape==matrix2.shape and matrix1.ndim==matrix2.ndim:  # checking if both matrices are of same shape and dimension(otherwise no addition is possible)
        print("addition of matrix is: ")
        print(np.add(matrix1,matrix2))
    else:
        print("Matrices dont have similar dimension or shape.")
        
# Substraction    
def sub():
    if matrix1.shape==matrix2.shape and matrix1.ndim==matrix2.ndim:  # checking if both matrices are of same shape(otherwise no addition is possible)
        print("substraction of matrix is: ")
        print(np.subtract(matrix1,matrix2))
    else:
        print("Matrices dont have similar dimension or shape.")
        
# Multiplication
def Mul():
    if col1==row2 and matrix1.ndim==matrix2.ndim:   # to multiply matrices, no. of columns of first must be equal to no. of rows of second
                                                    # and dimension of both matrices should be same
        print("Multiplication of matrix is: ")
        print(np.dot(matrix1,matrix2))
    else:
        print("These matrices aren't multiplicable.")
        
# transpose:
def transpose():
    T=int(input("Enter 1 for first matrix or 2 for second matrix: "))
    if T==1:
        print(matrix1.transpose())
            
    elif T==2:
        print(matrix2.transpose())
        
temp=1  # looping variable

while(temp):    # making operations menu driven
    print("===========MATRIX OPERATIONS============")
    print("1. Addition of two matrices")
    print("2. Subtraction of two matrices")
    print("3. Multiplication of two matrices")
    print("4. Transpose of a matrix")
    print("5. Exit")
    print("========================================")
    n=int(input("\nEnter your choice:"))

    if n==1:
        add()

    elif n==2:
        sub()

    elif n==3:
        Mul()

    elif n==4:
        print("Transpose of a matrices is:")
        transpose()

    elif n==5:
        exit(0)
        
    else:
        print("Invalid choice please select from given choices ")

    temp= int(input("Want to continue?(0 for no, 1 for yes): "))  # looping variable
