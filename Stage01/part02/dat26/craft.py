class Foo:
    def __init__(self,name):
        self.name = name
        
    def __getattr__(self, item):
        print('你找的属性【%s】不存在' %item)
        
    def __setattr__(self, key, value):
        print('执行setattr', key, value)
        if type(value) is str:
            print('开始设置')
            # self.key=value  # 触发__setattr_
            self.__dict__[key] = value
        else:
            print('必须是字符串类型')

f1=Foo('alex')
print(f1.name)
print(f1.age)