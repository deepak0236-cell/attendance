def verify_location(student_lat, student_long):

    college_lat = 12.9716
    college_long = 77.5946

    radius = 0.01

    if abs(student_lat - college_lat) < radius and \
       abs(student_long - college_long) < radius:

        return True

    return False