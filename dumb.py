from todo import Task, scheduler
from time import sleep

t = Task(0, "test task", 10, "random end of test job data")
t.start()
i = 0

while True:
    sleep(1)
    print(scheduler.get_jobs())
