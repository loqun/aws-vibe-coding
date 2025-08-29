from dataclasses import dataclass

@dataclass(frozen=True)
class ChildInfo:
    name: str
    age: int
    special_needs: str = ""
    allergies: str = ""
    pickup_authorization: str = ""
    special_instructions: str = ""
    
    def __post_init__(self):
        if not self.name or self.age < 0:
            raise ValueError("Name is required and age must be non-negative")