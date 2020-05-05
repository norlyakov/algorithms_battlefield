"""
Implement strStr()

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


def strStr(haystack: str, needle: str) -> int:
    len_needle = len(needle)
    if len_needle == 0:
        return 0

    for i in range(len(haystack) - len_needle + 1):
        if haystack[i: len_needle + i] == needle:
            return i

    return -1


def main():
    haystack = "hello"
    needle = "ll"
    assert strStr(haystack, needle) == 2

    haystack = "aaaaa"
    needle = "baa"
    assert strStr(haystack, needle) == -1

    haystack = ""
    needle = ""
    assert strStr(haystack, needle) == 0


if __name__ == '__main__':
    main()
