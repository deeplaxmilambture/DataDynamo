'''
Use time module
'''


import time

timestamp= time.strftime('%H:%M:%S')
print(timestamp)

timestamp= time.strftime('%H')
print(timestamp)

timestamp= time.strftime('%M')
print(timestamp)

timestamp= time.strftime('%S')
print(timestamp)

timestamp= time.strftime('%a') #abbreviated weekday name
print(timestamp)

timestamp= time.strftime('%A') #full weekday name
print(timestamp)

timestamp= time.strftime('%b') #abbreviated month name
print(timestamp)

timestamp= time.strftime('%B') #full month name
print(timestamp) 

timestamp= time.strftime('%c') #appropriate date and time representation
print(timestamp)

timestamp= time.strftime('%d') #Day of month in decimal
print(timestamp)

timestamp= time.strftime('%I') #Hour- 24 hr clock format- decimal number
print(timestamp)

timestamp= time.strftime('%j') #Hour- 12 hr clock format- decimal number
print(timestamp)

timestamp= time.strftime('%m') #month as decimal number
print(timestamp)

timestamp= time.strftime('%M') #minute as decimal number
print(timestamp)

timestamp= time.strftime('%p') #locale equivalent either AM or PM
print(timestamp)

timestamp= time.strftime('%S') #Second as decimal number
print(timestamp)

timestamp= time.strftime('%U') #Week number of the year 0-52
print(timestamp)

timestamp= time.strftime('%w') #Weekday as decimal 0-7
print(timestamp)

timestamp= time.strftime('%W') # Week number of the year 0-53
print(timestamp)

timestamp= time.strftime('%x') #locale appropriate date representation
print(timestamp)

timestamp= time.strftime('%X') #locale appropriate time representation
print(timestamp)

timestamp= time.strftime('%y') #year without century as decimal number 0-99
print(timestamp)

timestamp= time.strftime('%Y') #year with century as decimal number 
print(timestamp)

timestamp= time.strftime('%z') #timezone offset either indicating a positive or negative time difference from UTC/GMT in the form of +HHMM or -HHMM
print(timestamp)

timestamp= time.strftime('%Z') #timezone name
print(timestamp)

