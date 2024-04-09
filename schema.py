from pydantic import BaseModel

class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

class UpdateAddress(BaseModel):
    city: str |None = None
    country: str|None = None


class StudentUpdate(BaseModel):
    name: str |None = None
    age: int | None = None
    address: UpdateAddress | None = None