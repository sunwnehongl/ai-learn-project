import numpy as np

arr = np.random.randint(1,10,10)
print(arr)

# np.sort不改变原数组中内容
print(np.sort(arr))

# 输出排序的是索引
print(np.argsort(arr))

# nbarray.sort 改变原数组中的内容
arr.sort()
print(arr)

# 去重函数
arr = np.random.randint(1,200, 20)
print(arr)
print(np.unique(arr))