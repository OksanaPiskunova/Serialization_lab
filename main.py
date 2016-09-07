# -*- coding: utf-8 -*-
# main.py

import inspect
import tkinter
import tkinter.ttk
from tkinter.messagebox import *
from tkinter.filedialog import *

import plugins.base as base
import registrator
from controller import Controller
from factory import Factory


class Application(tkinter.Frame):
    def __init__(self, master=None):
        self.controller = Controller()
        self.factory = Factory()
        self._init_constructors()
        tkinter.Frame.__init__(self, master)
        self.create_widgets()
        self.register = registrator.PluginsRegistrator()
        self.register.register_plugins()
        self._search_plugins()
        # display the menu
        root.config(menu=self.menubar)
        self.pack()

    def _search_plugins(self):
        self.plugins_list = []
        serialization = None
        checksum = None
        tarfile = None
        tarfile_adapter = None
        checksum_adapter = None
        hashsum_dict = {}
        modules = self.register.get_modules()
        for module in modules:
            package_info = getattr(self.register.package_obj, module)
            for info in dir(package_info):
                file_info = getattr(package_info, info)
                for element in dir(file_info):
                    class_name = getattr(file_info, element)
                    if inspect.isclass(class_name):
                        pass
                        if issubclass(class_name, base.Serialization):
                            serialization = class_name
                        if issubclass(class_name, base.MainCheckSumBase):
                            checksum = class_name
                        if issubclass(class_name, base.CheckSumBase):
                            hashsum_dict[class_name.__name__] = class_name()
                        if issubclass(class_name, base.TarFileBase):
                            tarfile = class_name
                        if issubclass(class_name, base.AdapterBase):
                            if class_name.__name__ == self.TAR:
                                tarfile_adapter = class_name
                            elif class_name.__name__ == self.SUM:
                                checksum_adapter = class_name
        if serialization:
            self.plugins['serialization'] = serialization()
            self.create_menu_item_serialization()
        if checksum and checksum_adapter:
            self.plugins['checksum'] = checksum_adapter(hashsum_dict)
            self.plugins_list.append(checksum_adapter(hashsum_dict))
            self.create_menu_item_checksum()
        if tarfile and tarfile_adapter:
            tarfile_object = tarfile()
            self.plugins['archive'] = tarfile_adapter(tarfile_object)
            self.plugins_list.append(tarfile_adapter(tarfile_object))
            self.create_menu_item_tarfile()

    def create_widgets(self):
        self.init_menu()
        self.init_tree()
        self._init_btn_add_employee()
        self._init_btn_edit_employee()
        self._init_btn_del_employee()

    def create_menu_item_serialization(self):
        menu = tkinter.Menu(self.menubar, tearoff=0)
        menu.add_command(label="Serialize", command=self.serialize)
        menu.add_command(label="Deserialize", command=self.deserialize)
        self.menubar.add_cascade(label="Serialization", menu=menu)

    def create_menu_item_checksum(self):
        menu = tkinter.Menu(self.menubar, tearoff=0)
        for algorithm in self.plugins['checksum'].get_all_algorithms():
            menu.add_radiobutton(label=algorithm,
                                 command=lambda algorithm=algorithm:
                                 self.plugins['checksum'].set_algorithm(algorithm))
        menu.add_radiobutton(label='None',
                             command=lambda algorithm=None: self.plugins['checksum'].set_algorithm(algorithm))
        self.menubar.add_cascade(label="CheckSum", menu=menu)

    def create_menu_item_tarfile(self):
        menu = tkinter.Menu(self.menubar, tearoff=0)
        algorithm_list = self.plugins['archive'].get_all_algorithms()
        for algorithm in algorithm_list:
            menu.add_radiobutton(label=algorithm,
                                 command=lambda alg=algorithm:
                                 self.plugins['archive'].set_algorithm(alg))
        menu.add_radiobutton(label='None',
                             command=lambda alg=None: self.plugins['archive'].set_algorithm(alg))
        self.menubar.add_cascade(label="Archive", menu=menu)

    def _init_constructors(self):
        self.plugins = {}
        self.TAR = 'TarFileAdapter'
        self.SUM = 'CheckSumAdapter'

    def init_menu(self):
        self.menubar = tkinter.Menu(root)
        menu = tkinter.Menu(self.menubar, tearoff=0)
        menu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=menu)

    def init_tree(self):
        self.tree = tkinter.ttk.Treeview(self)
        self.tree.insert("", 1, "DominantPerson", text="Dominant Person")
        self.tree.insert("DominantPerson", 1, "SystemArchitect", text="System Architect")
        self.tree.insert("DominantPerson", 0, "ProjectManager", text="Project Manager")
        self.tree.insert("", 0, "Developer",  text="Developer")
        self.tree.insert("Developer", 0, "BackendDeveloper", text="Back-end Developer")
        self.tree.insert("Developer", 1, "FrontendDeveloper", text="Front-end Developer")
        self.tree.insert("", 2, "TestEngineer", text="Test Engineer")
        self.tree.insert("", 3, "SystemAdministrator", text="System Administrator")
        for employee in self.controller.list_of_employees:
            self.tree.insert(employee.__class__.__name__, 0, 0,
                             text=(employee.name + " " + employee.surname))
        self.tree.pack(side="bottom")

    def _get_chosen_tree_element(self):
        return self.tree.focus()

    def _init_btn_add_employee(self):
        self.btn_add_employee = tkinter.Button(self, width=20)
        self.btn_add_employee["text"] = "Add employee"
        self.btn_add_employee["command"] = self.add_employee
        self.btn_add_employee.pack()

    def _init_btn_edit_employee(self):
        self.btn_edit_employee = tkinter.Button(self, width=20)
        self.btn_edit_employee["text"] = "Edit employee"
        self.btn_edit_employee["command"] = self.edit_employee
        self.btn_edit_employee.pack()

    def _init_btn_del_employee(self):
        self.btn_del_employee = tkinter.Button(self, width=20)
        self.btn_del_employee["text"] = "Delete employee"
        self.btn_del_employee["command"] = self.delete_employee
        self.btn_del_employee.pack()

    def _init_btn_serialize(self):
        self.btn_serialize = tkinter.Button(self, width=20)
        self.btn_serialize["text"] = "Serialize"
        self.btn_serialize["command"] = self.serialize
        self.btn_serialize.pack()

    def _init_btn_deserialize(self):
        self.btn_deserialize = tkinter.Button(self, width=20)
        self.btn_deserialize["text"] = "Deserialize"
        self.btn_deserialize["command"] = self.deserialize
        self.btn_deserialize.pack()

    def add_employee(self):
        chosen_element = self._get_chosen_tree_element()
        try:
            employee = self.factory.get_object_by_class_name(chosen_element)
            if employee is not None:
                self.controller.add_employee(employee)
                self.tree.destroy()
                EditWindow(employee, self)
            else:
                showinfo("Add", "Choose the class")
        except Exception:
            showinfo("Add", "Choose the class")

    def edit_employee(self):
        chosen_element = self._get_chosen_tree_element()
        try:
            employee_number = int(chosen_element[1:], 16)
            employee = self.controller.list_of_employees[employee_number - 1]
            self.tree.destroy()
            EditWindow(employee, self)
        except Exception:
            showinfo("Edit", "Choose the employee")

    def delete_employee(self):
        chosen_element = self._get_chosen_tree_element()
        try:
            employee_number = int(chosen_element[1:], 16)
            employee = self.controller.list_of_employees[employee_number - 1]
            self.controller.delete_employee(employee)
            self.tree.destroy()
            self.init_tree()
        except Exception:
            showerror("Delete", "Employee not found")

    def serialize(self):
        try:
            sa = asksaveasfilename()
            self.plugins['serialization'].serialize(self.controller.list_of_employees, sa)
            key_list = list(self.plugins.keys())
            key_list.sort(reverse=True)
            print(key_list)
            for key in key_list:
                if key != 'serialization' and self.plugins[key].get_algorithm() is not None:
                    self.plugins[key].pre_process(sa)
        except Exception:
            showwarning("Serialize", "Can't serialize")
        finally:
            self.tree.destroy()
            self.init_tree()

    def deserialize(self):
        try:
            res = False
            op = askopenfilename()
            key_list = list(self.plugins.keys())
            key_list.sort(reverse=False)
            print(key_list)
            for key in key_list:
                if key != 'serialization' and self.plugins[key].get_algorithm() is not None:
                    print(key)
                    res = self.plugins[key].post_process(op)
                else:
                    res = True

            if res is True:
                list_of_employees = \
                    self.plugins['serialization'].deserialize(op)
                for employee in list_of_employees:
                    self.controller.add_employee(employee)
            else:
               showwarning("Deserialize", "Can't deserialize")
        except Exception:
            showwarning("Deserialize", "Can't deserialize")
        finally:
            self.tree.destroy()
            self.init_tree()


class EditWindow:
    def __init__(self, employee, parent=None):
        self.employee = employee
        self.parent = parent
        self.slave = tkinter.Toplevel(parent)
        self.slave.title("Edit")
        self.slave.protocol('WM_DELETE_WINDOW', self.close)
        #self.slave.geometry('200x150+400+300')
        self._init_variables()
        self.create_widgets()
        self.slave.mainloop()

    def _init_variables(self):
        self._init_dictionaries()
        self.properties_list = []

    def _init_dictionaries(self):
        self._init_label_text()

    def _init_label_text(self):
        self.label_text = {'_name': "Name",
                           '_surname': "Surname",
                           '_age': "Age",
                           '_salary': "Salary",
                           '_experience': "Experience",
                           '_used_technologies': "Used Technologies",
                           '_some_property': "Some Property",
                           '_current_projects_number': "Number of current projects",
                           '_methodology': "Methodology",
                           '_rank': "Rank",
                           '_subordinates_number': "Number of subordinates",
                           '_used_behavior_model': "Used BehaviorModel",
                           '_used_database': "Database",
                           '_specialization': "Specialization"
                           }

    def create_widgets(self):
        self.input_fields = []
        employee_dict = self.employee.__dict__
        for key in employee_dict.keys():
            self.properties_list.append(key)
            if key in self.label_text:
                self._init_label(self.label_text[key])
            else:
                self._init_label("Unknown param")
            self._init_entry(employee_dict[key])
        self._init_btn_ok()

    def _init_label(self, text=""):
        label = tkinter.Label(self.slave, text=text)
        label.pack()

    def _init_entry(self, text=""):
        entry = tkinter.Entry(self.slave, width=20, bd=2)
        entry.insert(0, text)
        entry.pack()
        self.input_fields.append(entry)

    def _init_btn_ok(self):
        self.btn_ok = tkinter.Button(self.slave, text="OK", width=16)
        self.btn_ok["command"] = self._change_properties
        self.btn_ok.pack()

    def _change_properties(self):
        property_dict = {}
        for i in range(len(self.properties_list)):
            property_dict[self.properties_list[i]] = \
                self.input_fields[i].get()
            self.parent.controller.set_properties(self.employee, property_dict)
        self.close()

    def close(self):
        self.parent.init_tree()
        self.slave.destroy()


if __name__ == "__main__":
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()
