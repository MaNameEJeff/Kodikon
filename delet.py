from database import database

data_base = database()
t = data_base.storage.child("Class1").child("Math").child("Chapter3/4.gif").get_url()
print(t)
