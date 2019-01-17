import pickle
import hashlib
from uu import encode


def create_md5():
    m=hashlib.md5()
    m.updae('abc',encode('utf-8'))
    return m.hexdidest()


class Base:
    def save(self):
        with open('school.db', 'wb') as f:
            pickle.dump(self, f)  # dump产生字节形式，w为写字符串，wb为写二进制


class School(Base):
    def __init__(self, id, name, addr):
        self.id = create_md5()
        self.name=name
        self.addr=addr


class Course(Base):
    def __init__(self, name, price, period, school):
        self.name = name
        self.price = price
        self.period = period
        self.school = school

# school_obj = pickle.load(open('school.db','rb')) load出保存在文件中的字节对象
# s1=School('oldboy','北京')
# s1.save()