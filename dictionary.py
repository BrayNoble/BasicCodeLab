patient_1 = {
    "last_name" : "Noble",
    "first_name" : "Brayen",
    "address" : "10299 new road",
    "city" : "North Jackson",
    "state" : "OH",
    "zip" : "44451",
    "age" : "17",
}

print(f"The patients name is {patient_1["first_name"], patient_1["last_name"]}")
print(f"The patients name is {patient_1.get["first name"], patient_1.get["last_name"]}")

print(patient_1)
patient_1["last_name"] = "sandwich"
print(patient_1)

for item in patient_1:
    print(item)