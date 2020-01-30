"""
Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
from typing import List, Iterable


def intersect(nums1: List[int], nums2: List[int]) -> Iterable:
    sorted1 = sorted(nums1)
    sorted2 = sorted(nums2)

    res = []
    pos1 = 0
    pos2 = 0
    while pos1 < len(nums1) and pos2 < len(nums2):
        elem1 = sorted1[pos1]
        elem2 = sorted2[pos2]
        if elem1 == elem2:
            res.append(elem1)
            pos1 += 1
            pos2 += 1
        elif elem1 > elem2:
            pos2 += 1
        else:
            pos1 += 1

    return res


def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert intersect(nums1, nums2) == [2, 2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    assert intersect(nums1, nums2) == [4, 9]


if __name__ == '__main__':
    main()
