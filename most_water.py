height = [1,8,6,2,5,4,8,3,7]
w = len(height) - 1
left = 0 
right = len(height) - 1
res = 0 
res_in = 0
while left < right:
    if height[left] > height[right]:
        res_in = height[right] * w
        right -= 1
        w -= 1
        res = max(res_in, res)
    else:
        res_in = height[left] * w
        left += 1
        w -= 1
        res = max(res_in, res)
print(res)