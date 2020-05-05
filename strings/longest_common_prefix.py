"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    s1 = min(strs)
    s2 = max(strs)
    for i, ch in enumerate(s1):
        if ch != s2[i]:
            return s1[:i]
    return s1


def main():
    inp = ["flower", "flow", "flight"]
    assert longestCommonPrefix(inp) == 'fl'

    inp = ["fl", "flow", "flight"]
    assert longestCommonPrefix(inp) == 'fl'

    inp = ["dog", "racecar", "car"]
    assert longestCommonPrefix(inp) == ''

    inp = ["", "racecar", "car"]
    assert longestCommonPrefix(inp) == ''

    inp = []
    assert longestCommonPrefix(inp) == ''

    inp = ['flower']
    assert longestCommonPrefix(inp) == 'flower'


if __name__ == '__main__':
    main()
