import csv
import requests
import cProfile

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"


def download_file(url):
    response = requests.get(url)
    return response.text.splitlines()


def csv_reader(url):
    data = download_file(url)
    return csv.reader(data[1:])


def get_employees_by_department(department_name, reader):
    employees = []
    department_name = department_name.lower()

    for row in reader:
        if row[2].lower() == department_name:
            name = row[0] + ' ' + row[1]
            start_date = row[3]
            employees.append((name, start_date))

    employees.sort(key=lambda x: x[0].split()[-1])
    return employees


def main():
    department_name = input("Enter the department name: ")
    reader = csv_reader(FILE_URL)
    employees = get_employees_by_department(department_name, reader)

    if employees:
        print(f"People in the {department_name} department (sorted alphabetically):")
        for employee in employees:
            print(employee)
    else:
        print(f"No employees found in the {department_name} department.")

    # runctx = command for run with input
    locals_dict = {"department_name": department_name, "reader": reader}
    command = "get_employees_by_department(department_name, reader)"
    cProfile.runctx(command, globals(), locals_dict)


if __name__ == "__main__":
    main()
