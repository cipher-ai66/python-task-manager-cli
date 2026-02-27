class Task:
    def __init__(self, description, completed = False):
        self.description = description
        self.completed = completed
        
    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.description}"