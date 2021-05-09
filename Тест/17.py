class Monster:
    def __init__ (self, name, height, weight):
        self.name = name
        self._height = height
        self.__weight = weight

m = Monster('Chucky', 55,5)
print(m.name, m._height, m.__weight)        