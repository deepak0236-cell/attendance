from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def backup_job():

    print("Database Backup Running")

scheduler.add_job(
    backup_job,
    'interval',
    hours=24
)

scheduler.start()