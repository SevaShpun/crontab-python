import time
import os
from apscheduler.schedulers.background import BackgroundScheduler


class CronTab:
    i = 0
    second = 5

    def job(self):
        self.i = 0
        os.system("python cron.py")

    def run(self):
        with open("test.txt", "w") as f:
            f.write('')
        # creating the BackgroundScheduler object
        scheduler = BackgroundScheduler()
        # setting the scheduled task
        scheduler.add_job(self.job, "interval", seconds=self.second)
        # starting the scheduled task using the scheduler object
        scheduler.start()

        try:
            # To simulate application activity (which keeps the main thread alive).
            while True:
                time.sleep(1)
                os.system("clear")
                self.i+=1
                print("Прошло", self.i, "сек")
        except (KeyboardInterrupt, SystemExit):
            # Not strictly necessary but recommended
            scheduler.shutdown()


def main():
    cron = CronTab()
    cron.second = 5
    cron.run()


if __name__ == "__main__":
    main()
