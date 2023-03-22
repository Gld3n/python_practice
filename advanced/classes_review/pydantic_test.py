import pydantic
from typing import Optional
from json import load

class Developer(pydantic.BaseModel):
    name: str
    age: int
    skills: set
    pets: Optional[list]
    has_degree: Optional[bool] = False
    
    @pydantic.validator("skills")
    @classmethod
    def skills_detector(cls, skills):
        fastapi_detected = [s for s in skills if s == "FastAPI"]
        if fastapi_detected:
            skills.add("Promoted")
            return skills
        return skills

developers = [Developer(**developer) for developer in load(open("devs.json"))]

for dev in developers:
    print(dev)