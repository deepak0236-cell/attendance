import csv

def export_report(data):

    with open(
        'attendance_report.csv',
        'w',
        newline=''
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            'Student',
            'Status'
        ])

        writer.writerows(data)