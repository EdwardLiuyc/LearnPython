from bubble_sort import bubble_sort
from comb_sort import comb_sort
from quick_sort import quick_sort
from quick_sort import quick_sort_inplace
from select_sort import select_sort
from merge_sort import merge_sort
from nums_gen import num_set_for_sort

# import time


if __name__ == '__main__':
    init_nums = num_set_for_sort()
    print('poython sort:')
    # print(init_nums)
    list = sorted(init_nums)
    print(list)

    print('quick sort:')
    # print(init_nums)
    quick_sort_nums = quick_sort(init_nums)
    print(quick_sort_nums)

    print('quick sort in place:')
    # print(init_nums)
    quick_sort_in_place_nums = quick_sort_inplace(init_nums)
    print(quick_sort_in_place_nums)

    print('bubble sort:')
    # print(init_nums)
    bubble_sort_nums = bubble_sort(init_nums, True)
    print(bubble_sort_nums)

    print('select sort:')
    # print(init_nums)
    select_sort_nums = select_sort(init_nums)
    print(select_sort_nums)

    print('merge sort:')
    # print(init_nums)
    merge_sort_nums = merge_sort(init_nums)
    print(merge_sort_nums)

    print('comb sort:')
    # print(init_nums)
    comb_sort_nums = comb_sort(init_nums, True)
    print(comb_sort_nums)
