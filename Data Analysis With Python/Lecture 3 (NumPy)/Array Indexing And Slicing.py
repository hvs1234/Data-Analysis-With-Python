import numpy as np
arr1 = np.array([[[11,12,13,14],
                 [13,14,15,19]],
                 [[15,16,17,21],
                  [63,92,36,18]],
                 [[98,32,81,23],
                  [17,18,19.5,43]]])

print(arr1.shape,"\n")

print(arr1[1],"\n")

print(arr1[1:],"\n")
print(arr1[1:,0:1,:2],"\n")
print(arr1[1:,1,:2],"\n")