from schema import Student


def student_to_dict_without_address(student) -> dict:
    return {
        "name": student["name"],
        "age": student["age"],
    }

def student_to_dict(student) -> dict:
    return {
        "name": student["name"],
        "age": student["age"],
        "address": dict(student["address"])
    }


def students_to_list(students):
    return [student_to_dict_without_address(student) for student in students]



def student_model_to_dict(student : Student) -> dict:
    return {
        "name": student.name.lower(),
        "age": student.age,
        "address": {
            "city": student.address.city.lower(),
            "country": student.address.country.lower()
        }
    }

