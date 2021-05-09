
#  Миксины — это особый вид наследования в Python (и других объектно-ориентированных языках),
# и он начинает набирать популярность в разработке Django / веб-приложений.
# Вы можете использовать Mixin, чтобы позволить классам в Python совместно использовать
# методы между любым классом, который наследуется от этого Mixin.

# Пример:

  
class BaseClass(object):
        def test(self):
                return 'BaseClass'
 
class Mixin1(object):
        def test(self):
                return 'Mixin1'
 
class Mixin2(object):
        def test(self):
                return 'Mixin2'
 
class MyClass1(BaseClass, Mixin1, Mixin2):
        pass
 
class MyClass2(Mixin2, Mixin1, BaseClass):
        pass
 
print(MyClass1().test())
print(MyClass2().test()) 