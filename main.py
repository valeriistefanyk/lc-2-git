import names
import random

def generate_name_by_gender():
    gender = input("Enter your gender [Male/Female or M/F]: ").lower()
    if gender == "male" or gender == "m":
        return names.get_first_name(gender="male")
    elif gender == "female" or gender == "f":
        return names.get_first_name(gender="female")
    else:
        return None

def generate_full_name(gender=None):
    if gender != "male" or gender != "female":
        gender = None
    return names.get_full_name(gender=gender)

def print_person_brief_info():
    full_name = generate_full_name()
    age = random.randint(14, 100)
    print(f"{full_name}, {age} years old")

if __name__ == "__main__":
    # func 1
    name = generate_name_by_gender()
    if name:
        print(f"Generated name: {name}")
    else:
        print("You entered incorrect gender")

    # func 2
    print(generate_full_name())
    print(generate_full_name(gender='female'))

    # func 3
    print_person_brief_info()
