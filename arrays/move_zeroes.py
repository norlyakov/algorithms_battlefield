"""
Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
from typing import List


def moveZeroes(nums: List[int]) -> None:
    length = len(nums)
    last_non_zero = -1
    cur = 0
    while cur < length:
        if nums[cur] != 0:
            last_non_zero += 1
            elem = nums[last_non_zero]
            nums[last_non_zero] = nums[cur]
            nums[cur] = elem
        cur += 1


def main():
    orig_list = [0, 1, 0, 3, 12]
    moveZeroes(orig_list)
    assert orig_list == [1, 3, 12, 0, 0]


if __name__ == '__main__':
    main()
