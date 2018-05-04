f = open("io_for_test.txt").read()
ff = open("io_for_test.txt").read()[0:5]
open("io_for_test.txt","a").write(" 123")
fw = open("io_for_test.txt","r").read()
print(f)
print(ff)
print(fw)