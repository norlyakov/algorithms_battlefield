"""
First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
import collections


def firstUniqChar(s: str) -> int:
    hash_map = collections.Counter(s)

    for i, ch in enumerate(s):
        if hash_map[ch] == 1:
            return i

    return -1


def main():
    s = "leetcode"
    assert firstUniqChar(s) == 0

    s = "loveleetcode"
    assert firstUniqChar(s) == 2


if __name__ == '__main__':
    main()
