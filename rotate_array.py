"""
Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
from typing import List


def rotate(nums: List[int], k: int) -> None:
    length = len(nums)
    k = k % length

    if k == 0 or length == 0:
        return

    pos = 0
    i = 0
    while i < length:
        start = pos
        curr = nums[pos]
        while True:
            pos = (pos + k) % length
            _elem = nums[pos]
            nums[pos] = curr
            curr = _elem
            i += 1
            if start == pos or i == length:
                break
        pos += 1

    return


def main():
    orig_list = [1]
    k = 10
    rotate(orig_list, k)
    assert orig_list == [1]

    orig_list = [-1, -100, 3, 99]
    k = 2
    rotate(orig_list, k)
    assert orig_list == [3, 99, -1, -100]

    orig_list = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(orig_list, k)
    assert orig_list == [5, 6, 7, 1, 2, 3, 4]


if __name__ == '__main__':
    main()
