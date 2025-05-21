'''
.ravel() -> view
.flatten() -> retrun copy of the array
'''

import numpy as np

arr = np.array([[5,6,7,8], [1,2,3,4]])
print(arr.ravel())
print(arr.flatten())

# Output will we same but ravel() return view, flatten() return copy of the array


