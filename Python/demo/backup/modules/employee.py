import os, sys


class Employee:
    name = "Alex"

    def __init__(self) -> None:
        # Class name
        print("ClassName", type(self).__qualname__)
        print("ClassName", __class__)
        # Main path
        print("EmployeeMainPath", sys.argv[0])
        print("EmployeeMainDir", os.path.dirname(sys.argv[0]))
        print("EmployeeMainDir", os.path.dirname(os.path.realpath(sys.argv[0])))
        print("EmployeePath", __file__)
        # Class dir path
        print("Employee", os.path.dirname(__file__))

    @staticmethod
    def is_date_valid(date_as_string):
        print(Employee.name)
        day, month, year = map(int, date_as_string.split("-"))
        return day <= 31 and month <= 12 and year <= 3999

    def throwEx(self):
        try:
            raise Exception("Error_Age", "422")
            # raise ValueError
        except (OSError, ValueError):
            print("Could not convert data to an integer")
        except Exception as ex:
            # Destruct from tuples
            msg, code = ex.args
            print("Exception msg:", msg, "and code:", code)
            # Re throw exception
            # raise
        finally:
            # Run always
            # print("Unknown error")
            pass
