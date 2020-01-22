inputTime = input()
hours = int(inputTime.split(":")[0])
minutes = int(inputTime.split(":")[1])
startHours = 6
hourDegreesInterval = 15
minuteDegreesInterval = 0.25

if (hours < 6) or (hours > 18):
    print("I don't see the sun!")
else:
    result = (hours - startHours) * hourDegreesInterval + minutes * minuteDegreesInterval
    if result % 1 == 0.0:
        print(int(result))
    else:
        print(result)
