import time

now = time.time()

seconds = int(now)

minutes = seconds // 60

seconds = seconds % 60

hours = minutes // 60

minutes = minutes % 60

days = hours // 24

hours = hours % 24

timeOfDay = "Time of day is {}:{}:{}"
print(timeOfDay.format(hours, minutes, seconds))

daysSinceTheEpoch = "The number of days since the epoch : {}"
print(daysSinceTheEpoch.format(days))
