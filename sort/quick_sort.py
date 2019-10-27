from nums_gen import num_set_for_sort


def quick_sort(input_nums):
    nums = input_nums[:]
    count = len(nums)
    if count <= 1:
        return nums
    else:
        div = nums[0]
        less = []
        larger = []
        for i in range(1, count):
            if nums[i] <= div:
                less.append(nums[i])
            else:
                larger.append(nums[i])
        less = quick_sort(less)
        larger = quick_sort(larger)
        less.append(div)
        less.extend(larger)
        return less


def quick_sort_inplace(input_nums):
    nums = input_nums[:]
    count = len(nums)
    if count <= 1:
        return nums
    else:
        i = 0
        j = count - 1
        div = nums[0]
        while i != j:
            while nums[j] > div and i < j:
                j -= 1
            while nums[i] <= div and i < j:
                i += 1
            if i == j:
                nums[0], nums[i] = nums[i], nums[0]
                break
            else:
                nums[i], nums[j] = nums[j], nums[i]

        less = nums[:i]
        larger = nums[i+1:]
        less = quick_sort_inplace(less)
        larger = quick_sort_inplace(larger)
        less.append(nums[i])
        less += larger
        return less


if __name__ == '__main__':
    init_nums = num_set_for_sort()
    # start = time.process_time()
    init_nums = quick_sort_inplace(init_nums)
    # end = time.process_time()
    # print(end-start)
    print(init_nums)
