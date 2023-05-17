from pytest import fixture
import mock
from todo import Task, TaskList


@fixture
def single_task():
    end_func = mock.MagicMock()
    end_kwargs = {"a": 0}
    return Task(0, "test task", 1, end_func, end_kwargs)


@fixture
def three_tasks():
    end_func_0 = mock.MagicMock()
    end_kwargs_0 = {"a": 0}
    end_func_1 = mock.MagicMock()
    end_kwargs_1 = {"b": 1}
    end_func_2 = mock.MagicMock()
    end_kwargs_2 = {"c": 2}
    return [
        Task(0, "test task", 1, end_func_0, end_kwargs_0),
        Task(1, "test task", 1, end_func_1, end_kwargs_1),
        Task(2, "test task", 1, end_func_2, end_kwargs_2),
    ]


@fixture
def empty_list():
    return TaskList(id=0, name="test list")


@fixture
def list_with_single_task(empty_list, single_task):
    single_task.start = mock.MagicMock()
    empty_list.add_task(single_task)
    return empty_list


@fixture
def list_three_tasks(three_tasks, empty_list):
    empty_list.add_tasks(three_tasks)
    return empty_list
