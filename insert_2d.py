import numpy as np

arr = np.array([[1,2], [4,5]])
print(arr)

new_arr_2d = np.insert(arr, 2, [6,7], axis=0)
print(new_arr_2d)