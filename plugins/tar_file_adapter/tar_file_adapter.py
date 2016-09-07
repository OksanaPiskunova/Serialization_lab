# -*- coding: utf-8 -*-
import plugins.base as base


class TarFileAdapter(base.AdapterBase):
    def __init__(self, tarfile_object):
        self.archiver = tarfile_object
        self._algorithms = ['gz', 'bz2']
        self._algorithm = None

    def get_all_algorithms(self):
        return self._algorithms

    def set_algorithm(self, algorithm):
        self._algorithm = algorithm
        print(algorithm)

    def get_algorithm(self):
        return self._algorithm

    algorithm = property(fset=set_algorithm,
                         fget=get_algorithm)

    def pre_process(self, filename):
        self.archiver.make_archive(filename, self._algorithm)

    def post_process(self, filename):
        archive_name = filename + '.tar.' + self._algorithm
        self.archiver.extract(archive_name)

