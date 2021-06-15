import numpy as np

#create n-dimensional numpy array
##a = np.array([1,2,3,4,5,6])
##print(a.dtype)
##print(type(a))
##print(a.shape)
##print(a.ndim)
##print(a)

#Zero dimensional array i.e Scalar
##zero_D = np.array(4)
##
##print(zero_D.shape)
##print(zero_D.ndim)
##print(zero_D)

#One dimensional array i.e Vector
##one_D = np.array([1,2,3,4,5,6])
##
##print(one_D.shape)
##print(one_D.ndim)
##print(one_D)

#Two dimensional array i.e Matrix
##two_D = np.array([[1,2,3],
##                  [4,5,6]])
##
##print(two_D.shape)
##print(two_D.ndim)
##print(two_D)

#Two dimensional row array i.e Row Matrix
##row_2D = np.array([[1,2,3,4,5]])
##
##print(row_2D.shape)
##print(row_2D.ndim)
##print(row_2D)

#Two dimensional column array i.e Column Matrix
##col_2D = np.array([[3],
##                   [4],
##                   [5]])
##
##print(col_2D.shape)
##print(col_2D.ndim)
##print(col_2D)

#Three dimensional array i.e 3D Matrix
##three_D = np.array([[[1,2,3], [4,5,6]],
##                    [[7,8,9], [10,11,12]]])
##
##print(three_D.shape)
##print(three_D.ndim)
##print(three_D)

#numpy array supports indexing and slicing same as python datatypes
##a = np.array([1,2,3,4,5,6])
##
##print(a[2:5])

##two_D = np.array([[1,2,3],
##                  [4,5,6]])
##print(two_D[0:2,0:2])


##zeros_mat = np.zeros((3,3))
##print(zeros_mat)
##print(zeros_mat.dtype)


##ones_mat = np.ones((4,5))
##print(7*ones_mat)


##identity_mat = np.eye(5)
##print(identity_mat)


##random_mat = np.random.random((5,4))
##print(random_mat)
##
##print(random_mat.dtype)


##a = np.array([[2,3,4],
##              [5,6,7]])
##b = np.array([[11,20,25],
##               [22,10,15]])


##print('Elementwise operation')
##print("Add:", a + b)
##print()
##print('Sub:', a - b)
##print()
##print('Divide:', a/b)
##print()
##print('Multiply:', a*b)


##print('Square:', np.square(a))
##print('Power: ', np.power(a, 1/3))
##print('Mean: ', np.mean(a))
##print('Min: ', np.min(a[:,2]))
##print('Sum: ', np.sum(a))
##print('Column-wise addition:', np.sum(a, axis = 0))
##print('Row-wise addition:', np.sum(a, axis = 1))
##print('Max: ', np.max(a))

#arange() method
##r = np.arange(1,13)
##print(r)
##print(r.shape)

#reshape() method
##r_3x4 = r.reshape((3,4))
##print(r_3x4)
##print(r_3x4.shape)

##r_4x3 = r.reshape((4,3))
##print(r_4x3)
##print(r_4x3.shape)

#linspace() method
##l = np.linspace(0,11)
##print(l.shape)
##print(l)
##
##l_10x5 = l.reshape(10,5)
##print(l_10x5.shape)
##print(l_10x5)


#You can perform all matrix operations

##x = np.array([[1,2],[3,4]])
##y = np.array([[5,6],[7,8]])
##
##v = np.array([9,10])
##w = np.array([11, 12])

# Inner product of vectors; both produce 219

##print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]

##print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]

##print(np.dot(x, y))


##transpose_v = v.T
##print(transpose_v.shape)
##
##
##
##x = np.array([[1,2], [3,4]])
##print(x)    # Prints "[[1 2]
##            #          [3 4]]"
##print(x.T)  # Prints "[[1 3]
##            #          [2 4]]"
##
### Note that taking the transpose of a rank 1 array does nothing:
##v = np.array([1,2,3])
##print(v)    # Prints "[1 2 3]"
##print(v.T)  # Prints "[1 2 3]"




##v = np.array([1,2,3])  # v has shape (3,)
##w = np.array([4,5])    # w has shape (2,)
### To compute an outer product, we first reshape v to be a column
### vector of shape (3, 1); we can then broadcast it against w to yield
### an output of shape (3, 2), which is the outer product of v and w:
### [[ 4  5]
###  [ 8 10]
###  [12 15]]
##print(np.reshape(v, (3, 1)) * w)
