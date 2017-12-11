import re
import os
import sys
import time
import random

duration = sys.argv[1:2]
duration = "".join(duration)

if not re.search('^([0-9]+|[0-9]*.[0-9]+)$', duration):
    duration = 60
else:
    duration = float(duration)
    if not duration > 0:
        duration = 60

extensions = ['jpeg', 'jpg', 'png', 'bmp']
path = os.getcwd()
pattern = re.compile('.*\.(jpeg|png|jpg|bmp)$')
images = [path+'/'+f for f in os.listdir(path) if pattern.search(f.lower())]

if len(images) == 0: exit(1)

if re.search(' random ', " "+" ".join(sys.argv)+" "):
    random.shuffle(images)
else:
    images.sort(key = str.lower)

if re.search(' transition ', " "+" ".join(sys.argv)+" "):
    transition = True
else:
    transition = False

print(f'Images: {len(images)}\nDuration: {duration} secs')

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

    for i in range(0, len(images)):
          f.write('<static>\n')
          f.write(f'  <duration>{duration}</duration>\n')
          f.write(f'  <file>{images[i]}</file>\n')
          f.write('</static>\n\n')

          if i < len(images)-1 and transition:
              f.write('<transition type="overlay">\n')
              f.write('  <duration>1.0</duration>\n')
              f.write(f'  <from>{images[i]}</from>\n')
              f.write(f'  <to>{images[i+1]}</to>\n')
              f.write('</transition>\n\n')
