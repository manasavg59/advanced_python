import json
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
print(type(e))
e1=e.__dict__
print(type(e1))

print("performing serialization using json")
time.sleep(2)
print("using dumps")
time.sleep(2)
s1=json.dumps(e1)
print(s1)
print("sucessfull using dumps.....")
time.sleep(2)
print("using dump....")
time.sleep(2)
with open('emp12.json','w') as f:
    json.dump(e1,f)
print('.......')
print('de-serialization........')
time.sleep(2)
print('using loads') 
print('......')
s2=json.loads(s1)
print('......')
print(s2)    
    
print('using loads')    
print("...........")
time.sleep(2)
with open('emp12.json','r') as f:
    s3=json.load(f)
print("using load successfull....")
print(s3)

e3=Emp(s3['name'],s3['city'],s3['gender'])
e3.display()


