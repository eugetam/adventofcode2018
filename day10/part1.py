import numpy as np

with open(r'2018\day10\input.txt') as f:
    lines = f.readlines()

arr = np.zeros((len(lines), 4), dtype='int64')
#position=< 9,  1> velocity=< 0,  2>
for i, line in enumerate(lines):
    line = line.replace('position=<', '')
    line = line.replace('velocity=<', '')
    line = line.strip()
    fields = line.split()
    x = int(fields[0][:-1])
    y = int(fields[1][:-1])
    vx = int(fields[2][:-1])
    vy = int(fields[3][:-1])
    arr[i] = [x, y, vx, vy]

#print(arr)

def printstars(arr, printpic=False):
    xmin = np.min(arr[:,0])
    xmax = np.max(arr[:,0])
    ymin = np.min(arr[:,1])
    ymax = np.max(arr[:,1])
    piclist = []
    for y in range(ymin, ymax+1):
        row = ['.' for x in range(xmin, xmax+1)]
        piclist.append(row)
        
    for star in arr:
        piclist[star[1]-ymin][star[0]-xmin] = '#'
    
    pic = [''.join(row) for row in piclist]
    if printpic:
        print('\n'.join(pic))
    return (len(pic)* len(pic[0]))


size_arr = []
for count in range(100000):
    arr[:, 0] = arr[:, 0] + arr[:, 2]
    arr[:, 1] = arr[:, 1] + arr[:, 3]
    area =  (np.max(arr[:,0]) - np.min(arr[:,0])) * (np.max(arr[:,1]) - np.min(arr[:,1])) 
    size_arr.append(area)
    if count == 10417:          # section added after min area count determined 
        # print(area)
        # print(np.max(arr[:, 0]))
        # print(np.min(arr[:, 0]))
        # print(np.max(arr[:, 1]))
        # print(np.min(arr[:, 1]))
        printstars(arr, True)
        break
        
print(size_arr.index(min(size_arr)))