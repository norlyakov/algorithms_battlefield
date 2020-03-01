"""
Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
import string


def isPalindrome(s: str) -> bool:
    alphanumeric = string.ascii_letters + string.digits

    i, j = 0, len(s) - 1
    while True:
        if i > j:
            break
        ch1 = s[i]
        if ch1 not in alphanumeric:
            i += 1
            continue
        ch2 = s[j]
        if ch2 not in alphanumeric:
            j -= 1
            continue

        if ch1.lower() != ch2.lower():
            return False
        else:
            i += 1
            j -= 1

    return True


def main():
    s = "A man, a plan, a canal: Panama"
    assert isPalindrome(s) is True

    s = "race a car"
    assert isPalindrome(s) is False


if __name__ == '__main__':
    main()
