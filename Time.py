time = input('Please enter your time: ')
hours, mins = time.split(':')
adjusted_hours = hours if int(hours)==12 else str(int(hours) % 12)
daytime = ['AM','PM'][int(hours)>=12]
print('Converted to English format: ' + adjusted_hours + ':' + mins + ' ' + daytime)