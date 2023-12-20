import statistics
import time
import math
print("The value of pi is",math.pi)
seconds=time.time()
print("Seconds since epoch(the point where time begins)=",seconds)
li=[1,2,3,3,2,2,2]
print("The average of list values is :",end="")
print(statistics.mean(li))
local_time=time.ctime(seconds)
print("Local time:",local_time)