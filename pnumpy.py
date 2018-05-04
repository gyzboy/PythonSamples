
import numpy as np
#numpy数组可以进行很多列表不能进行的运算

#从列表传入
lst  = [3,2,1]
arrl = np.array(lst)
print(arrl)


#直接传入列表
arr = np.array([1,2,3,4],dtype="uint8")
print(arr)
print(arr+2)
print(arr+arr)
print(arr*4)


print(type(arr))

#查看数组中的数据类型
print(arr.dtype)
#查看每个元素所占字节
print(arr.itemsize)

#查看形状,返回一个元组,每个元素代表这一维的元素数目
sp = np.array([[3,4,],[5,3]],dtype=np.uint64)
print(sp.shape)
#查看元素总个数
print(sp.size)
#查看整个array元素所占空间
print(sp.nbytes)

print(sp.dtype)

#查看数组维数
print(sp.ndim)


#赋初值,随机数
cc = np.empty(3)

#赋初值,全0
dd = np.zeros(5)
cc.fill(5.5)
print(cc)
print(dd)

#od代表每天的总里程数
od = np.array([21000,21180,21240,22100,22400])
print(od[1:])
print(od[:-1])
#dist就算出了每天的里程数
dist = od[1:] - od[:-1]
print(dist)


#切片在np数组与列表中的区别
a = np.array([1,2,3,4])
b = a[2:3]#是引用,会改变a[2]的值,为了防止这种情况,可以使用copy新申请一段内存
#b = np.copy(a[2:3])
b[0] = 100
print(a)

aa = [1,2,3,4]
bb = aa[2:3]
bb[0] = 100
print(aa) #不会改变a[2]的值

loc = np.where(a > 3)
print(a[loc])

sm1 = np.array([[1,2,3,4],[2,3,4,]])
print(np.sum(sm1))#求和,如果两个维数不同会返回每个元素的值
sm2 = np.array([[1,2,3],[3,4,5]])
print(np.sum(sm2))
print(np.sum(sm2,axis=1))

pd = np.array([[2,3,4],[4,3,2]])
print(np.prod(pd))#乘积

print(np.argmax(pd,axis=1))#最大值的位置,默认第一维
print(np.argmin(pd))#最小值的位置
print(np.mean(pd))#均值
print(np.std(pd))#标准差 标准差能反映一个数据集的离散程度，标准偏差越小，这些值偏离平均值就越少 计算公式例：
# 有一组数字分别是200、50、100、200，求它们的样本标准偏差。
#  X = (200+50+100+200)/4 = 550/4 = 137.5
#  S^2= [(200-137.5)^2+(50-137.5)^2+(100-137.5)^2+(200-137.5)^2]/3
#样本标准偏差 S = Sqrt(S^2)=75

print(np.var(pd))#方差 方差是实际值与期望值之差平方的平均值，而标准差是方差算术平方根

print(np.clip(pd,3,3))#将大于5的clip为5，小于3的clip为3

print(np.ptp(aa))#最大值与最小值差

print(np.transpose(pd))#将数组转置

dg = np.array([[2,3,1]
              ,[2,2,1]
              ,[4,5,4]])
print(np.diagonal(dg))#对角线元素

print(np.diagonal(dg,offset=-1))#负数左移
print(np.diagonal(dg,offset=1))#正数右移

ts = np.array([1,2,3,4],dtype=np.uint8)#使用toString,fromstring需要制定dtype
print(ts.tostring(order='F'))
print(np.fromstring(ts.tostring(),dtype=np.uint8))

print(np.genfromtxt("io_for_test.txt",dtype=np.str_))#读取文本 读取二进制使用save、load


print(np.arange(4))#返回一个数组
print(np.linspace(0,1,5))#返回一个以N等距分布的数组
print(np.logspace(0,1,5))#返回一个以N等距分布、以10为底的数组


mt = np.array([[1,2,4],
              [2,5,3],
              [7,5,9]])
print(np.mat(mt))
