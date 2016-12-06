class Node:
    def __init__(self):
        self.data = None
        self.type = None
        self.parent = None
        self.n_child = 0
        self.children = []
        self.records = {}
        self.condition = None
        self.which_parent = None

    def set_wp(self, which_parent):
        self.which_parent = which_parent

    def is_empty(self):
        return (self.data is None)

    def set_parent(self, parent):
        self.parent = parent

    def set_condition(self, condition):
        self.condition = condition

    def get_condition(self):
        return self.condition
    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def set_data(self,data):
        self.data = data

    def get_parent(self):
        return self.parent

    def get_data(self):
        return self.data

    def get_n_child(self):
        return self.n_child

    def add_child(self, child):
        self.children.append(child)
        self.n_child += 1

    def get_children(self):
        return self.children