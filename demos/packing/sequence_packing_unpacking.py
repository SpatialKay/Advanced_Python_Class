nums = [1, 2, 3]

# unpacking
first, second, third = nums

print(first)
print(second)
print(third)

# unpacking into first, unpcking remaining elements into others <= unpacking
first, *others, last = nums
#     ^ packing

print(first)
print(others)
print(last)

nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7, 8]

nums = [*nums1, *nums2]
print(nums)

# packing operator
# *<variable> = <itirable>

# unpacking operator
# <variable> = *<itirable>