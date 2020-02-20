"""
Reverse String

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


def reverseString(s: List[str]) -> None:
    length = len(s)

    for i in range(length//2):
        _elem = s[i]
        s[i] = s[length - i - 1]
        s[length - i - 1] = _elem


def main():
    input = ["h", "e", "l", "l", "o"]
    reverseString(input)
    assert input == ["o", "l", "l", "e", "h"]

    input = ["H", "a", "n", "n", "a", "h"]
    reverseString(input)
    assert input == ["h", "a", "n", "n", "a", "H"]


if __name__ == '__main__':
    main()
