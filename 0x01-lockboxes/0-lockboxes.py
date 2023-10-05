#!/usr/bin/python3
"""
Lockboxes
"""

def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]
    while stack:
        node = stack.pop()
        for i in boxes[node]:
            if i < n and not visited[i]:
                visited[i] = True
                stack.append(i)

    return all(visited)