import numpy as np
climate_data = np.array([[73,67,43],
                         [91,88,64],
                         [87,134,58],
                         [102,43,37],
                         [69,96,70]])

print(f"{climate_data}")
# print(f"{climate_data.shape}")
# print(f"{climate_data.dtype}")
weights = [0.3,0.5,0.7]

print(f"{np.matmul(climate_data,weights)}")
print(f"{climate_data @ weights}")