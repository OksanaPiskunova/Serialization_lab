# -*- coding: utf-8 -*-


class Serialization:
    def serialize(self, object_list, filename):
        pass

    def deserialize(self, filename):
        pass


class CheckSumBase:
    def calculate_sum(self, filename):
        pass

    def check_sum(self, filename, curr_sum):
        pass


class MainCheckSumBase:
    def get_hash_dictionary(self):
        pass

    def calculate_sum(self, filename):
        pass

    def check_sum(self, filename):
        pass

    def _read_sum_from_file(self, filename):
        pass

    def _write_sum_to_file(self, filename, curr_sum):
        pass


class TarFileBase:
    def _init__(self):
        pass

    def make_archive(self, filename):
        pass

    def extract(self, filename):
        pass


class AdapterBase:
    def set_algorithm(self, algorithm):
        pass

    def get_algorithm(self):
        pass

    def get_all_algorithms(self):
        pass

    def pre_process(self, filename):
        pass

    def post_process(self, filename):
        pass
