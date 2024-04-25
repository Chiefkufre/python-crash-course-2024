# dictionary

# key-values pairs


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



# daniel = familyTree.get("daniel")

# {'tel': '090272651900', 'compl': 'dark', 'height': '170m', 'age': 35}

# familyTree.popitem()

villageTree = {
    "Jane": {
         "tel" : ["070272651800", "070272651800"],
         "compl": "dark",
         "height":  "170m",
         "age":  400,
         "marital_status": "Married"
     }
}

# familyTree.update()

villageTree.update(familyTree)

print(villageTree)