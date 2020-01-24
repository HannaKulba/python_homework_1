inputTime = input()
hours = int(inputTime.split(":")[0])
minutes = int(inputTime.split(":")[1])
start_hours = 6
hour_degrees_interval = 15
minute_degrees_interval = 0.25

if (hours < 6) or (hours > 18):
    print("I don't see the sun!")
else:
    result = (hours - start_hours) * hour_degrees_interval + minutes * minute_degrees_interval
    if result % 1 == 0.0:
        print(int(result))
    else:
        print(result)
