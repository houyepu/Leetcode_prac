#[1,2,3,4]
#[24,12,8,6]
arr = [1,2,3,4]
list_new = []
n= len(arr)
for i in range(0,n):
    res = 1
    for j in range(0,n):
        if j != i:
            res *= arr[j]
    list_new.append(res)

print(list_new)


arr = [1, 2, 3, 4]
n = len(arr)
left_products = [1] * n
right_products = [1] * n
result = [1] * n

# Calculate left  products


# Calculate right products


# Calculate result by multiplying left and right products
for i in range(n):
    result[i] = left_products[i] * right_products[i]

print(result)
