from datetime import datetime


print("cron.py был вызван")
with open("test.txt", "a") as f:
    f.write(f'Accessed on {str(datetime.now())}\n')
