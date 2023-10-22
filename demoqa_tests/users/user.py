import dataclasses

@dataclasses.dataclass
class User:
    full_name: str
    email: str
    gender: str
    number: int
    date_of_birth: {day: str, month: str, year: str}
    hobbies: str
    address: str
    state: str
    city: str
    image: str
    subject: str
