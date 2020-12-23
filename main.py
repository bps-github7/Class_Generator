# from Parser.Inline import Inline

# inline = Inline.from_inline("skone : bisk, chalp : anal")

# print(inline.methods)

import json

items = json.loads('[{"id":123, "text":"Bisk"}, {"id" : "345", "text" : "chalp"}]')

for item in items:
    print(item['text'])
