import numpy as np

# 比较是否大于、小于、等于、与、或、非
arr = np.random.randint(1,100,10)
arr2 = np.random.randint(1,100,10)
print(arr)
print(arr2)
print("大于50",np.greater(arr,50))
print("大于等于50",np.greater_equal(arr,50))
print("等于50",np.equal(arr,50))
print("小于50",np.less(arr,50))
print("小于等于50",np.less_equal(arr,50))

print("两个数组比较大于",np.greater(arr,arr2))

arr = np.random.randint(0,2,5)
arr2 = np.random.randint(0,2,5)
print(arr)
print(arr2)
print("逻辑与",np.logical_and(arr,arr2))
print("逻辑或",np.logical_or(arr,arr2))
print("逻辑非",np.logical_not(arr))

# 自定义条件
arr = np.random.randint(1,100,10)
print(arr)
print("大于50",np.where(arr>50,1,0))
print("及格和不及格",np.where(arr>=60,"及格","不及格"))
print("嵌套判断",np.where(arr<60,"不及格",np.where(arr< 80,"良","优秀")))