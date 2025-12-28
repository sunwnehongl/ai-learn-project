import numpy as np

# 统计函数：求和、求平均值、加权平均、求中位数
arr = np.random.randint(1,100,(3,3))
print("矩阵",arr)
print("求和：",np.sum(arr))
# 平均值
print("平均值：",np.mean(arr))
print("按行求平均",np.mean(arr,axis=0))
print("按列求平均",np.mean(arr,axis=1))
# 多维数组求平均
arr = np.random.randint(1,10,(3,3,3))
print("3维数组",arr)
print("按0维求平均",np.mean(arr,axis=2))
# 加权平均
arrA = np.array([1,2,3,4])
arrW= np.array([0.4,0.3,0.2,0.1])
print("加权平均",arrA,arrW)
print(np.average(arrA,weights=arrW))

# 中位数计算：中位数是将数据集排序后位于中间位置的值，奇数个数据：中间值，偶数个数据：中间两个数的平均值
# 奇数个
arrA = np.array([9,4,2,5,1])
arrB = np.array([3,1,4,6])
print("9,4,2,5,1中位数",np.median(arrA))
print("3,1,4,6中位数",np.median(arrB))

arr = np.random.randint(1,10,(3,3))
print(arr)
print("多维中位数",np.median(arr))
print("每列的中位数",np.median(arr,axis=0))
print("每行的中位数",np.median(arr,axis=1))

# 方差：方差是衡量一组数据（或一个随机变量）取值分散程度或波动大小的指标
# 标准差：标准差是方差的平方根
arr = np.array([1,2,3,4,5])
print("求方差",arr)
print("平均值",np.median(arr))
print("标准差",np.std(arr))
print("总体方差",np.var(arr))
print("总体标准差",np.std(arr))
print("样本方差：",np.var(arr,ddof=4))
print("样本标准差",np.std(arr,ddof=4))

arr= np.random.randint(1,10,(3,3))
print("方差",arr)
print("每列的方差",np.var(arr,axis=0))
print("每列的标准差",np.std(arr,axis=0))
print('每行的方差',np.var(arr,axis=1))
print("每行的标准差",np.std(arr,axis=1))
# 标准差：标准差是方差的平方根