def add_time(start, duration, day=None):
    # setting up the initial values for the program
    days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]
    am_or_pm = {"AM": "PM", "PM": "AM"}
    start_time, period = start.split()
    start_h, start_m = start_time.split(":")
    duration_h, duration_m = duration.split(":")
    total_minutes = int(start_m) + int(duration_m)
    total_hours = int(start_h) + int(duration_h)
    time_str = ""
    # if the sum of minutes add up to more than 60
    if total_minutes >= 60:
        total_minutes = total_minutes % 60
        total_hours += 1
    # remaining hours after the total hours are known
    remaining_hours = total_hours % 12
    # the value of hours should be 12 if the remaining hours is 0 using the ternary operator in python
    final_hours = remaining_hours if remaining_hours else 12
    # number of cycles of 12 hours to get the am and pm
    cycles_of_12h = total_hours // 12
    number_of_days = cycles_of_12h // 2
    # if the cycle is odd then it means that am has turned to pm and vice versa
    if cycles_of_12h % 2 != 0:
        # adding a day if pm is turned to am
        if period == "PM":
            number_of_days += 1
        # changing the period if the am is changed to pm or vice versa
        period = am_or_pm[period]
    # the final string to return
    time_str = f"{final_hours}:{total_minutes:02d} {period}"
    # get the day or days
    if day:
        [present_day_index] = [
            days.index(value) for value in days if value.lower() == day.lower()
        ]
        final_day_index = (present_day_index + number_of_days) % 7
        time_str += f", {days[final_day_index]}"
    # the number of days after adding the duration
    if number_of_days:
        days_str = (
            " (next day)" if number_of_days == 1 else f" ({number_of_days} days later)"
        )
        time_str += days_str
    return time_str


print(add_time("8:16 PM", "466:02", "tuesday"))
# print(add_time("11:43 AM", "2:20"))
# print(add_time("11:43 AM", "102:20"))
# print(add_time("6:30 PM", "205:12", "monDay"))
# print(add_time("11:43 PM", "24:20", "tueSday"))
# print(add_time("10:10 PM", "3:30"))
# print(add_time("11:30 AM", "2:32", "Monday"))
# print(add_time("11:43 AM", "00:20"))
# print(add_time("3:00 PM", "3:10"))

# * Old Solution

# def add_time(time, duration="", day=""):
#     x = tuple(time.split())
#     st = tuple(x[0].split(':'))
#     sd = tuple(duration.split(':'))
#     if duration == '' or duration == "0:00":
#         return time
#     h = int(st[0]) + int(sd[0])
#     m = int(st[1]) + int(sd[1])
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#     def day_of(day):
#         for i in days:
#             if day.lower() == i.lower():
#                 z = days.index(i)
#                 return ',' + ' ' + days[(z + n) % 7]
#             else:
#                 if day == '':
#                     return ''
#     if m > 60:
#         m = m % 60
#         take_over = 1
#     elif m == 60:
#         m = m % 60
#         take_over = 1
#     else:
#         take_over = 0

#     m = str(m)
#     if len(m) == 1:
#         m = '0' + m
#     h = h + take_over
#     y = ""
#     b = ""
#     if h < 12:
#         n = 0
#         if x[1] == "AM":
#             y += 'PM'
#             return str(h) + ':' + m + ' ' + y + day_of(day)
#         else:
#             return str(h) + ':' + m + ' ' + x[1] + day_of(day)
#     elif h == 12:
#         if x[1] == "AM":
#             y += "PM"
#             h = h
#             return str(h) + ':' + m + ' ' + y + day_of(day)
#         elif x[1] == "PM":
#             n = 1
#             y += "AM"
#             b += "(next day)"
#             h = h
#             return str(h) + ':' + m + ' ' + y + day_of(day) + ' ' + b
#     elif 12 < h < 24:
#         h = h % 12
#         if x[1] == "PM":
#             n = 1
#             y += "AM"
#             b += "(next day)"
#             return str(h) + ':' + m + ' ' + y + day_of(day) + ' ' + b
#         elif x[1] == "AM":
#             y += "PM"
#             n = 0
#             return str(h) + ':' + m + ' ' + y + day_of(day)
#     if duration == '24:00':
#         n = 1
#         return time + day_of(day) + ' ' + '(next day)'
#     if h >= 24:
#         n = int(h / 24) + 1
#         b += f"({n} days later)"
#         if h % 24 > 12 and x[1] == "PM":
#             y += "AM"
#             h = h % 24 % 12
#             return str(h) + ':' + m + ' ' + y + day_of(day) + ' ' + b
#         elif h % 24 > 12 and x[1] == "AM":
#             y += "PM"
#             h = h % 24 % 12
#             return str(h) + ':' + m + ' ' + y + day_of(day) + ' ' + b
#         else:
#             h = h % 24
#             if h <= 12 and x[1] == "AM":
#                 y += "PM"
#                 return str(h) + ':' + m + ' ' + y + day_of(day) + ' ' + b
#             elif h <= 12 and x[1] == "PM":
#                 y += "AM"
#                 return str(h) + ':' + m + ' ' + y + day_of(day) + ' ' + b
