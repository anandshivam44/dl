import numpy as np
a=np.random.rand(10)
print(a)
print(a.shape)
print(a.T)
print(np.dot(a,a.T),"\n\n\n")
b=np.random.rand(5,1)
print(b)
print(b.T)
print("\n\n")
print(np.dot(b,b.T))
assert(b.shape==(1,5))