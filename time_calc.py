def add_time(start, duration, start_day=None):

  print('\n\nstart = ', start)
  print('duration = ', duration)
  print('start_day = ', start_day)

  init = start.split()

  #hour substring
  hour_str = init[0].split(':')[0]
  minute_str = init[0].split(':')[1]

  #pm_am
  am_pm = init[1]

  #duration
  dur_hour_str = duration.split(':')[0]
  dur_minute_str = duration.split(':')[1]
  
  #calculate output - minutes segment
  tot_minute = int(minute_str) + int(dur_minute_str)
  add_hour = 1 if tot_minute > 59 else 0
  final_minute = tot_minute if tot_minute <= 59 else tot_minute - 60 
  final_minute_str = str(final_minute).rjust(2, '0')

  #calculate output - hour segment
  hour = int(hour_str)
  dur_hour = int(dur_hour_str)
  if am_pm.upper() == 'PM':
    hour += 12
  final_hour = hour + dur_hour + add_hour
  hour_mod = final_hour % 24

  #AM or PM
  final_am_pm = 'AM' if hour_mod < 12 else 'PM'

  #format hour
  hour_mod = 12 if hour_mod == 0 else hour_mod
  hour_12hr_format = hour_mod if hour_mod < 13 else hour_mod - 12 
  final_hour_str = str(hour_12hr_format)

  num_days = final_hour // 24
  num_days_str = ''
  if num_days == 1:
    num_days_str = ' (next day)'
  elif num_days > 1:
    num_days_str = ' ('+str(num_days)+' days later)'

  #days of the week
  day_of_week = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
  }

  final_day_of_week = ''
  start_day_index = 0
  if start_day is not None: 
    for day in day_of_week.values():
      if start_day.upper() == day.upper():
        break;
      start_day_index += 1
    
    final_day_index = (start_day_index + num_days) % 7
    final_day_of_week = ', '+day_of_week.get(final_day_index)

  #construct new time 
  new_time = final_hour_str+':'+final_minute_str+' '+final_am_pm
  new_time = new_time+final_day_of_week+num_days_str

  print('new_time = ',new_time)

  return new_time
