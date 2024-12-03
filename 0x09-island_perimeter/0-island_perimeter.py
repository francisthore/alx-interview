#!/usr/bin/env python3
"""Island Perimiter algo"""

def island_perimeter(grid):
    """Calculate perimeter."""
    width, height = len(grid[0]), len(grid)
    edges, size = 0, 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if j > 0 and grid[i][j - 1] == 1:
                    edges += 1
                if i > 0 and grid[i - 1][j] == 1:
                    edges += 1
    return size * 4 - edges * 2
