day_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


def add_time(start, duration, starting_day=None):

    # aufbereitung der daten

    new_time_list = [0,0,0,"","",""]
    new_time = ""

    if starting_day != None:
        starting_day = starting_day.lower()

    start_list1 = start.split(" ")
    start_list1[0] = start_list1[0].split(":")
    start_list1[0][0] = int(start_list1[0][0])
    start_list1[0][1] = int(start_list1[0][1])

    duration_list1 = duration.split(":")
    duration_list1[0] = int(duration_list1[0])
    duration_list1[1] = int(duration_list1[1])

    match starting_day:
        case "monday":
            new_time_list[2] = 1
        case "tuesday":
            new_time_list[2] = 2
        case "wednesday":
            new_time_list[2] = 3
        case "thursday":
            new_time_list[2] = 4
        case "friday":
            new_time_list[2] = 5
        case "saturday":
            new_time_list[2] = 6
        case "sunday":
            new_time_list[2] = 7
        case None:
            new_time_list[2] = 0

    # berechnungen; umrechnung in normale stunden und minuten
    if start_list1[1] == "AM" and start_list1[0][0] < 12:
        new_time_list[0] = start_list1[0][0]
    elif start_list1[1] == "AM" and start_list1[0][0] == 12:
        new_time_list[0] = 0
    elif start_list1[1] == "PM" and start_list1[0][0] < 12:
        new_time_list[0] = 12 + start_list1[0][0]
    elif start_list1[1] == "PM" and start_list1[0][0] == 12:
        new_time_list[0] = 12

    new_time_list[1] = start_list1[0][1] + duration_list1[1]
    new_time_list[0] += duration_list1[0]
    if new_time_list[1] >= 60:
        new_time_list[0] += 1
        new_time_list[1] = new_time_list[1] % 60

    day_converter = 0

    if new_time_list[0] > 23 and new_time_list[0] < 48:
        day_converter = int(new_time_list[0] / 24)
        new_time_list[2] += day_converter
        new_time_list[0] = new_time_list[0] % 24
        new_time_list[4] = "(next day)"
    elif new_time_list[0] >= 48:
        day_converter = int(new_time_list[0] / 24)
        new_time_list[2] += day_converter
        new_time_list[0] = new_time_list[0] % 24
        new_time_list[4] = f"({str(day_converter)} days later)"

    if new_time_list[0] < 12:
        new_time_list[3] = "AM"
        if new_time_list[0] == 0:
            new_time_list[0] = 12
    else:
        new_time_list[3] = "PM"
        if new_time_list[0] == 12:
            new_time_list[0] = 12
        else:
            new_time_list[0] = new_time_list[0] % 12
    
    if starting_day != None:
        if new_time_list[2] > 0 and new_time_list[2] < 8:
            new_time_list[5] = day_list[new_time_list[2]-1] # ggf. Leerzeichen bei Monday falsch
        else:
            new_time_list[5] = day_list[new_time_list[2] % 7-1]

    if new_time_list[1] < 10:
        new_time_list[1] = "0" + str(new_time_list[1])
    else:
        new_time_list[1] = str(new_time_list[1])

    if starting_day == None and new_time_list[2] == 0:
        new_time = str(new_time_list[0]) + ":" + new_time_list[1] + " " + new_time_list[3]
    elif starting_day == None and new_time_list[2] > 0:
        new_time = str(new_time_list[0]) + ":" + new_time_list[1] + " " + new_time_list[3] + " " + new_time_list[4]

    if starting_day != None:
        new_time = str(new_time_list[0]) + ":" + new_time_list[1] + " " + new_time_list[3] + ", " + new_time_list[5]
        if new_time_list[4] != "":
            new_time += " " + new_time_list[4]

    return new_time

print(repr(f"{add_time('8:16 PM', '466:02', 'tuesday')}"))
print(repr('6:18 AM, Monday (20 days later)'))

print(repr(f"{add_time('3:00 PM', '3:10')}"))
print(repr('6:10 PM')) 

print(repr(f"{add_time('11:30 AM', '2:32', 'Monday')}"))
print(repr('2:02 PM, Monday')) 

print(repr(f"{add_time('11:43 AM', '00:20')}"))
print(repr('12:03 PM')) 

print(repr(f"{add_time('10:10 PM', '3:30')}"))
print(repr('1:40 AM (next day)')) 

print(repr(f"{add_time('11:43 PM', '24:20', 'tueSday')}"))
print(repr('12:03 AM, Thursday (2 days later)')) 

print(repr(f"{add_time('6:30 PM', '205:12')}"))
print(repr('7:42 AM (9 days later)')) 

print(repr(f"{add_time('3:30 PM', '2:12', 'Monday')}"))
print(repr('5:42 PM, Monday')) 

print(repr(f"{add_time('2:59 AM', '24:00', 'saturDay')}"))
print(repr('2:59 AM, Sunday (next day)')) 
