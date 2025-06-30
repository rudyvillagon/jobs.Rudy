list_of_keys = ["access_level", "age"]
employee = {
            "name": "John", 
            "email": "john@ecorp.com",
            "access_level": 5,
            "age": 28,
        }

for My_filter in list_of_keys:
    employee.pop(My_filter)

print(employee)