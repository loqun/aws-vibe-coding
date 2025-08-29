from dataclasses import dataclass

@dataclass(frozen=True)
class CustomerInfo:
    name: str
    email: str
    phone: str
    emergency_contact: str = ""
    
    def __post_init__(self):
        if not self.name or not self.email or not self.phone:
            raise ValueError("Name, email, and phone are required")