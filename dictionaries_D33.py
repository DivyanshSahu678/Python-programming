#day 33 

#dictionaries in python

dic = {
    "aman": 19,
    "sahil": 20,
    "sachin": 21,
    "rohit": 22
}
print(dic["aman"]) # 19

info = {"name": "aman", "age": 19 , "gender": "male"}
print(info)
print(info["name"])
print(info["age"])

#multiple values in dictionary

for key in info.keys():
    print(f"The value corresponding to the key {key} is:{info[key]}")
   
print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is:{value}") 
    