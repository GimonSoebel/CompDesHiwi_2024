from .MyPavilion_cls import*

#import MyPavilion_cls

class Level(MyPavilion):
    def __init__(self, name, baseheight, height):
        super().__init__()
        self.name = name
        self.baseheight = baseheight
        self.height = height    

    def get_info(self):
        return (f"Project: {self.get_project_name()}, "
                f"Level: {self.name}, GUID: {self.guid}, "
                f"Base Height: {self.baseheight}, Height: {self.height}")    
