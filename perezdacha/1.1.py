class Course:
    def __init__(self, name, teacher, number_of_classes):
        self.name = name
        self.teacher = teacher
        self.number_of_classes = number_of_classes


course1 = Course('информационные системы', 'Алексей Александрович', 10)
print(f'Курс: ', course1.name, ',', 'Преподаватель: ', course1.teacher, ',',
      'Количество занятий: ', course1.number_of_classes)
print(course1.name)
