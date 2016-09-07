# -*- coding: utf-8 -*-
# controller.py
import development_team


class Controller:
    def __init__(self):
        self._list_of_employees = []
        '''self.constructors = {"DominantPerson": development_team.DominantPerson,
                             "SystemArchitect": development_team.SystemArchitect,
                             "ProjectManager": development_team.ProjectManager,
                             "Developer": development_team.Developer,
                             "BackendDeveloper": development_team.BackendDeveloper,
                             "FrontendDeveloper": development_team.FrontendDeveloper,
                             "TestEngineer": development_team.TestEngineer,
                             "SystemAdministrator": development_team.SystemAdministrator}'''

    @property
    def list_of_employees(self):
        return self._list_of_employees

    def get_last_employee(self):
        employee_count = len(self._list_of_employees)
        return self._list_of_employees[employee_count - 1]

    def add_employee(self, employee):
        self._list_of_employees.append(employee)

    def delete_employee(self, employee):
        self._list_of_employees.remove(employee)

    def set_properties(self, employee, object_dict):
        setters = employee.get_setters()
        for key in setters.keys():
            if key in object_dict:
                setters[key](str(object_dict[key]))

