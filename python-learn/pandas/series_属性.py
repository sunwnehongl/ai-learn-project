import pandas as pd

s = pd.Series([1,2,3,4,5])
# values属性
print("values:",s.values)
# index 属性
print("index:",s.index)
# shape 属性
print("shape:",s.shape)
# ndim 属性
print("ndim:",s.ndim)
#size 属性
print("size:",s.size)
# dtype属性
print("dtype:",s.dtype)