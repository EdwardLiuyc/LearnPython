from nums_gen import num_set_for_sort


def select_sort(input_nums):
    nums = input_nums[:]
    count = len(nums)
    if count <= 1:
        return nums
    else:
        for i in range(count):
            min_index = i
            min = nums[i]
            for j in range(i+1, count):
                if nums[j] < min:
                    min_index = j
                    min = nums[j]
            if min_index != i:
                nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


if __name__ == '__main__':
    init_nums = num_set_for_sort()
    # start = time.process_time()
    init_nums = select_sort(init_nums)
    # end = time.process_time()
    # print(end-start)
    print(init_nums)
