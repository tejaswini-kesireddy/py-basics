from datetime import datetime, timedelta

today = datetime.now()
user = input('Enter the number of days you want to add:\n')
new_date = today + timedelta(days=int(user))
format_date = new_date.strftime('%A %B %d, %Y')
print(f'New date is: {format_date}')

# %B - month in words
# %A - day of the date
