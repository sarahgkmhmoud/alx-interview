#!/usr/bin/python3
"""technical interview"""


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.'''

    if n <= 0:
        return 0

    operations = 0
    clipboard = 1  # Start with 1 'H' in the clipboard
    remaining = n

    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n //= i
            remaining -= i
            if remaining == 0:
                return operations

    return operations
