class Class_Dict:
    def __init__(self, classes=None, attributes=None, methods=None, parents=object):
        self.classes = classes
        self.attributes = attributes
        self.methods = methods
        self.parents = parents

    def __repr__(self):
        return {self.classes: (self.attributes, self.methods, "parents = {}".format(self.parents))}

    def __str__(self):
        return str(self.__repr__())

    @classmethod
    def to_classdict(cls, inline):
        return Class_Dict(*inline.split(":"))
