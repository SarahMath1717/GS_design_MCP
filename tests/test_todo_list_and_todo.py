from lib.todo_list import *
from lib.todo import *

def test_add_works():
    tdl = TodoList()
    tdl.add("check")
    assert tdl.list == ["check"]
    

def test_can_add_todos_and_retrieve_incomplete():
    t1 = Todo("Buy groceries")
    t2 = Todo("Wash car")
    tdl = TodoList()
    tdl.add(t1)
    tdl.add(t2)

    assert tdl.incomplete() == [t1, t2]
    assert tdl.complete() == []


def test_marking_a_todo_as_complete_removes_it_from_incomplete():
    t1 = Todo("Do laundry")
    t2 = Todo("Call mum")
    t2.mark_complete()

    tdl = TodoList()
    tdl.add(t1)
    tdl.add(t2)

    assert tdl.incomplete() == [t1]
    assert tdl.complete() == [t2]

def test_give_up_marks_all_todos_complete():
    t1 = Todo("Exercise")
    t2 = Todo("Pay bills")
    t3 = Todo("Write report")

    tdl = TodoList()
    tdl.add(t1)
    tdl.add(t2)
    tdl.add(t3)

    tdl.give_up()

    assert tdl.incomplete() == []
    assert tdl.complete() == [t1, t2, t3]