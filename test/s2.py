import sys
import re
from collections import defaultdict
import datetime


def main(input_file):
    with open(input_file, 'r') as file:
        log_lines = file.read().strip().split('\n')

    error_count = 0
    start_time = None
    end_time = None
    user_count = defaultdict(int)

    for line in log_lines:
        # Check if the line is an error line
        if "-E" in line:
            error_count += 1

        # Extract timestamp
        timestamp = line[:23]

        if not start_time:
            start_time = timestamp

        end_time = timestamp

        # Extract username or process
        match = re.search(r'EDT\s+([^\s]+)$', line)
        if match:
            user = match.group(1)
            user_count[user] += 1

    # Calculate session length
    fmt = "%Y-%m-%d %H:%M:%S.%f"
    start_time_dt = datetime.datetime.strptime(start_time, fmt)
    end_time_dt = datetime.datetime.strptime(end_time, fmt)
    session_length = (end_time_dt - start_time_dt).total_seconds()

    # Print results
    print(error_count)
    print(start_time)
    print(end_time)
    print(f"{session_length:.2f}")

    for user, count in sorted(user_count.items(), key=lambda item: item[1], reverse=True):
        if user=='-E.': continue
        print(user, count)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scratch.py <input_file>")
    else:
        main(sys.argv[1])
