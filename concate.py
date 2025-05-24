'''
np.concatenate((array1, array2), axis - 0)

axis 0 - vertical stacking 
axis 1 - horizintal stacking
'''

import numpy as np

arr1 = np.array([10,20,30,40])
arr2 = np.array([50,60,70,80])


# concate_arr = np.concatenate((arr1, arr2), axis=0)
# print(concate_arr)

concate_arr = np.concatenate((arr1, arr2), axis=1)
print(concate_arr)
