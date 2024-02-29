arr = [1,2,3,4,5,6,7,8,9,10]
target = 5
l = 0
r = len(arr) - 1
def binary(target,l,r):
    while l <= r:
        mid = l + (r-l) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
    return -1

res = binary(target,l,r)

if res != -1:
    print(res)
