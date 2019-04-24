

class DependencyInjector:

    def __init__(self):
        self.Registries = dict()

    def Register(self, cls_type, *args):
        self.Registries[cls_type] = args
    
    def Request(self, cls_type):
        return cls_type( *self.Registries[cls_type] )