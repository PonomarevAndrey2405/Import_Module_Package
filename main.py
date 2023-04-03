import datetime
from pandas_geojson import write_geojson
from Application.salary import calculate_salary
from Application.db.people import get_employees

now = datetime.datetime.now()

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(now.strftime("%d-%m-%Y %H:%M"))
