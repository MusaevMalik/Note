class Address:
     def __init__ (self, street, home_number, city_name):
         self.street = street
         self.home_number = home_number
         self.city_name = city_name


class Client:
     def __init__ (self, name, street, home_number, city_name):
         self.name = name
         self.address = Address(street, home_number, city_name)
     def show_address():
         return f'{self.name}, {self.address.street}, {self.address.home_number}, {self.city_name}'

client = Client('Artur', 'Lenina', 13, 'Karakol')
      client.show_address()