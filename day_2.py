#challenge: https://www.codewars.com/
# minutes to midnight
import datetime


round = lambda x: int(x) if x % 1 < 0.01 else int(x) + 1

#my answer
def minutes_to_midnight(d):
    midnight = datetime.datetime(d.year, d.month, d.day, 23, 59, 59)
    min = (midnight - d).seconds / 60
    return str(round(min)) + " minutes"


#best answer
# def minutes_to_midnight(d):
#     next_day = datetime.combine(d + timedelta(days=1), time.min)
#     remain = next_day - d
#     minutes = round(remain.seconds / 60)
#     return f'{minutes} minutes'
