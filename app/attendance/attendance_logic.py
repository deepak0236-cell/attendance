from datetime import datetime

def calculate_percentage(total, present):

    if total == 0:
        return 0

    return round((present / total) * 100, 2)

def is_late(attendance_time):

    current = datetime.now().time()

    return current > attendance_time