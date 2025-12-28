import numpy as np

a = np.array([1,2,3])
b = np.array((4,5,6))

print(a + b)
print(b - a)
print(a * b)
print(b / a)

# nbarray和标量的计算，对每个元素做一样的运算
print(a + 10)
print(a - 1)
print(a * 2)
print(a/ 10)


# 矩阵的乘法运算  
a = np.array([[1,2,3],
               [4,5,6]
             ,[7,8,9]])
b = np.array([[7,8,9],
               [10,11,12],
              [10,11,12]])
print(a @ b)