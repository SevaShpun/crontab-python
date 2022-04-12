import time
import os
from apscheduler.schedulers.background import BackgroundScheduler


class CronTab:
    i = 0

    def job(self):
        self.i = 0
        os.system("python cron.py")

    def run(self):
        # creating the BackgroundScheduler object
        scheduler = BackgroundScheduler()
        # setting the scheduled task
        scheduler.add_job(self.job, "interval", seconds=5)
        # starting the scheduled task using the scheduler object
        scheduler.start()

        try:
            # To simulate application activity (which keeps the main thread alive).
            while True:
                time.sleep(1)
                os.system("clear")
                self.i+=1
                print(self.i)
        except (KeyboardInterrupt, SystemExit):
            # Not strictly necessary but recommended
            scheduler.shutdown()


cron = CronTab()
cron.run()
