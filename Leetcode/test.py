nums = [-1, 0, 3, 5, 9, 12]
target = 2

left = 0
right = len(nums)

while left < right:
    mid = (left // 2) + (right // 2)
    print(left, mid, right)

    if nums[mid] == target:
        print(mid)
        exit()
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid

    input()

print(-1)
