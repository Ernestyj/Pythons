import sys
import re
from collections import defaultdict
import datetime
from dateutil import parser


inStr = '''2024-05-01 16:55:12.5151 EDT -E.
2024-05-01 16:55:13.746381 EDT -E.
2024-05-01 16:55:13.746418 EDT -E.
2024-05-01 16:55:13.746504 EDT jsmith
2024-05-01 16:55:13.746564 EDT jsmith
2024-05-01 16:55:13.746524 EDT -E.
2024-05-01 16:55:13.746686 EDT -E.
2024-05-01 16:55:13.746769 EDT jsmith
2024-05-01 16:55:13.746809 EDT process124'''


outStr = '''
Sample output:
5
2024-05-01 16:55:12.5151 EDT
2024-05-01 16:55:13.746809 EDT
1.23
jsmith 3
process124 1

5
2024-05-01 16:55:12.5151 EDT
2024-05-01 16:55:13.746809 EDT
1.23
jsmith 3
process124 1



python scratch.py <<EOF
2024-05-01 16:55:12.5151 EDT -E.
2024-05-01 16:55:13.746381 EDT -E.
2024-05-01 16:55:13.746418 EDT -E.
2024-05-01 16:55:13.746504 EDT jsmith
2024-05-01 16:55:13.746564 EDT jsmith
2024-05-01 16:55:13.746524 EDT -E.
2024-05-01 16:55:13.746686 EDT -E.
2024-05-01 16:55:13.746769 EDT jsmith
2024-05-01 16:55:13.746809 EDT process124
EOF
'''




def main():
    log_lines = sys.stdin.read().strip().split('\n')

    error_count = 0
    start_time = None
    end_time = None
    user_count = defaultdict(int)

    for line in log_lines:
        # Check if the line is an error line
        if "-E" in line:
            error_count += 1

        pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+ [A-Z]{3})'
        match = re.search(pattern, line)
        if match:
            timestamp = match.group(1)

        if not start_time:
            start_time = timestamp

        end_time = timestamp

        # Extract username or process
        match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+ [A-Z]{3} (.*)$', line)
        if match:
            user = match.group(1)
            user_count[user] += 1

    # Calculate session length
    fmt = "%Y-%m-%d %H:%M:%S.%f %Z"
    # start_time_dt = datetime.datetime.strptime(start_time, fmt)
    # end_time_dt = datetime.datetime.strptime(end_time, fmt)
    start_time_dt = parser.parse(start_time)
    end_time_dt = parser.parse(end_time)
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
    main()
    # print(inStr.split('\n'))
    # main(inStr)
