import dataclasses
import datetime


@dataclasses.dataclass
class User:
    full_name: dict[str, str]
    email: str
    gender: str
    number: str
    date_of_birth: datetime.datetime
    hobbies: list[str]
    address: str
    state: str
    city: str
    image: str
    subject: str
