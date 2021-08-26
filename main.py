from application import salary
from db import people
from datetime import datetime as dt

if __name__ == '__main__':
    print(dt.today())
    salary.calculate_salary()
    people.get_employees()

