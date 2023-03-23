from pydantic import BaseModel, validator, Field, constr, conint
from json import load

class Developer(BaseModel):
    name: constr(strip_whitespace=True, strict=True, min_length=2)
    age: conint(gt=16, le=80, strict=True)
    skills: set
    # Discovered the | operator, which does the same as Optional[]
    #It's only available after Python 3.10
    pets: list | None
    has_degree: bool | None = Field(alias="hasDegree")
    
    @validator("skills")
    @classmethod
    def skills_detector(cls, skills):
        fastapi_detected = [s for s in skills if s == "FastAPI"]
        if fastapi_detected:
            skills.add("Promoted")
            return skills
        return skills

developers = [Developer(**developer) for developer in load(open("devs.json"))]

for dev in developers:
    print(dev.json(by_alias=True), end="\n\n")