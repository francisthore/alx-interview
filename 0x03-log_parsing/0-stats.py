#!/usr/bin/python3
"""
Script to parse logs from stdin and compute metrics.
"""

import sys


def display_metrics(status_counts: dict, total_size: int) -> None:
    """
    Prints the accumulated file size and status code counts.
    """
    print("File size: {}".format(total_size))
    for status, count in sorted(status_counts.items()):
        if count > 0:
            print("{}: {}".format(status, count))


if __name__ == '__main__':
    total_size, line_count = 0, 0
    valid_status_codes = ["200", "301", "400", "401",
                          "403", "404", "405", "500"]
    status_counts = {code: 0 for code in valid_status_codes}

    try:
        for log_line in sys.stdin:
            line_count += 1
            log_parts = log_line.split()

            try:
                status_code = log_parts[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except IndexError:
                pass

            try:
                file_size = int(log_parts[-1])
                total_size += file_size
            except (IndexError, ValueError):
                pass

            if line_count % 10 == 0:
                display_metrics(status_counts, total_size)

        display_metrics(status_counts, total_size)

    except KeyboardInterrupt:
        display_metrics(status_counts, total_size)
        raise
