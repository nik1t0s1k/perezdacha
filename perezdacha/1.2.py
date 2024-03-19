class Software:
    def __init__(self, name, developer, version):
        self.name = name
        self.developer = developer
        self.version = version

    def description_program(self):
        print(f"Программа: {self.name}, Разработчик: {self.developer}, Версия : {self.version}")


program = Software("Математика", "Иванов", 2)

print(program.description_program())
