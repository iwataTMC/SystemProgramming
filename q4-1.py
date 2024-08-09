def hash2(time_str):
    hours, minutes, seconds = map(int, time_str.split(":"))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds % 36
