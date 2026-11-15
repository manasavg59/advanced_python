import pickle
import time

class Emp:
    def __init__(self,name,city,gender):
        self.name=name
        self.city=city
        self.gender=gender
    def display(self):
        print("Name:",self.name)
        print("city:",self.city)
        print("Gender:",self.gender)

e=Emp("Manasa","Manglore","Female")  

print("performing serialization using pickling")
time.sleep(2)

with open("employee.txt",'wb')as f:
    pickle.dump(e,f)
    print("sucessfull....")

print("de-serialization using pickle...")
time.sleep(2)
with open("employee.txt",'rb') as f:
    s1=pickle.load(f)
print("sucesful...")
time.sleep(2)
s1.display()
