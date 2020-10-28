class Inline:
    # not worried about validation here because this is the user input, its parsed and rejected until a valid one is submitted.

    def __init__(self, classes=None, attributes=None, methods=None, global_testing=None, global_exporting=None):
        def cleanse(items: str):
            def clean(x): return x.strip()
            items = map(clean, items.split(","))
            return ",".join(items)
        self.classes = cleanse(classes.strip())
        self.attributes = cleanse(attributes.strip())
        self.methods = cleanse(methods.strip())
        self.global_testing = global_testing
        self.global_exporting = global_exporting

    @classmethod
    def from_inline(cls, inline: str):
        def testing(x): return True if x.count("-t") else False
        def exporting(x): return inline.split("-e")[1] if x.count("-e") else 0
        new_line = inline.split(":")
        modified_methods = new_line[2].split("-t")[0]
        return Inline(classes=new_line[0],
                      attributes=new_line[1],
                      methods=modified_methods,
                      global_testing=testing(inline),
                      global_exporting=exporting(inline))


if __name__ == "__main__":
    new_line = Inline.from_inline(
        "classA : attr1, attr2 : method1, method2 -t -e{us,ts,er}")
    print(new_line.global_testing)
