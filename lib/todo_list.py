class TodoList:
    def __init__(self):
        self.list = []

    def add(self, todo):
        self.list.append ({"task": todo, "completed": False})

    def incomplete(self):
        return self.list

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass