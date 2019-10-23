import time
from nums_gen import num_set_for_sort


def bubble_sort(input_nums):
    nums = input_nums[:]
    count = len(nums)
    if count <= 1:
        return nums
    for i in range(count - 1):
        for j in range(count-1-i):
            if(nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == '__main__':
    init_nums = num_set_for_sort()
    # start = time.process_time()
    bubble_sort(init_nums)
    # end = time.process_time()
    # print(end-start)
    print(init_nums)
