from backup.modules.employee import Employee

import os, inspect

em = Employee()

# Main dir path
print("ClassName", type(em).__qualname__)
print("ClassName", em.__class__)
print("MainPath", __file__)
print("MainDir", os.path.dirname(__file__))

# Module dir path
print("Path", inspect.getfile(Employee))
print("Path", inspect.getfile(em.__class__))
print("PathDir", os.path.dirname(inspect.getfile(Employee)))

# Module relative dir and filename (backup/modules/employee.py)
print("RelativeModulePath", os.path.relpath(inspect.getfile(Employee)))

# Module dir (backup/modules)
print("RelativeModuleDir", os.path.relpath(os.path.dirname(inspect.getfile(Employee))))

# Static
print(Employee.is_date_valid("11-09-2012"))

# F-string format
code = "0123"
print(f"Code 6-digits: {code:>06}")

price = 0.6
print(f"Price: {price:.2f}")

dt = 3
print(f"Day: {dt:>02}")

# Exception
em.throwEx()
