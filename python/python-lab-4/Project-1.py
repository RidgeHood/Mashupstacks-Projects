from datetime import datetime,date
current=datetime.now()


print(f'Current date and time is {current}')
print(f'Current year is {date.today().year}')
print(f'Current month is {current.strftime("%B")}')
print(f'Current week number is {current.strftime("%V")}')
print(f'Current week number is {current.strftime("%A")}')
print(f'Current day of year is {current.strftime("%j")}')
print(f'Current day of month is {current.strftime("%d")}')
print(f'Current day of week is {current.strftime("%w")}')