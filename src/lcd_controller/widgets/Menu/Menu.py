from lcd_controller.widgets.Widget import Widget

class Menu(Widget):
    
    menu = None
    
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.menu = []
        self.active = self
    
    
    def add_entry(self, entry):
        self.menu.append(entry)
     
    
    def next(self):
        print("next")
    
    
    def prev(self):
        print("prev")
    
    
    def select(self):
        print("selected")
    
    
    def __dispatch__(self, func, args=None):
        if self.active == self:
            arg_str = ""
            for arg in args:
                arg_str += arg + ", "
            return eval("self."+func+"("+arg_str+")")
        else:
            self.active.__dispatch__(func, args)
        
    