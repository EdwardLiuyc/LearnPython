import time
from nums_gen import num_set_for_sort
import matplotlib.pyplot as plt


def bubble_sort(input_nums, plot_fig=False):
    fig = plt.figure()

    ax1 = fig.add_subplot(1, 1, 1)
    nums = input_nums[:]
    count = len(nums)
    if count <= 1:
        return nums
    for i in range(count - 1):
        for j in range(count-1-i):
            if(nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
                if plot_fig:
                    ax1.clear()
                    ax1.bar(range(len(nums)), nums)
                    plt.pause(0.1)

    if plot_fig:
        plt.show()
    return nums


if __name__ == '__main__':
    init_nums = num_set_for_sort()
    # start = time.process_time()
    init_nums = bubble_sort(init_nums, True)
    # end = time.process_time()
    # print(end-start)
    print(init_nums)
