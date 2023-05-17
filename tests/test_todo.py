import mock
from todo import scheduler 


def test_set_job_from_task(single_task):
    single_task.start()
    job = scheduler.get_job(single_task.job_id)
    assert job != None


def test_end_job(single_task):
    single_task.start()
    single_task.finish()
    single_task.end_timer_func.assert_called_with(**single_task.end_timer_kwargs)
    assert single_task.finished


def test_list_set_single_job(list_with_single_task):
    t = list_with_single_task.tasks[0]
    list_with_single_task.start()
    t.start.assert_called_once()


def test_add_task(single_task, empty_list):
    empty_list.add_task(single_task)
    assert empty_list.tasks[0].id == single_task.id
    assert empty_list.tasks[0].name == single_task.name
    assert empty_list.tasks[0].minutes_to_do == single_task.minutes_to_do
    assert isinstance(empty_list.tasks[0].end_timer_func, mock.MagicMock)
    assert empty_list.tasks[0].end_timer_kwargs == single_task.end_timer_kwargs


# def test_tasks_status(single_task, empty_list):
#     empty_list.add_task(single_task[0])
#     tasks = empty_list.get_tasks()


def test_multiple_tasks_in_list(list_three_tasks):
    list_three_tasks.start()
    list_three_tasks.tasks[0].finish()
    assert list_three_tasks.tasks[0].finished
    list_three_tasks.tasks[1].finish()
    assert list_three_tasks.tasks[1].finished
    list_three_tasks.tasks[2].finish()
    assert list_three_tasks.tasks[2].finished
