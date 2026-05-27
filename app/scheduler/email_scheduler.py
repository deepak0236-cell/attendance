from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def send_daily_email():

    print("Daily Emails Sent")

scheduler.add_job(
    send_daily_email,
    'cron',
    hour=8
)

scheduler.start()