student_info = {
    'roni': 50,
    'akash': 75,
    'sourav': 30
}

name = input("Enter the student's name: ")

if name in student_info:
    print(f"{name}'s marks: {student_info[name]} ")
else:
    print(f"{name} not found.")
