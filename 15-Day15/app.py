import time

user = input('Enter your name: ')
timestamp = time.strftime('%H:%M:%S')
print("The current time is: " + timestamp)

if (timestamp > "06:00:00" and timestamp < "11:59:00"):
    print('Good morning ' + user)
elif (timestamp > "12:00:00" and timestamp < "16:59:00"):
    print('Good afternoon ' + user)
elif (timestamp > "17:00:00" and timestamp < "20:59:00"):
    print('Good evening ' + user)
else:
    print('Good night ' + user)
