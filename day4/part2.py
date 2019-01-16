#[1518-03-17 00:01] falls asleep
from collections import Counter
import itertools
import re

with open(r'2018/day4/input.txt', 'r') as f:
    lines = f.readlines()
lines = sorted(lines)

guard = ''
total_sleep_count = {}
minute_track = []
count = 0
for line in lines:
    if 'Guard' in line and 'begins' in line:
        if guard and guard in total_sleep_count.keys():
            total_sleep_count[guard] += sleepcount
            minute_track.extend(minutes)
        elif guard:
            total_sleep_count[guard] = sleepcount
            minute_track.extend(minutes)
        result = re.search(r'\[.*\] Guard #(\d+)', line)
        guard = result.group(1)
        sleepcount = 0
        minutes = []
    elif 'falls asleep' in line:
        result = re.search(r'\[\d\d\d\d-\d\d-\d\d \d\d:(\d\d)\]', line)
        start_sleep = int(result.group(1))
    elif 'wakes up' in line:
        result = re.search(r'\[\d\d\d\d-\d\d-\d\d \d\d:(\d\d)\]', line)
        end_sleep =  int(result.group(1))
        sleepcount += end_sleep - start_sleep
        new_minutes = [(guard, x) for x in range(start_sleep, end_sleep)]
        minute_track.extend(new_minutes)
        count += len(new_minutes)

tally = Counter(minute_track)
guard, minute = max(tally, key=tally.get)
print(int(guard) * minute)
