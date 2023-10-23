#!/usr/bin/python3
"""
Minoperations
"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """

    # The base case: If n is less than 2, we cannot perform any operations.
    if n < 2:
        return 0

    ops, root = 0, 2

    while root <= n:
        # Check if n is evenly divisible by the current root value.
        if n % root == 0:
            # Calculate the total operations by adding the root value.
            ops += root
            # Update n to be the result of the division by root.
            n = n / root
            # Reduce root to find remaining smaller values that evenly divide n.
            root -= 1

        # Increment root until it evenly divides n.
        root += 1

    return ops


