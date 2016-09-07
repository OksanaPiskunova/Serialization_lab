# -*- coding: utf-8 -*-
import tarfile
import plugins.base as base


class TarFile(base.TarFileBase):
    def make_archive(self, filename, algorithm='gz'):
        archive_name = filename + '.tar.' + algorithm
        file_mode = 'w:' + algorithm
        file = tarfile.open(archive_name, mode=file_mode)
        try:
            filename_start = filename.rfind('/') + 1
            file.add(name=filename, arcname=filename[filename_start :])
        finally:
            file.close()

    def extract(self, filename):
        file = tarfile.open(filename)
        try:
            dir_name_end = filename.rfind('/') + 1
            file.extractall(path=filename[: dir_name_end])
        finally:
            file.close()


if __name__ == '__main__':
    tar = TarFile()
    #tar.make_archive('../../files/ser.json')
    tar.extract('/home/oksana/PycharmProjects/oop3/files/ser.json.tar.gz')

