from dataclasses import dataclass


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    date_of_birth: str
    birth_day: str
    birth_month: str
    birth_month_str: str
    birth_year: str
    subjects: list[str]
    hobbies: list[str]
    photo: str
    current_address: str
    state: str
    city: str

    @staticmethod
    def full_name(first_name, last_name):
        return ' '.join([first_name, last_name])

    @staticmethod
    def state_and_city(state, city):
        return ' '.join([state, city])
