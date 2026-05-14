import numpy as np
# 1. 二维数组切片
arr = np.arange(20).reshape(4, 5)
print("原始数组：")
print(arr)
# 取第1~2行、第2~4列
print("第1~2行、第2~4列：")
print("你的代码写在下面")
print(arr[0:2,1:4])



# 2. 步长切片
arr = np.arange(20).reshape(4, 5)
# 隔一行取一行，隔一列取一列
print("隔行隔列取：")
print("你的代码写在下面")
print(arr[::2,::2])

# 3. 切片是视图——改切片影响原数组
arr = np.arange(12).reshape(3, 4)
sub = arr[0:2, 0:2]
sub[0, 0] = 999
# 此时 arr[0,0] 也会变，因为切片是视图不是副本
print("修改切片后原数组的值：", arr[0, 0])  # 猜猜是多少？
# 用 copy() 避免这个问题
arr2 = np.arange(12).reshape(3, 4)
sub2 = arr2[0:2, 0:2].copy()
sub2[0, 0] = 999
print("用了copy后原数组的值：", arr2[0, 0])  # 猜猜是多少？

# 4. 广播——形状不同的数组也能运算
a = np.array([1, 2, 3])       # 形状 (3,)
b = np.array([[10], [20], [30]])  # 形状 (3, 1)
# a 和 b 形状不同，但 NumPy 会自动扩展
print("广播结果：")
print(a + b)
# 你能说出结果是怎样的吗？把结果写在注释里
# 结果：a 广播成 [[1,2,3],[1,2,3],[1,2,3]]，b 广播成 [[10,10,10],[20,20,20],[30,30,30]]
# 相加得 [[11,12,13],[21,22,23],[31,32,33]]

# 5. 广播实用场景：标准化
data = np.array([[80, 90, 85],
                 [70, 75, 80],
                 [95, 92, 88]])
# 计算每列的平均值（axis=0）
col_mean = np.mean(data, axis=0)
# 用广播让每列都减去对应列的均值
# 提示：data 是 (3,3)，col_mean 是 (3,)，NumPy 自动广播
centered = data - col_mean
print("原始数据：")
print(data)
print("每列均值：", col_mean)
print("去均值后的数据：")
print(centered)

# 6. 花式索引——用数组做索引
arr = np.arange(10)
indices = np.array([0, 3, 5, 7])
# 用 indices 取出 arr 中对应位置的元素
print("花式索引结果：", arr[indices])

# 7. 花式索引——二维花式索引
arr = np.arange(16).reshape(4, 4)
rows = np.array([0, 2, 3])
cols = np.array([1, 3, 0])
# 取出 (0,1)、(2,3)、(3,0) 三个位置的元素
print("二维花式索引结果：", arr[rows, cols])

# 8. 综合：三维数组切片 + 花式索引
# 模拟 2 张 3x3 的灰度图
imgs = np.arange(18).reshape(2, 3, 3)
print("两张图像：")
print(imgs)
# 取出第一张图
print("第一张图：")
print(imgs[0])
# 取出两张图的第一行
print("两张图的第一行：")
print(imgs[:, 0, :])
# 取出两张图中心区域（第1行第1列）
print("两张图中心像素：")
print(imgs[:, 1, 1])
