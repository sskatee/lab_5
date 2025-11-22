def bubble_sort(nums):

    def swap_1(i, j):
        arr1 = nums
        nums[i], nums[j] = nums[j], nums[i]

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                swap_1(i, i + 1)
                swapped = True

    return nums

nums = [11, 25, 333, 444, 21, 2, 5, 9, 178]


def selection_sort(nums1):
    for k in range(len(nums1)):
        lowest_value_index = k
        for j in range(k + 1, len(nums1)):
            if nums1[j] < nums1[lowest_value_index]:
                lowest_value_index = j
        nums1[k], nums1[lowest_value_index] = nums1[lowest_value_index], nums1[k]

    return nums1

nums1 = [13,1345,24,2,36,7,86,3]