#!/usr/bin/python3
"""
UTF-8 Validation module.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    i = 0

    while i < len(data):
        if not 0 <= data[i] <= 0x10ffff:
            return False
        # checks for single-byte UTF-8 characters ASCII
        if data[i] <= 0x7f:
            i += 1
            continue

        # determine the number of bytes the character uses
        n_bytes = 0
        mask = 0b10000000
        while data[i] & mask:
            n_bytes += 1
            mask >>= 1

        if n_bytes < 2 or n_bytes > 4:
            return False

        # check continuation bytes
        for j in range(i + 1, i + n_bytes):
            if j >= len(data) or (data[j] & 0b11000000) != 0b10000000:
                return False

        i += n_bytes

    return True
