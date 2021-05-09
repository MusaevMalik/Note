#Вопрос №12 

# Метакласс - это класс, который создаёт другие классы.
# В сущности, метапрограммирование создаёт или модифицирует код во время выполнения программы,
# а не во время её написания. Python предоставляет возможность управлять данным процессом,
# разрешая написать собственный метакласс для выполнения этой работы.

# Пример:

# описание метакласса
class myobject(type):
    # небольшое вмешательство в момент выделения памяти для класса
    def __new__(cls, name, bases, dict):
        print "NEW", cls.__name__, name, bases, dict
        return type.__new__(cls, name, bases, dict)
    # небольшое вмешательство в момент инициализации класса
    def __init__(cls, name, bases, dict):
        print "INIT", cls.__name__, name, bases, dict
        return super(myobject, cls).__init__(name, bases, dict)
# порождение класса на основе метакласса (заменяет оператор class)
MyObject = myobject("MyObject", (), {})
# обычное наследование другого класса из только что порожденного
class MySubObject(MyObject):
    def __init__(self, param):
        print param
# получение экземпляра класса
myobj = MySubObject("parameter")