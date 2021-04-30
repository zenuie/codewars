def mark_readable(seconds):
    second = str(seconds % 3600 % 60).zfill(2)
    minutes = str(seconds % 3600 // 60).zfill(2)
    hours = str(seconds // 3600).zfill(2)
    return '{}:{}:{}'.format(hours, minutes, second)
