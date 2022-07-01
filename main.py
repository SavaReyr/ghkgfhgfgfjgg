from application.salary import calculate_salary
from db.people import get_employees
import datetime

def time():
    dt_now = datetime.datetime.now()
    return dt_now

if __name__ == '__main__':
    print(time())

if __name__ == '__main__':
    calculate_salary()
    get_employees()
