import time


def get_time_period():
    local_time_hour = time.localtime().tm_hour
    if local_time_hour < 12:
        time_period = 'Morning'
    elif local_time_hour < 16:
        time_period= 'Afternoon'
    else:
        time_period = 'Evening'
    return time_period
