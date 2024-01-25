#!/usr/bin/python3
'''
    A simple module since it has only one funciton called `find_peak`.
'''


def find_peak(nums):
    '''Finds a peak in a list of unsorted integers.

    Parameters:
        - nums (list): array of integers

    Returns:
        - a peak if it's found, None otherwise
    '''

    size = len(nums)
    if size > 1:
        if nums[0] > nums[1]:
            return nums[0]
        elif nums[-1] > nums[-2]:
            return nums[-1]
        prev = nums[0]
        cur = nums[1]
        for i in range(2, size):
            next = nums[i]
            if prev <= cur >= next:
                return cur
            prev = cur
            cur = next
    return nums[0] if size == 1 else None
