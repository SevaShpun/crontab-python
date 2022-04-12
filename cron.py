from datetime import datetime

with open("test.txt", "a") as f:
    f.write(f'Accessed on {str(datetime.now())}\n')
