# Вопрос №6

# Под инкапсуляцией понимается сокрытие деталей реализации, данных и т.п. от внешней стороны.
# Например, можно определить класс “холодильник”, который будет содержать следующие данные: 
# производитель, объем, количество камер хранения, потребляемая мощность и т.п., и методы:
# открыть/закрыть холодильник, включить/выключить, но при этом реализация того,
# как происходит непосредственно включение и выключение пользователю вашего класса не доступна, 
# что позволяет ее менять без опасения, что это может отразиться на использующей класс «холодильник» программе.
# При этом класс становится новым типом данных в рамках разрабатываемой программы. 
# Можно создавать переменные этого нового типа, такие переменные называются объекты.

# Модификаторы доступа в Python используются для модификации области видимости переменных по умолчанию. 
# Есть три типа модификаторов доступов в Python ООП:

# №1 публичный — public;
# №2 приватный — private;
# №3 защищенный — protected.

# Пример:

class Phone:
    username = "Kate"                # public variable
    __how_many_times_turned_on = 0   # private variable

    def call(self):                  # public method
        print( "Ring-ring!" )

    def __turn_on(self):             # private method
        self.__how_many_times_turned_on += 1 
        print( "Times was turned on: ", self.__how_many_times_turned_on )

my_phone = Phone()

my_phone.call()
print( "The username is ", my_phone.username )
# my_phone.turn_on()
# my_phone.__turn_on()
# print( “Turned on: “, my_phone.__how_many_times_turned_on)
# print( “Turned on: “, my_phone.how_many_times_turned_on)
# will produce an error
input( "Press Enter to exit" )