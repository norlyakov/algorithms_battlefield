"""
Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    it = m + n - 1
    m -= 1
    n -= 1
    while n >= 0:
        if m >= 0 and nums1[m] > nums2[n]:
            nums1[it] = nums1[m]
            m -= 1
        else:
            nums1[it] = nums2[n]
            n -= 1
        it -= 1


def main():
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 3, 4, 5, 6]

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]


if __name__ == '__main__':
    main()
