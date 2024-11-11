#!/usr/bin/python3
"""
Module to validate UTF-8 encoding.
"""


def validUTF8(data) -> bool:
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    """
    remaining_bytes = 0  # Tracks how many continuation bytes are expected

    for byte in data:
        leading_mask = 1 << 7

        if remaining_bytes == 0:
            while byte & leading_mask:
                remaining_bytes += 1
                leading_mask >>= 1

            if remaining_bytes == 0:
                continue

            if remaining_bytes == 1 or remaining_bytes > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0
