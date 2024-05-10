#!/usr/bin/python3
"""
Method file for solving
"""


def validUTF8(data):
    """
    Method file for solving
    """
    def check(num):
        """
        Method file for solving
        """
        mask = 1 << (8 - 1)  # 10000000
        i = 0
        while num & mask:  # 11000110 & 100000
            mask >>= 1
            i += 1
        return i

    i = 0
    while i < len(data):
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            cur = check(data[i])
            if cur != 1:
                return False
            i += 1
    return True
