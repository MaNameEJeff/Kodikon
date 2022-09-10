from database import database

data_base = database()
t = data_base.db.child("Class3").child("Math").get()
print(dict(t.val())["FunWithNumbers"])




