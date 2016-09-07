# -*- coding: utf-8 -*-
import json
import plugins.base as base
from factory import Factory


class JsonSerialization(base.Serialization):
    def __init__(self):
        self.factory = Factory()

    def serialize(self, object_list, filename="../../files/json_serialization.json"):
        file = open(filename, mode="w")
        try:
            object = []
            for employee in object_list:
                employee_dict = employee.__dict__
                employee_dict['type'] = employee.__class__.__name__
                object.append(employee_dict)
            json_object = json.JSONEncoder().encode(object)
            file.write(json_object)
        finally:
            file.close()

    def deserialize(self, filename="../../files/json_serialization.json"):
        file = open(filename, mode="r")
        try:
            json_object = file.readline()
            return json.JSONDecoder(object_hook=self._decode_from_json).decode(json_object)
        finally:
            file.close()

    def _decode_from_json(self, json_object):
        if 'type' in json_object.keys():
            class_name = json_object['type']
            employee = self.factory.get_object_by_class_name(class_name)
            if employee is not None:
                employee = self._set_properties(employee, json_object)
                return employee
            else:
                return None
        else:
            return None

    def _set_properties(self, employee, object_dict):
        try:
            setters = employee.get_setters()
            for key in setters.keys():
                if key in object_dict:
                    value = object_dict[key]
                    setters[key](value)
        except Exception:
            print(Exception)
        finally:
            return employee
