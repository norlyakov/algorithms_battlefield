"""
Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
def reverse(x: int) -> int:
    positive = True
    if x < 0:
        x = -x
        positive = False

    max_int = 2 ** 31

    new_x = 0
    while x:
        new_x *= 10
        remainder = x % 10
        x = x // 10
        new_x += remainder
        if new_x > max_int:
            return 0

    return new_x if positive else -new_x


def main():
    input = 123
    assert reverse(input) == 321

    input = -123
    assert reverse(input) == -321

    input = 120
    assert reverse(input) == 21

    input = -1534236469
    assert reverse(input) == 0


if __name__ == '__main__':
    main()
