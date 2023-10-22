import datetime
from demoqa_tests.users.user import User

irina = User(
    full_name={"first_name": 'Irina', "last_name": 'Kirillova'},
    email='IrinaQA@gmail.com',
    gender='Female',
    number="8909898900",
    date_of_birth=datetime.datetime(day=15, month=3, year=1993),
    subject='Commerce',
    hobbies=['Reading'],
    image='Screenshot_1.png',
    address='Almaty, street Testovaya 1, 44',
    state='Haryana',
    city='Karnal',
)
