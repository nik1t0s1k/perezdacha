class Product:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price

    def product_description(self):
        print(f"Продукт: {self.name}, Тип: {self.type}, Цена: {self.price}")


product = Product("Телефон", "Электроника", 500)

product.product_description()
