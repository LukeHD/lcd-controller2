class Widget(object):
    
    active = None
    renderer = None
    
    def __init__(self, name, parent)
        self.name = name
        self.parent = parent
    
    
    def next(self):
        pass
    
    
    def prev(self):
        pass
    
    
    def select(self):
        pass
    
    
    def __dispatch__(self, func, args=None):
        if self.active == self:
            arg_str = ""
            for arg in args:
                arg_str += arg + ", "
            return eval("self."+func+"("+arg_str+")")
            