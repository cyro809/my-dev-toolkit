import schedule
import time

def job():
    print("Running scheduled task")

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)