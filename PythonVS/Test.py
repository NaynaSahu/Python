from sys import flags
import numpy as np


a = np.array([1,2,3,4] , ndmin= 4)
for i in np.nditer(a, flags=['buffered'] , op_dtypes=['S']):
    print(i)