import re
import os
import sys
import time
import random

duration = path = rand = transition = False

i = 1
while i < len(sys.argv):
    if sys.argv[i] == '-d' and i < len(sys.argv)-1:
        path = sys.argv[i+1]
        i += 1
    elif sys.argv[i] == '-t' and i < len(sys.argv)-1:
        duration = sys.argv[i+1]
        i += 1
    elif sys.argv[i] == '-r':
        rand = True
    elif sys.argv[i] == '-T':
        transition = True

    i += 1

if duration:
    try:
        duration = float(duration)
    except:
        duration = 60
else:
    duration = 60

if not path or not os.path.isdir(path):
    path = os.getcwd()

extensions = ['jpeg', 'jpg', 'png', 'bmp']
pattern = re.compile(f'.*\.({"|".join(extensions)})$')
images = [path+'/'+f for f in os.listdir(path) if pattern.search(f.lower())]

if len(images) == 0: exit(1)

if rand:
    random.shuffle(images)
else:
    images.sort(key = str.lower)

print(f'Images: {len(images)}')
print(f'Duration: {duration} secs')
print(f'Random: {bool(rand)}')
print(f'Transition: {bool(transition)}')

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

    f.write('</background>\n')
