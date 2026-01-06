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
# loc 显示索引,标签索引或者切片 iloc隐式索引，按位置索引或者切片
print(s.iloc[0:2])
# at 按标签访问单个原始，iat按位置访问当个元素
print("第2个元素： ",s.at[1])

# 数据访问
print(s[2])
print(s[s<4])