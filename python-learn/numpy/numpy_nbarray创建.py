import numpy as np

# 传入数组对象进行创建
arr = np.array([1,2,3],np.int64)
print(arr)
print('数据类型:',arr.dtype)

# 通过复制创建
arr1 = np.copy(arr)
print(arr1)
print('数据类型:',arr.dtype)

# 全零数组
arr = np.zeros((3,3,3))
print("全零",arr)
print("全零数据类型",arr.dtype)

# 全一的数组
arr = np.ones((3,3))
print("全一",arr)
print("全一数据类型",arr.dtype)

# 未初始化
arr = np.empty((2,3))
print("未初始化",arr)
print("未初始化数据类型",arr.dtype)

# 填充创建
arr = np.full((2,2), 3)
print("填充创建",arr)

arr1 = np.zeros_like(arr)
print("zeros_like",arr1)

# 等差数列创建 start end step(步长）
arr = np.arange(1,30,2)
print("等差数列",arr)

# 等间隔数列 start end  间隔差
arr = np.linspace(1,10,1)
print("等间隔数列",arr)

# 对数间隔数列
arr1 = np.logspace(1,5,5,base=2)
print("对数数列",arr1)

# 单位矩阵：主对角线上的值全为1，其余位置的值为零
arr = np.eye(3)
print("单位矩阵",arr)

# 对角矩阵：主对角线上非零的值，其余位置的值为零
arr = np.diag([1,3,4,6])
print("对数矩阵",arr)