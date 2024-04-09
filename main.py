from fastapi import FastAPI, HTTPException, Path,status
from db import students_collection
from schema import Student,  StudentUpdate 
from pydantic.v1.utils import deep_update
from function import student_model_to_dict,student_to_dict,student_to_dict_without_address,students_to_list
from bson import ObjectId 

app = FastAPI()

@app.get('/')
async def welcome():
    return {
        "GET /docs": "For swagger documentaion"
    }


@app.post("/students/", status_code=status.HTTP_201_CREATED)
def post_students(student: Student) -> dict:
    res =  students_collection.insert_one(student_model_to_dict(student))
    return  {
        "id" :str(res.inserted_id)
    }



@app.get("/students/")
def get_all_students(country: str = None, age: int = None) -> dict:
    if age is not None and country is not None:
        db_students = students_collection.find({"age": age, "address.country": country},{"_id": 0,"address": 0})
    elif age is not None:
        db_students = students_collection.find({"age": age},{"_id": 0,"address": 0})    
    elif country is not None:
        db_students = students_collection.find({ "address.country": country.lower()},{"_id": 0,"address": 0})
    else:
        db_students = students_collection.find({},{"_id": 0,"address": 0})
    students = students_to_list(db_students)
    return {
        "data": students
    }



@app.get("/students/{id}")
def get_all_students(id: str) -> dict:
    db_student = students_collection.find_one({"_id": ObjectId(id)},{"_id": 0})
    student = student_to_dict(db_student)
    return student



@app.patch("/students/{id}",status_code=status.HTTP_204_NO_CONTENT)
def update_student(id: str,student : StudentUpdate | None = None):
    upd_stu = student.model_dump(exclude_unset=True)
    db_student = students_collection.find_one({"_id": ObjectId(id)})
    stu = student_to_dict(db_student)
    stu = deep_update(stu,upd_stu)
    students_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
        "name": stu["name"].lower(),
        "age": stu["age"],
        "address": {
            "city": stu["address"]["city"].lower(),
            "country": stu["address"]["country"].lower()
        }
    }})
    return {}


@app.delete("/students/{id}")
def delete_student(id : str):
    students_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {}





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)


  