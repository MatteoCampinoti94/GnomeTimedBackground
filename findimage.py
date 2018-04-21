import bs4
import datetime, calendar
import os
import sys
import math

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    sys.exit(1)

if not os.path.isfile(file):
    sys.exit(2)

with open(file, 'r') as f:
    bkg = "".join(f.readlines())

bkg = bs4.BeautifulSoup(bkg, 'lxml')

starttime = []
for t in ('year', 'month', 'day', 'hour', 'minute', 'second'):
    starttime.append(int(bkg.find('starttime').find(t).string))

print('Start time: {}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}'.format(*starttime))
print('Curnt time: {}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}'.format(*nowtime))
deltatime = calendar.timegm(nowtime) - calendar.timegm(starttime)
print('Delta time:', deltatime, 'seconds')

image = ''
i = 0
bkg = bkg.findAll(['static', 'transition'])
while deltatime > 0:
    deltatime -= float(bkg[i].find('duration').string)
    if bkg[i].find('file'):
        image = bkg[i].find('file').string
    elif bkg[i].find('from') and bkg[i].find('to'):
        image = bkg[i].find('from').string + ' -> ' + bkg[i].find('to').string
    i += 1
    if i == len(bkg):
        i = 0

print('Image find:', image)
