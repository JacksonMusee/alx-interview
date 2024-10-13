#!/usr/bin/python3
"""
Everythng in this module is about Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists as row of the Pascal's Triangle
    """
    triangle = []
    row_num = 0

    if n > 0:
        for row_num in range(n):
            new_row = []
            if row_num == 0:
                new_row.append(1)
            else:
                last_row = triangle[-1]
                for index in range(row_num + 1):
                    if index in (0, row_num):
                        new_row.append(1)
                    else:
                        new_row.append(last_row[index - 1] + last_row[index])
            triangle.append(new_row)

    return triangle
