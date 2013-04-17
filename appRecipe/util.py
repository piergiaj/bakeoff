def timeString(time):
  hours = time / 60
  minutes = time % 60
  if (hours > 0):
    return str(hours) + (' hour ' if hours==1 else ' hours ')+ str(minutes) + (' minute' if minutes==1 else ' minutes')
  else:
    return str(minutes) + (' minute' if minutes==1 else ' minutes')