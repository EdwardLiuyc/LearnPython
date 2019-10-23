import random


def num_set_for_sort():
    nums = []
    for _ in range(20):
        nums.append(random.randint(0, 30))

    print(nums)
    return nums


if __name__ == '__main__':
    num_set_for_sort()
