#birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
appointment= {'name':'', 'time': ''}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in appointment:
        print(appointment[name] + ' is the schedule for ' + name)
    else:
        print('I do not have schedule information for ' + name)
        print('What time is the appointment?')
        time = input()
        appointment[name] = time
        print('Appointment database updated.')
