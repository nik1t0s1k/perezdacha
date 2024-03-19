class Furniture:
    def __init__(self, name, material, price):
        self.name = name
        self.material = material
        self.price = price

    def description(self):
        print(f'Мебель: {self.name}, Материал: {self.material}, Цена: {self.price}')


furniture = Furniture("Стул", "Дерево", 100)

furniture.description()