def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    # index = 1
    def value(index, value):

        this_index = (index + k) % length
        temp = nums[this_index]
        nums[this_index] = value
        index = this_index
        return index, temp

    if length %2 != 0:
        index, temp = value(0, nums[0])
        while index != 0:
            index, temp = value(index, temp)
    else:
        index, temp = value(0, nums[0])
        while index != 0:
            index, temp = value(index, temp)
        index, temp = value(1, nums[1])
        while index != 1:
            index, temp = value(index, temp)
    return nums





nums = [-1,-100,3,99]
print(rotate(nums, 2))
print(nums)