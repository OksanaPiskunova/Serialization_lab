# -*- coding: utf-8 -*-
import hashlib
import plugins.base as base


class Md5Sum(base.CheckSumBase):
    def calculate_sum(self, filename):
        result = None
        file = open(filename, mode='rb')
        try:
            result = hashlib.md5(file.read()).hexdigest()
            print(result)
        finally:
            file.close()
            return result

    def check_sum(self, filename, curr_sum):
        result = None
        file = open(filename, mode='rb')
        try:
            file_sum = hashlib.md5(file.readline()).hexdigest()
            print(file_sum)
            if file_sum == curr_sum:
                result = True
            else:
                result = False
        finally:
            file.close()
            return result


if __name__ == '__main__':
    m = Md5Sum()
    s = m.calculate_sum('../base.py')
    print(s)
    f = m.check_sum('../base.py', s)
    print(f)

