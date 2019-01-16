#[1518-03-17 00:01] falls asleep
from collections import Counter
import re

with open(r'2018/day4/input.txt', 'r') as f:
    lines = f.readlines()
lines = sorted(lines)

guard = ''
total_sleep_count = {}
minute_track = {}
for line in lines:
    if 'Guard' in line and 'begins' in line:
        if guard and guard in total_sleep_count.keys():
            total_sleep_count[guard] += sleepcount
            minute_track[guard].extend(minutes)
        elif guard:
            total_sleep_count[guard] = sleepcount
            minute_track[guard] = minutes
        result = re.search(r'\[.*\] Guard #(\d+)', line)
        guard = result.group(1)
        sleepcount = 0
        minutes = []
    elif 'falls asleep' in line:
        result = re.search(r'\[\d\d\d\d-\d\d-\d\d \d\d:(\d\d)\]', line)
        start_sleep = int(result.group(1))
    elif 'wakes up' in line:
        result = re.search(r'\[\d\d\d\d-\d\d-\d\d \d\d:(\d\d)\]', line)
        sleepcount += int(result.group(1)) - start_sleep
        minutes.extend(list(range(start_sleep,int(result.group(1)))))
    

max_id = max(total_sleep_count, key=total_sleep_count.get)
count = Counter(minute_track[max_id])
max_min = max(count, key=count.get)

print(max_min*int(max_id))