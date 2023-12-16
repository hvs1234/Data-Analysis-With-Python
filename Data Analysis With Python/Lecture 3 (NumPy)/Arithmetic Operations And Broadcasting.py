import numpy as np
arr1 = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,1,2,3]])

arr2 = np.array([[11,12,13,14],
                [15,16,17,18],
                [19,11,12,13]])

arr3 = np.array([[1,2,3],
                [1,2,3],
                [1,2,3],])

print((arr1+3),"\n")
print((arr1-arr2),"\n"); print((arr2-arr1),"\n")
print((arr1+arr2),"\n")
print((arr1/2),"\n")
print((arr1/arr2),"\n")
print((arr1*arr2),"\n")
print((arr1.shape),arr2.shape,"\n")

print(arr1+arr3,"\n") #Cannot be executed due to the brodcasting. Different shapes of two different arrays.