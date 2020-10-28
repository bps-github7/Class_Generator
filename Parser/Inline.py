class Inline:
    # not worried about validation here because this is the user input, its parsed and rejected until a valid one is submitted.

    def __init__(self, classes=None, attributes=None, methods=None, testing=None, exporting=None, parents=object):
        self.classes = classes
        self.attributes = attributes
        self.methods = methods
        self.testing = testing
        self.exporting = exporting
        self.parents = parents

    # alternative constructor
    @classmethod
    def from_inline(cls, inline: str):
        return Inline(*inline.split(":"))

    # need to find a way to work this into an instance method- can it be done. why yes of course!
    def testing(cls, inline: str):
        if inline.count("-t"):
            return True

    def export(cls, inline: str):
        if inline.count("-e"):
            return inline.split("-e")[1]


if __name__ == "__main__":
    new_line = Inline.from_inline(
        "classA : attr1, attr2 : method1, method2 -t")
    if new_line.methods.count("-"):
        switch = new_line.methods.split("-")[1]
        print(switch)
