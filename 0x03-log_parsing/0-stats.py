#!/usr/bin/python3
'''
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size> (if the format is not this one, the line
    must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:

    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size>
    (see input format above)

    Number of lines by status code:
        #possible status code: 200, 301, 400, 401, 403, 404, 405 and 500

        #if a status code doesn’t appear or is not an integer, don’t
        print anything for this status code

        #format: <status code>: <number>
        status codes should be printed in ascending order
'''
import sys
import re

log_regex = (
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
    r'\[(.+?)\] '
    r'"GET \/projects\/260 HTTP\/1\.1" '
    r'(\d{3}) (\d+)$'
)

line_count = 0
file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0,
                      401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def print_metrics():
    '''
    Helper function to prints metrics
    '''
    print(f"File size: {file_size}")

    for code, count in status_code_counts.items():
        if count > 0:
            print(f"{code}: {count}")


try:
    for line in sys.stdin:
        line = line.strip()
        line_count += 1

        match = re.fullmatch(log_regex, line)
        if match:
            file_size += int(match.group(4))
            try:
                status_code = int(match.group(3))
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            except Exception:
                pass

        if line_count == 10:
            print_metrics()
            line_count = 0

except (KeyboardInterrupt, EOFError):
    print_metrics()
    sys.exit(0)

print_metrics()
