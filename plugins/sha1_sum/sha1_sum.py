# -*- coding: utf-8 -*-
import hashlib
import plugins.base as base


class Sha1Sum(base.CheckSumBase):
    def calculate_sum(self, filename):
        result = None
        file = open(filename, mode='rb')
        try:
            result = hashlib.sha1(file.read()).hexdigest()
        finally:
            file.close()
            return result

    def check_sum(self, filename, curr_sum):
        result = True
        file = open(filename, mode='rb')
        try:
            file_sum = hashlib.sha1(file.readline()).hexdigest()
            print(file_sum)
            if file_sum == curr_sum:
                result = True
            else:
                result = False
        finally:
            file.close()
            return result


if __name__ == '__main__':
    m = Sha1Sum()
    s = m.calculate_sum('../base.py')
    print(s)
    f = m.check_sum('../base.py', s)
    print(f)

