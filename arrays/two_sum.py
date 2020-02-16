"""
Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i, val in enumerate(nums):
        term = target - val
        if term in d:
            pos1 = d[term]
            return [pos1, i]
        d[val] = i


def main():
    orig_list = [2, 7, 11, 15]
    target = 9
    assert twoSum(orig_list, target) == [0, 1]


if __name__ == '__main__':
    main()
