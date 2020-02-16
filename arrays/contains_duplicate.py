"""
Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


def main():
    orig_list = [1, 2, 3, 1]
    assert containsDuplicate(orig_list) is True

    orig_list = [1, 2, 3, 4]
    assert containsDuplicate(orig_list) is False

    orig_list = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert containsDuplicate(orig_list) is True


if __name__ == '__main__':
    main()
