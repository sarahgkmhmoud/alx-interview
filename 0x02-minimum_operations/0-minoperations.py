#!/usr/bin/python3
"""technical interview"""

def minOperations(n):
    if n <= 0:
        return 0

    operation = 0
    remaining = n
    character = 1


    while remaining > 0:
        if remaining % character == 0:
            remaining //= character
            operation += 1
        
        operation += 1
        character +=1
    
    return operation