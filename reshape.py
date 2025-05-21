"""
reshape(rows, columns) -Specify new shape
if dimensions match
"""

import numpy as np

arr = np.array([10,20,30,40,50,60])
# Reshaping does not create copy, its effect the array (View).
reshape_arr = arr.reshape(3,2)
print(reshape_arr)

# [[10 20]
#  [30 40]
#  [50 60]]