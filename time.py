def to_normal(time):
    decimal_hours = float(time)
    hours = int(decimal_hours)
    minutes = (decimal_hours - hours) * 60
    rounded_up = int(minutes) + int((minutes * 10 % 10 >= 5))
    if rounded_up<10:
        r='0'+str(rounded_up)
    else:
        r=rounded_up
    return f"{hours}:{r}"



def to_decimal(time):
    if isinstance(time, int):
        hours = time // 60
        minutes = time % 60
    elif isinstance(time, str):
        hours, minutes = map(int, time.split(":"))
    decimal_hours = hours + (minutes / 60)
    return round(decimal_hours, 2)