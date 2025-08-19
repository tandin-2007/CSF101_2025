name = "tandin wangchuk"  
age = 18 
height = 1.50  
is_student = True 

person_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}
print(person_info)
person_info["favorite_color"] = "pink" 
try:
    print(person_info["weight"])
except KeyError as e:
    print(f"Error: {e}")

