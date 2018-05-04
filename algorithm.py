import sys
#二分查找
def binary_search(a,target):
    length = len(a)
    start = 0
    end = length - 1
    while end >= start:
        mid = (end - start)/2+ start
        if a[mid] > target:
            end = mid - 1
        elif a[mid] < target:
            start = mid + 1
        else:
            print("find num")
            break


if __name__=="__main__":
    print(type(sys.argv[1]))
    print(type(sys.argv[2]))
    binary_search(eval(sys.argv[1]),(int)(sys.argv[2]))
