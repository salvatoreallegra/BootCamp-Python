# -------------------------------------------------------
# day03_oop.py
# Basic OOP: class, constructor (__init__), instance methods.
# -------------------------------------------------------

class Task:
    """
    Represents a simple to-do task.
    A class bundles data (title, description, is_done) and behavior (mark_done).
    """

    def __init__(self, title, description="", is_done=False):
        """
        __init__ is the constructor. It runs when Task(...) is called.
        'self' is the instance being created; we attach attributes onto it.
        """
        self.title = title
        self.description = description
        self.is_done = is_done

    def mark_done(self):
        """
        Instance method: toggles state on 'self'.
        Methods read/write data on the current object.
        """
        self.is_done = True

    def __str__(self):
        """
        String representation used by print(t) and str(t).
        Helpful for debugging/logging.
        """
        return f"Task(title='{self.title}', done={self.is_done})"

# Create objects (instances) using the class "blueprint"
t1 = Task("Finish Day 3", "Learn validation + OOP")
t2 = Task("Start Day 4")

# Read the string form (calls __str__ under the hood)
print(t1)   # Task(title='Finish Day 3', done=False)

# Call an instance method to change state
t1.mark_done()
print(t1)   # Task(title='Finish Day 3', done=True)

print(t2)   # Task(title='Start Day 4', done=False)
