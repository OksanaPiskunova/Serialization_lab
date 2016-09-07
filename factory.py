# -*- coding: utf-8 -*-
from development_team import *


class Factory:
    def __init__(self):
        self.constructors = {"DominantPerson": DominantPerson,
                             "SystemArchitect": SystemArchitect,
                             "ProjectManager": ProjectManager,
                             "Developer": Developer,
                             "BackendDeveloper": BackendDeveloper,
                             "FrontendDeveloper": FrontendDeveloper,
                             "TestEngineer": TestEngineer,
                             "SystemAdministrator": SystemAdministrator}

    def get_object_by_class_name(self, class_name):
        if class_name in self.constructors.keys():
            return self.constructors[class_name]()
        else:
            return None
