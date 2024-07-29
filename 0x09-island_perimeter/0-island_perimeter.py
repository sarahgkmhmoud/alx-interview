#!/usr/bin/python3
"""technical interview"""


def island_perimeter(grid):
    """   width_list = []
    height = 0
    for list in grid:
        width_pot = 0
        for item in list:
            if item == 1:
                width_pot += 1
        width_list.append(width_pot)
        if width_pot:
            height += 1

    width = max(width_list)
    perimeter = (width + height) * 2

    return perimeter
"""
    edges = 0
    for height in range(len(grid)):
        for width in range(len(grid[0])):
            if grid[height][width] == 1:
                edges += 4
                if width > 0 and grid[height][width-1] == 1:
                    edges -= 2
                if height > 0 and grid[height - 1][width] == 1:
                    edges -= 2
    return edges
