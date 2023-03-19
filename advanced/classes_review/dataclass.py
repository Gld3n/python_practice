from dataclasses import dataclass, field

# dataclasses are like the structs from Golang
@dataclass
class Developer:
    name: str
    age: int
    skills: set
    pets: list = field(repr=False, default=None)
    has_degree: bool = False
    
dev1 = Developer('Robert', 18, {'Python', 'MarkDown', 'Django', 'FastAPI'}, pets=['Chiqui'])
dev2 = Developer('Alejandro', 18, {'Typescript', 'Deno','MarkDown', 'Rust', 'React'}, has_degree=False)

print(dev1)
print(dev2)
print(dev1.skills.symmetric_difference(dev2.skills))
print(dev1.skills.intersection(dev2.skills))