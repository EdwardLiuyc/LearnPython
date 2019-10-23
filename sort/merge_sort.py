from nums_gen import num_set_for_sort


def merge_sort(input_nums):
    nums = input_nums[:]
    count = len(nums)
    if count <= 1:
        return nums
    elif count == 2:
        if nums[0] < nums[1]:
            return nums
        else:
            return nums[::-1]
    else:
        mid = count // 2
        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])
        i = 0
        j = 0
        for index in range(count):
            if left[i] < right[j]:
                nums[index] = left[i]
                i += 1
            else:
                nums[index] = right[j]
                j += 1

            if i == len(left):
                for remain_j in range(j, len(right)):
                    index += 1
                    nums[index] = right[remain_j]
                break
            if j == len(right):
                for remain_i in range(i, len(left)):
                    index += 1
                    nums[index] = left[remain_i]
                break
    return nums


if __name__ == '__main__':
    init_nums = num_set_for_sort()
    # start = time.process_time()
    init_nums = merge_sort(init_nums)
    # end = time.process_time()
    # print(end-start)
    print(init_nums)
