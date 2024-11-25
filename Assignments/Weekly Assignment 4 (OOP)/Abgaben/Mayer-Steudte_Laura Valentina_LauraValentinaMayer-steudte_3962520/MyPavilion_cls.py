import uuid

class MyPavilion:
    project_name = None  # Class attribute for the project name

    def __init__(self, base_point=(0, 0, 0)):
        self.guid = self.generate_guid()
        self.base_point = base_point
        self.levels = []  # List to store associated levels


    @staticmethod
    def generate_guid():
        """Generate a unique GUID."""
        return uuid.uuid4()    
    
    @classmethod
    def set_project_name(cls, name):
        """Set the project name (shared across all objects)."""
        cls.project_name = name

    @classmethod
    def get_project_name(cls):
        """Get the project name."""
        return cls.project_name    

    def get_guid(self):
        return self.guid   

    def add_level(self, level):
        self.levels.append(level) 

    def get_levels(self):
        return self.levels     