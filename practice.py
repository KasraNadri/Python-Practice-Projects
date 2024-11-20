import numpy as np

a = np.array([1, 2, 3])

b = np.array([[9.0, 8, 0, 7, 0], 
              [6, 0, 5, 1, 5]])

a.ndim
b.shape
b.size
#--------------------------

#----- GET A SPECIFIC ELEMENT [R, C]
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
a[1, 5]

#----- GET A SPECIFIC ROW
a[0:]

#----- GET A SPECIFIC COLUMN
a[: 2]

#----- [STARTINDEX : ENDINDEX : STEPSIZE]
a[0, 1:-2:]


b = np.array([[[1, 2], 
               [3, 4]], 
                    [[5, 6,], 
                    [7, 8]]])



print(b[0, 1, 1])
b[:, 0, :] = [[9, 9], [9, 9]]
print(b)



#--------
np.zeros((2, 3, 3, 2))

np.ones((4, 2, 2), dtype ='int32')

np.full((2, 2), 99, dtype = 'float64')

np.full_like(a, 4)

#----- RANDOM DECIMAL NUMBERS
np.random.rand(4, 2)

np.random.random_sample(a.shape)

#----- RANDOM INTEGER VALUES
np.random.randint(1, 10, size= (3, 3))

#------ IDENTITY MATRIX
np.identity(5)


arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis = 1)

#--------- PRACTICE
array = np.ones((5, 5), dtype = 'int32')
array[1:4, 1: 4] = 0
array[2, 2] = 9
print(array)

#----- BE CAREFUL WHEN COPYING ARRAYS
a = np.array([1, 2, 3])
b = a.copy() #---WITHOUT REFERENCING 'a' DIRECTLY
b[0] = 100
