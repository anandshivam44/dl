import numpy as np
A=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(A)
cal=A.sum(axis=0)
print(cal)
percentage=100*A/cal.reshape(1,4)
print (percentage)