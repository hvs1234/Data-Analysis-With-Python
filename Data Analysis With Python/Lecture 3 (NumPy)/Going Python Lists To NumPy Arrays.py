import numpy as np

kanto = np.array([73,67,43])
w1,w2,w3 = 0.3,0.2,0.5

print(f"{kanto,type(kanto)}")
weights = np.array([w1,w2,w3])

print(f"{weights,type(weights)}")

print(f"{kanto[2]+3}")