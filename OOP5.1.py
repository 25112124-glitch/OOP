import time
spoche = time.time()
days = spoche // 86400
hours = (spoche % 86400) // 3600
minutes = (spoche % 3600) // 60
seconds = spoche % 60
print('the number of days since 1970 is','{:.0f}'.format(days), 'days')
print('the times since 1970 is','{:.0f}'.format(hours),'hours', '{:.0f}'.format(minutes), 'minutes', '{:.0f}'.format(seconds), 'seconds')
