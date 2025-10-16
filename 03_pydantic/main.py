from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Optional

class User(BaseModel):
    id: int
    name: str
    rols: List[str]
    tasks: Optional[List[dict[str, str]]] = None

    surname: str = Field (
        ...,                    #... means this field is mandetotery
        min_length = 0,
        max_length = 10000,
        description = "employee surname"
    )

    age: int
    @field_validator('age')
    def validate_age(x):
        if x > 100:
            raise ValueError('invalid age')
        return x

user_1 = {
    'id':1,
    'name':'dipak',
    'rols':['asd', 'asd2'],
    # 'tasks':[{'t1':'this is task 1'}],
    'surname':'khade' ,
    'age':12
}

user_2 = {
    **user_1,
    'name':'gaurav'
}

user_1_instance = User(**user_1)
user_2_instance = User(**user_2)

print(user_2_instance.name)
