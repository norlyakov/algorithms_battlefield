"""
Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
import collections


def isAnagram(s: str, t: str) -> bool:
    length_s = len(s)
    if length_s != len(t):
        return False

    hash_map = collections.defaultdict(int)
    for ch in s:
        hash_map[ch] += 1

    for ch in t:
        hash_map[ch] -= 1
        if hash_map[ch] < 0:
            return False

    return True


def main():
    s = "anagram"
    t = "nagaram"
    assert isAnagram(s, t) is True

    s = "cat"
    t = "rat"
    assert isAnagram(s, t) is False


if __name__ == '__main__':
    main()
