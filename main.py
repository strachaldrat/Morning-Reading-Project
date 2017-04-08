import urllib2
from datetime import datetime
import calendar
import json

now = datetime.now()

# Variables to be read out by text-to-speech
""" good morning. Its h:mm am on the (day of week, day date, month). The weather this morning is #(degrees)
with (scattered clouds, thunderstorms etc.). The sun will rise in #(mins)
at #(time). The weather in the afternoon will be (fuzzy)
"""
# Variables for paragraph
current_day_period = ""
current_hour = ""
current_minute = ""
current_time_period = ""

day_of_week = ""
current_date = now.day
ordinal_number = ""
current_month = ""


raw_conditions_dict = json.loads('http://api.wunderground.com/api/XXXX/conditions/q/XXXX/XXXX.json')
current_temperature = raw_conditions_dict[]

# tests for pm time and subtracts if true
if now.hour > 12:
    current_hour = str(now.hour - 12)
else:
    current_hour = str(now.hour)

# sets current_day_period depending on current_hour
if now.hour <= 11:
    current_day_period = "morning"
elif now.hour <= 16:
    current_day_period = "afternoon"
else:
    current_day_period = "evening"

# tests if the minute time equates to 0 and leaves variable empty if true
if now.minute == 0:
    current_minute = ""
else:
    current_minute = now.minute

# sets current_time_period to AM or PM
if now.hour > 12:
    current_time_period = "PM"
else:
    current_time_period = "AM"

# stores day of week in day_of_week variable

day_of_week = datetime.today()
day_of_week = str(calendar.day_name[day_of_week.weekday()])

temperature_morning = ""
conditions_morning = ""
minutes_to_sunrise = ""
sun_rise_time = ""

#sets ordinal_number
if now.day == 1:
    ordinal_number = "st"
elif now.day == 2:
    ordinal_number = "nd"
elif now.day == 3:
    ordinal_number = "rd"
else:
    ordinal_number = "th"

#stores name of month in current_month
current_month = calendar.month_name[now.month]

#extracts current_temperature from current_raw_conditions


# Text to speech reads:

tts = "Good %s. It's %s %s %s on %s the %s%s of %s. The weather in Newcastle is %s" % (current_day_period, current_hour,
                                                    current_minute, current_time_period, day_of_week, current_date,
                                                     ordinal_number, current_month, current_temperature )

print tts
