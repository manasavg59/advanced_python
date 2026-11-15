

import json
import time

e={
    'name':'Manasa',
    'class':'python-gen-ai',
    'city':'Manglore',
    'is_t':True
}

print("performing serialization using json")
time.sleep(2)
print("using dumps")
time.sleep(2)
s1=json.dumps(e)
print(s1)
print("sucessfull using dumps.....")
time.sleep(2)
print("using dump....")
time.sleep(2)
with open('emp12.json','w') as f:
    json.dump(e,f)
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
