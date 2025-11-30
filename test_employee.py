import employee_info

def test_get_employeesbyagerange():
    #arrange
    employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]

    #act
    result = employee_info.get_employees_by_age_range(23, 35)

    #assert
    assert result == employee_data

def test_calc_avg_sal():
    #arrange
    expected_result = 60166.67

    #act
    result = employee_info.calculate_average_salary()

    #assert
    assert result == expected_result

def test_getemployeebydept():
    #arrange
    employee_data = [
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    ]

    #act
    result = employee_info.get_employees_by_dept("Marketing")

    #assert
    assert result == employee_data