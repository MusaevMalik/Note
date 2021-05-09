
#  Миксины — это особый вид наследования в Python (и других объектно-ориентированных языках),
# и он начинает набирать популярность в разработке Django / веб-приложений.
# Вы можете использовать Mixin, чтобы позволить классам в Python совместно использовать
# методы между любым классом, который наследуется от этого Mixin.

# Пример:

class GraphicalEntity:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y


class ResizableMixin:
    def resize(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y


class ResizableGraphicalEntity(GraphicalEntity, ResizableMixin):
    pass