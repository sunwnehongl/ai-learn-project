import numpy as np

# 平方根函数 sqrt,返回的数据结果是浮点数类型
print(np.sqrt(81))
arr = np.array([[1,4,9],
                [16,25,36]])
print(np.sqrt(arr))

# 计算指数exp,用于计算 e（自然常数，约等于 2.71828）的幂
print(np.exp(1))
print(np.exp(2))
arr = np.array([0, 1, 2, 3])
print(np.exp(arr))

# 计算对数log函数 lnx
print(np.log(7.38905609893065))

# 正玄和余玄函数
print(np.sin(90))
print(np.cos(np.pi))

# 计算绝对值
print("计算绝对值")
print(np.abs([-1,2,-3]))
arr = np.random.randint(-10,10,(3,3))
print(arr)
print(np.abs(arr))

#  计算a的b次幂
print("计算a的b次幂")
print(np.power([1,2,3],3))
arr = np.random.randint(1,10,(3,3))
print(arr)
print(np.power(arr,2))

# 四舍五入round
print(np.round([1.2,2.50,3.51,6.6,9.9]))

arr = np.array([1.0,2.1,3.5,4.6])
# 向上取整
print(np.ceil(arr))
# 向下取整
print(np.floor(arr))

# 检查缺失值
print(np.isnan([1,1,2,3]))
print(np.isnan(np.empty((2,2))))