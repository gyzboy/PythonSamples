
import sys

#python2整型计算只返回整型
print(12/5)  #2
#python3可以返回float数
print(12/5) #2.4

print(type(12))
print(type('2'))
print(type("4"))

print(sys.float_info)

compl = 1 + 2j
print(type(compl))
print(compl.real)#实部
print(compl.imag)#虚部
print(compl.conjugate())#共轭

a = "hello world"
print(a[0])
print(a[-1])
print(a[0:5])#切片时右侧都相当于),实际上是读取index为0-4的5个数
print(a[:5])#第一个索引是0还可以省略
print(a[0:5:2])#切片时跳步也相当于),实际上是每隔一个取一个,=>hlo,或者这么理解,从index为0的元素开始,步长为2所以从e开始作为第一个元素计数取第二个元素l,以此类推
print(a[-1:-5:-3])#切片的倒数第一个元素索引为-1,从d开始往前数3个数取到o,所以最后结果为do
print(a[0:len(a):2])
print(a[-2:])#第二个参数默认到最后一个元素
print(a.split("o"))

#[]用来生成列表,列表中可以有重复元素
list=[1,3,2,4]
print(len(list))
print(list+list)
list.append("3")
print(list)

#{}用来生成集合,集合中不含有重复元素
collect ={2,3,4,2}
print(len(collect))
collect.add("2")
print(collect)

#{key:value}用来生成字典
dict = {'dog':5,'cats':6}
dict2 = {"dog":55,'cats':6}
print(dict)
print(dict2)
dict['dog'] = 10
dict["dog"] = 15
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())

print(ord('f'))#查看ASCII