#!/usr/bin/python3
"""Technical interview this is my logic for optmized version we used this logic

"""
# triangle = []
#     for i in range(n):
#         list = [0] * (i + 1)
#         list[0] = 1
#         list [-1] = 1
#         if i > 1:
#             for j in range(1,i):
#                 list[j] = triangle[i-1][j-1] + triangle[i-1][j]
#         triangle.append(list)
#     return triangle
# ==============================================================
#     triangle = [[] for _ in range(n)]
#     for i in range(n):
#         triangle[i] = []* (i+1)
#         triangle[i][0] = 1
#         triangle[i][-1] = 1
#         if i > 1:
#             for j in range(1,i):
#                 triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
#     return triangle
#   ============================================================================


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n"""

    lists = []*n
    for i in range(n):
        lists.append([0]*i)

    for list in lists:
        list.insert(0, 1)
        if len(list) > 1:
            list[-1] = 1
    for i in range(2, n):
        for j in range(1, i):
            lists[i][j] = lists[i-1][j-1] + lists[i-1][j]
    return lists
