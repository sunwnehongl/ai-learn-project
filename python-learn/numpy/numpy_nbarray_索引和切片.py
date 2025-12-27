import numpy as np

arr = np.random.randint(1,100,10)
print(arr)
# 基础索引
print(arr[9])

# 切片 [start:stop:step]
print("[start:stop:step]")
print(arr[:])
print(arr[2:6])
print(arr[2:6:2])
print(arr[2:])
print(arr[::3])

# 使用数组作为索引
index = [0,2,4]
print(arr[index])

# 布尔索引
print("布尔索引")
print(arr[arr> 10])

print("多维数组")
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]])
# 第0列第1行
print(arr2d[0,1])
# 切片 [一维start:stop:step,二维start:stop:step,n维start:stop:step]
print(arr2d[0])
print(arr2d[:2])
print(arr2d[0::2, 1:3])
# 当使用整数索引列时，会降低一个维度，返回一维数组。
print(arr2d[0:3, 1])
# 花式索引 第一个列表 [0, 1, 2] 指定行索引,第二列指定列
print(arr2d[[0,1,2],[1,1,1]])