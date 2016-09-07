# -*- coding: utf-8 -*-
import plugins.base as base


class CheckSum(base.MainCheckSumBase):
    def __init__(self, algorithms):
        self._algorithms = algorithms        # dictionary {algorithm: object}
        self._algorithm = None

    def get_hash_dictionary(self):
        return self._algorithms

    def calculate_sum(self, filename):
        print(self._algorithm)
        print(self._algorithms)
        curr_sum = self._algorithms[self._algorithm].calculate_sum(filename)
        if curr_sum is not None:
            sum_filename = filename
            print(curr_sum)
            self._write_sum_to_file(sum_filename,  str(curr_sum))

    def check_sum(self, filename):
        result = None
        try:
            sum_filename = filename #+ '.' + self._algorithm.lower()
            curr_sum = self._read_sum_from_file(sum_filename)
            if curr_sum is not None:
                result = self._algorithms[self._algorithm].check_sum(filename, curr_sum)
        finally:
            return result

    def _read_sum_from_file(self, filename):
        result = None
        file = open(filename, mode='r')
        try:
            file.readline()
            result = file.readline()
        finally:
            file.close()
            return result

    def _write_sum_to_file(self, filename, curr_sum):
        filename = filename #+ '.' + self._algorithm.lower()
        file = open(filename, mode='a')
        try:
            file.write('\n' + str(curr_sum))
        finally:
            file.close()


class CheckSumAdapter(base.AdapterBase):
    def __init__(self, algorithms):
        self.checksum = CheckSum(algorithms)
        self._algorithm = None

    def set_algorithm(self, algorithm):
        self._algorithm = algorithm
        self.checksum._algorithm = algorithm
        print(algorithm)

    def get_algorithm(self):
        return self._algorithm

    algorithm = property(fset=set_algorithm,
                         fget=get_algorithm)

    def pre_process(self, filename):
        self.checksum.calculate_sum(filename)

    def post_process(self, filename):
        return self.checksum.check_sum(filename)

    def get_all_algorithms(self):
        return self.checksum.get_hash_dictionary()
