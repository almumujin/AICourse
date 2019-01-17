

s1="hello"
try:
    int(s1)
#多分支处理异常 （按实际需求与万能异常使用）
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)
# except Exception as e: //万能异常处理
#     print(e)
else:
   print("try without exception")#try内无异常时执行
finally:
    print("Done") #有没有异常都会执行 ，通常用于做一些清理工作
print("2222")

#自定义异常类
class EgonException(BaseException):# 需集成BaseExcepion
    def __init__(self,msg):
        self.msg = msg
# raise EgonException("自己定制的异常")

