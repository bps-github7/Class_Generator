class Inline:
    # not worried about validation here because this is the user input, its parsed and rejected until a valid one is submitted.

    def __init__(self, classes=None, attributes=None, methods=None, parents=object):
        self.classes = classes
        self.attributes = attributes
        self.methods = methods
        self.parents = parents

    # alternative constructor
    @classmethod
    def from_inline(cls, inline: str):
        return Inline(*inline.split(":"))
