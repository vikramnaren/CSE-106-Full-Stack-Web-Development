import numpy as np
import random

def randomArr():
    x =  np.arange(2, 11).reshape(3,3)
    print(x)


def unique(list1):
 
    # initialize a null list
    unique_list = []
 
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    print(unique_list)

def unique_something(list1):
 
    # initialize a null list
    unique_list = []
 
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x > 37:
            unique_list.append(x)
    # print list
    print(unique_list)

def conversion(list1): 
    for i in range(len(list1)):
        print(np.multiply(list[i], 1.8) + 32)
    
def checkerboard():
    x = np.ones((3,3))
    print("Checkerboard pattern:")
    x = np.zeros((8,8),dtype=int)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                x[i][j] = 1
    print(x)


def main():
    randomArr()
    checkerboard()
    unique([10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10])
    unique_something([6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57])
    #conversion([0, 12, 45.21 ,34, 99.91])


if __name__ == "__main__":
    main()

