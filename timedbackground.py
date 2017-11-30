import glob
import re
import os
import sys
import time
import random

duration = sys.argv[1:2]
duration = "".join(duration)

if not re.search('^[0-9]+$', duration):
    duration = 60
else:
    duration = int(duration)

extensions = ['jpeg', 'jpg', 'png', 'bmp']
images = [] ; path = os.getcwd()
for e in extensions:
    images.extend(glob.glob(f'{path}/*.{e}'))

if re.search(' random ', " "+" ".join(sys.argv)+" "):
    random.shuffle(images)
else:
    images.sort()

if len(images) == 0: exit(1)

with open('background.xml', 'w') as f:
    f.write(f'''<background>
  <starttime>
    <year>{time.strftime("%Y")}</year>
    <month>{time.strftime("%m")}</month>
    <day>{time.strftime("%d")}</day>
    <hour>{time.strftime("%H")}</hour>
    <minute>{time.strftime("%M")}</minute>
    <second>{time.strftime("%S")}</second>
  </starttime>\n\n''')

    for i in images:
          f.write('<static>\n')
          f.write(f'<duration>{duration}</duration>\n')
          f.write(f'<file>{i}</file>\n')
          f.write('</static>\n\n')
