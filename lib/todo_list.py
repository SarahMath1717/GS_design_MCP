class TodoList:
    def __init__(self):
        self.list = []

    def add(self, todo):
        self.list.append(todo)

    def incomplete(self):
        return [todo for todo in self.list if not todo.complete]

    def complete(self):
        return [todo for todo in self.list if todo.complete]

    def give_up(self):
        for todo in self.list:
            todo.mark_complete()