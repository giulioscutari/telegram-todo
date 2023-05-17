from apscheduler.schedulers.background import BackgroundScheduler
from slugify import slugify
from typing import Callable

scheduler = BackgroundScheduler()
scheduler.start()


class TaskList:
    id: int
    name: str
    tasks: list

    def __init__(self, id, name, tasks=[]) -> None:
        self.id = id
        self.name = slugify(name)
        self.tasks = []
        self.add_tasks(tasks)

    def start(self):
        if len(self.tasks):
            self.tasks[0].start()

    def add_task(self, task):
        if not isinstance(task, Task):
            raise ValueError()

        self.tasks.append(task)

    def add_tasks(self, tasks):
        if not hasattr(tasks, "__iter__"):
            raise ValueError()
        for i in tasks:
            i.belongs_to = self
        self.tasks = self.tasks + tasks

    def start_next_task(self, finished_task_id):
        finished_task_pos = [i.id for i in self.tasks].index(finished_task_id)
        if len(self.tasks) > finished_task_pos + 1:
            self.tasks[finished_task_pos + 1].start()


class Task:
    id: int
    name: str
    minutes_to_do: int
    end_timer_func: Callable
    end_timer_kwargs: dict
    job_id = None
    finished = False
    belongs_to = None

    def __init__(
        self, id, name, minutes_to_do, end_timer_func, end_timer_kwargs=None
    ) -> None:
        self.id = id
        self.name = name
        self.minutes_to_do = minutes_to_do
        self.end_timer_func = end_timer_func
        self.end_timer_kwargs = end_timer_kwargs

    def start(self):
        print(f"starting task {self.id}")
        job = scheduler.add_job(
            self.finish, "interval", minutes=self.minutes_to_do
        )
        self.job_id = job.id

    def finish(self):
        scheduler.remove_job(self.job_id)
        self.finished = True
        if self.belongs_to:
            self.belongs_to.start_next_task(self.id)
        self.end_timer_func(**self.end_timer_kwargs)

    def __str__(self) -> str:
        return f"task {self.name}({self.id})"
