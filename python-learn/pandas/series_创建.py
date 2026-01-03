import pandas as pd

s = pd.Series([1,2,3,4,5])
print(s)

# 自定义索引
s = pd.Series([5,3,4,1,2],[1,2,3,4,5], name="成绩")
print(s)

# 通过字典创建
s = pd.Series({'张三':'12','李四':'18'})
print(s)