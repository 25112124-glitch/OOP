x = int (input( 'minutes:'))
y = int (input( 'seconds:'))
print ( 'Total seconds is:', x * 60 + y ) 

z = float (input( 'Enter the distance (km):'))
print ('Distance in miles is:', '{:.2f}'.format(z / 1.61))

k = float ('{:.2f}'.format((z/1.61 )/(x+y/60)))
i = float ('{:.2f}'.format((z/1.61 )/((x+y/60)/60)))
print ('Average pace is:', k, 'miles per minute')
print ('Average speed is:', i, 'miles per hour')
