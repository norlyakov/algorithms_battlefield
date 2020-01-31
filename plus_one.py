"""
Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321."""
from typing import List


def plusOne(digits: List[int]) -> List[int]:
    add = 1
    for i in range(-1, -(len(digits) + 1), -1):
        digits[i] = digits[i] + add
        add = digits[i] // 10
        digits[i] = digits[i] % 10
        if add == 0:
            break

    if add:
        digits.insert(0, add)

    return digits


def main():
    orig_list = [0]
    assert plusOne(orig_list) == [1]

    orig_list = [1, 2, 9]
    assert plusOne(orig_list) == [1, 3, 0]

    orig_list = [4, 3, 2, 1]
    assert plusOne(orig_list) == [4, 3, 2, 2]


if __name__ == '__main__':
    main()
