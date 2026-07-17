user_profile = {

}

user_profile["name"] = input("Enter your name:")
user_profile["age"] = int(input("Enter your age:"))
user_profile["city"] = input("Enter your city:")


print(f"name: {user_profile['name']}")
print(f"age: {user_profile['age']}")
print(f"city: {user_profile['city']}")
if "city" in user_profile:
    print("City saved successfully")