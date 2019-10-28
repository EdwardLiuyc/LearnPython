# 梳排序
# 冒泡排序的改进版本

import time
from nums_gen import num_set_for_sort
import matplotlib.pyplot as plt


def comb_sort(input_nums, plot_fig=False):
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    s = 1.3  # 经验参数
    nums = input_nums[:]
    count = len(nums)
    if count <= 1:
        return nums

    # step1
    step = int(count / s)
    while step > 1:
        for i in range(count - step):
            if nums[i] > nums[i+step]:
                nums[i], nums[i+step] = nums[i+step], nums[i]
                if plot_fig:
                    ax1.clear()
                    ax1.bar(range(len(nums)), nums)
                    plt.pause(0.05)
        step = int(step / s)

    # step2
    again = True
    for i in range(count-1):
        again = False
        for j in range(count - 1 - i):
            if(nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
                again = True
                if plot_fig:
                    ax1.clear()
                    ax1.bar(range(len(nums)), nums)
                    plt.pause(0.05)
        if again != True:
            break

    if plot_fig:
        plt.show()
    return nums


if __name__ == '__main__':
    init_nums = num_set_for_sort()
    # start = time.process_time()
    init_nums = comb_sort(init_nums, True)
    # end = time.process_time()
    # print(end-start)
    print(init_nums)
