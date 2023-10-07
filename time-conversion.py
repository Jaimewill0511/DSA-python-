def time_conversion(time):
    time_of_day = time[-2:]
    hour = int(time[:2])
    rest_part_of_string = time[2:-2]
    if time_of_day == 'PM' and hour != 12:
        hour += 12
    elif hour != 12 and time_of_day == 'AM':
        hour = f'0{hour}'
    elif hour == 12 and time_of_day == 'PM':
        hour = 12
    else:
        hour = '00'

    new_time = f'{hour}{rest_part_of_string}'
    return new_time


print(time_conversion('07:05:45PM'))
