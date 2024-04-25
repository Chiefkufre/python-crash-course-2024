
# JSON - Javascript object notation

# API - application programming inferface

import json


familyTree = {
     
     "daniel": {
         "tel" : "090272651900",
         "compl": "dark",
         "height":  "170m",
         "age":  35,
     },

     "James": {
         "tel" : "070272651800",
         "compl": "Fair",
         "height":  "180m",
         "age":  35,
     },

     "Jane": {
         "tel" : ["070272651800", "070272651800"],
         "compl": "dark",
         "height":  "170m",
         "age":  22,
         "marital_status": "Single"
     }

}

py_json = json.dumps(familyTree)


# print(type(py_json))


famTree = json.loads(py_json)

print(type(famTree))