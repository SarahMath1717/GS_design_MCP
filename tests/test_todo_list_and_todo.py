from lib.todo_list import *
from lib.todo import *

def test_add_works():
    tdl = TodoList()
    tdl.add("check")
    assert tdl.list == ["check"]

def test_task_marked_as_true():
    tdl = TodoList()
    tdl.add("feed snakes")
    tdl.add("sort laundry")
    tdl.add("get milk")
    assert tdl.list == ["feed snakes", "sort laundry", "get milk"]
    tdl.list[1].complete
    