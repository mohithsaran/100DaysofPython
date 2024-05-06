#Day 15 exercise solution

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)
if(hour>=0 and hour<12):
  print('Good Morning!')
elif(hour>=12 and hour<17):
  print('Good Afternoon')
elif(hour>=17 and hour<0):
  print('Good Night')
# https://docs.python.org/3/library/time.html#time.strftime