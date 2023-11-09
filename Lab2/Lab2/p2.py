import numpy as np

def addArr():
    arr1 = np.array([[1,2, 3], [-4, 5, 6], [7, 8, 9]])
    arr2 = np.array([[3, 1, 4], [2, 6, 1], [2, 9, 7]])
    sum = np.add(arr1, arr2)
    print("sum array: ", sum)

def multiplyArr():
  arr1 = np.array([[1,2, 3], [-4, 5, 6], [7, 8, 9]])
  arr2 = np.array([[3, 1, 4], [2, 6, 1], [2, 9, 7]])
  product = np.dot(arr1, arr2)
  print("product array: ", product)

def determinant():
    arr1 = np.array([[1,2, 3], [4, 5, 6], [7, 8, 9]])
    det = np.linalg.det(arr1)
    print("Determinent: ", int(det))
def inverse():
    arr2 = np.array([[3, 1, 4], [2, 6, 1], [2, 9, 7]])
    invs = np.linalg.inv(arr2)
    print("Inverse: ", invs)

def eignen():
    arr1 = np.array([[1,2, 3], [4, 5, 6], [7, 8, 9]])
    w, v = np.linalg.eig(arr1)
    print("Eigenvalues: ", w)




def main():
    addArr()
    multiplyArr()
    determinant()
    inverse()
    eignen()



if __name__ == "__main__":
    main()
