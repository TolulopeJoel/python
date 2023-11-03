# inital solution
def number(nums):
    min_num = int(100)
    for num in nums:
        if num < min_num:
            min_num = num

    print(min_num)


number([23, 46, 4, 9, 2, 15])

# function does not work properly when numbers are greater than 100
number([105, 548, 761, 321])


# fixed solution
def min_num(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    print(min_num)


min_num([1000000, 105, 761, 321, 43])
