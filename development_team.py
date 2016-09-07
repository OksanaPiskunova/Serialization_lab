# development_team.py


class MemberOfTeam:
    def __init__(self):
        self._name = "Name"
        self._surname = "Surname"
        self._age = 20
        self._experience = 0
        self._salary = 50

    def get_setters(self):
        return {'_name': self.set_name,
                '_surname': self.set_surname,
                '_age': self.set_age,
                '_experience': self.set_experience,
                '_salary': self.set_salary}

    # property 'name'
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    name = property(fget=get_name, fset=set_name,
                    doc="Name")

    # property 'surname'
    def get_surname(self):
        return self._surname

    def set_surname(self, value):
        self._surname = value

    surname = property(fget=get_surname, fset=set_surname,
                       doc="Surname")

    # property 'age'
    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value

    age = property(fget=get_age, fset=set_age,
                   doc="Age")

    # property 'experience'
    def get_experience(self):
        return self._experience

    def set_experience(self, value):
        self._experience = value

    experience = property(fget=get_experience,
                          fset=set_experience,
                          doc="Experience")

    # property 'salary'
    def get_salary(self):
        return self._salary

    def set_salary(self, value):
        self._salary = value

    salary = property(fget=get_salary, fset=set_salary,
                      doc="Salary")


class DominantPerson(MemberOfTeam):
    def __init__(self):
        MemberOfTeam.__init__(self)
        self._current_projects_number = 1

    def get_setters(self):
        property_dict = MemberOfTeam.get_setters(self)
        property_dict['_current_projects_number'] = self.set_current_projects_number
        return property_dict

    # property 'current_projects_number'
    def get_current_projects_number(self):
        return self._current_projects_number

    def set_current_projects_number(self, value):
        self._current_projects_number = value

    current_projects_number = property(fget=get_current_projects_number,
                                       fset=set_current_projects_number,
                                       doc="Number of current projects")


class SystemArchitect(DominantPerson):
    def __init__(self):
        DominantPerson.__init__(self)
        self._methodology = ""

    def get_setters(self):
        property_dict = MemberOfTeam.get_setters(self)
        property_dict['_methodology'] = self.set_methodology
        return property_dict

    # property 'current_projects_number'
    def get_methodology(self):
        return self._methodology

    def set_methodology(self, value):
        self._methodology = value

    methodology = property(fget=get_methodology, fset=set_methodology,
                           doc="Methodology")


class ProjectManager(DominantPerson):
    def __init__(self):
        DominantPerson.__init__(self)
        self._subordinates_number = 2

    def get_setters(self):
        property_dict = MemberOfTeam.get_setters(self)
        property_dict['_subordinates_number'] = self.set_subordinates_number
        return property_dict

    # property 'subordinates_number'
    def get_subordinates_number(self):
        return self._subordinates_number

    def set_subordinates_number(self, value):
        self._subordinates_number = value

    subordinates_number = property(fget=get_subordinates_number,
                                   fset=set_subordinates_number,
                                   doc="Number of subordinates")


class Developer(MemberOfTeam):
    def __init__(self):
        MemberOfTeam.__init__(self)
        self._used_technologies = ""
        self._rank = "Junior"

    def get_setters(self):
        property_dict = MemberOfTeam.get_setters(self)
        property_dict['_used_technologies'] = self.set_used_technologies
        property_dict['_rank'] = 'set_rank'
        return property_dict

    # property 'rank'
    def get_used_technologies(self):
        return self._used_technologies

    def set_used_technologies(self, value):
        self._used_technologies = value

    used_technologies = property(fget=get_used_technologies,
                                 fset=set_used_technologies,
                                 doc="Used technologies")

    # property 'rank'
    def get_rank(self):
        return self._rank

    def set_rank(self, value):
        self._rank = value

    rank = property(fget=get_rank, fset=set_rank, doc="Rank")


class BackendDeveloper(Developer):
    def __init__(self):
        Developer.__init__(self)
        self._used_database = ""

    def get_setters(self):
        property_dict = MemberOfTeam.get_setters(self)
        property_dict['_used_database'] = self.set_used_database
        return property_dict

    def get_used_database(self):
        return self._used_database

    def set_used_database(self, value):
        self._used_database = value

    used_database = property(fget=get_used_database,
                             fset=set_used_database,
                             doc="Database")


class FrontendDeveloper(Developer):
    def __init__(self):
        Developer.__init__(self)
        self._specialization = ""

    def get_setters(self):
        property_dict = MemberOfTeam.get_setters(self)
        property_dict['_specialization'] = self.set_specialization
        return property_dict

    def get_specialization(self):
        return self._specialization

    def set_specialization(self, value):
        self._specialization = value

    specialization = property(fget=get_specialization,
                              fset=set_specialization,
                              doc="Specialization")


class TestEngineer(MemberOfTeam):
    def __init__(self):
        MemberOfTeam.__init__(self)
        self._used_behavior_model = ""

    def get_setters(self):
        property_dict = MemberOfTeam.get_setters(self)
        property_dict['_used_behavior_model'] = self.set_used_behavior_model
        return property_dict

    def get_used_behavior_model(self):
        return self._used_behavior_model

    def set_used_behavior_model(self, value):
        self._used_behavior_model = value

    used_behavior_model = property(fget=get_used_behavior_model,
                                   fset=set_used_behavior_model,
                                   doc="Used behavior model")


class SystemAdministrator(MemberOfTeam):
    def __init__(self):
        MemberOfTeam.__init__(self)
        self._specialization = ""

    def get_setters(self):
        property_dict = MemberOfTeam.get_setters(self)
        property_dict['_specialization'] = self.set_specialization
        return property_dict

    def get_specialization(self):
        return self._specialization

    def set_specialization(self, value):
        self._specialization = value

    specialization = property(fget=get_specialization,
                              fset=set_specialization,
                              doc="Specialization")
