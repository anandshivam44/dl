import numpy as np
a=np.random.rand(1000000)
b=np.random.rand(1000000)
import time
start=time.time()
c=np.dot(a,b)
end=time.time()
print("Vectorized version: "+str(1000*(end-start)))
c=0
start=time.time()
for i in range (1000000):
    c+=a[i]*b[i]
end=time.time()
print("For loop: "+str(1000*(end-start)))

d=[3,4,5,54,6,88,0,90,4,23,4,234,2,34,654,56,7,6,76,8]
e=np.log(d)
print(e)