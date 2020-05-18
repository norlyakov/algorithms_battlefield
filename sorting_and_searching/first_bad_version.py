"""
First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""


def firstBadVersion(n):
    if not isBadVersion(n):
        return None

    bad_version = n
    valid_version = 0
    while bad_version - valid_version > 1:
        _ver = (bad_version + valid_version) // 2
        if isBadVersion(_ver):
            bad_version = _ver
        else:
            valid_version = _ver

    return bad_version


def main():
    n = 5
    isBadVersion.first_bad_ver = 2
    assert firstBadVersion(n) == isBadVersion.first_bad_ver


def isBadVersion(ver):
    if not hasattr(isBadVersion, 'first_bad_ver'):
        raise ValueError('Set first_bad_ver for isBadVersion function')
    return ver >= isBadVersion.first_bad_ver


if __name__ == '__main__':
    main()
