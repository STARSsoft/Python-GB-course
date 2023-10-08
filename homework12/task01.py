'''
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. 
Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета
 и по оценкам всех предметов вместе взятых.

Вам предоставлен файл subjects.csv, содержащий предметы.
 Сейчас в файл записана следующая информация.

Математика,Физика,История,Литература

Создайте класс Student, который будет представлять студента и его успехи по предметам. 
Класс должен иметь следующие методы:

__init__(self, name, subjects_file): конструктор класса, принимающий ФИО студента
 и имя файла с данными о предметах и оценках.

add_subject(self, subject, grade, test_score): метод для добавления информации о предмете,
 оценке и результате теста.

get_average_grade(self): метод, возвращающий средний балл студента по всем предметам.

get_subjects(self): метод, возвращающий список всех предметов, 
по которым есть информация у студента.

Реализовать функцию get_average_grades(students), 
которая принимает список студентов и выводит информацию о средних баллах для каждого студента.

Реализовать функцию get_subject_average(students, subject), 
которая принимает список студентов и название предмета, 
и выводит информацию о среднем балле по этому предмету для каждого студента.

Реализовать функцию get_top_student(students, subject),
которая принимает список студентов и название предмета, 
и выводит информацию о студенте с наивысшим средним баллом по этому предмету.

Пример
На входе:

student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
На выходе:

Средний балл: 4.5
Средний результат по тестам по математике: 85.0
Студент: Иван Иванов
Предметы: Математика, История

'''

import csv

class Name_:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.__validate(value)
        setattr(instance, self.param_name, value)

    @staticmethod
    def __validate(value):
        if not isinstance(value, str):
            raise TypeError(
                'ФИО должно состоять только из букв и начинаться с заглавной буквы')
        for char in value:
            if not char.isalpha() and not char.isspace():
                raise ValueError(
                    'ФИО должно состоять только из букв и начинаться с заглавной буквы')
        if not value.istitle():
            raise ValueError(
                'ФИО должно состоять только из букв и начинаться с заглавной буквы')


class Range_:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(
                f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(
                f'Значение {value} должно быть меньше {self.max_value}')


class Student:
    _grade = Range_(2, 5)
    _test_score = Range_(0, 100)
    _name = Name_()
    _subject = dict()

    def __init__(self, name, subject_file):
        '''конструктор класса, принимающий ФИО студента и имя файла с данными о предметах и оценках.
        '''
        self._name = name
        self.subject_file = subject_file

        with open(self.subject_file, 'r', encoding="UTF-8") as file:
            lines = csv.reader(file, dialect='excel')
            for line in lines:
                for item in line:
                    self._subject[item] = {'grade': [], 'test_score': []}

    def add_subject(self, subject, grade, test_score):
        """метод для добавления информации о предмете, оценке и результате теста.
        """
        if subject in self._subject:
            self._subject[subject]["grade"].append(grade)
            self._subject[subject]["test_score"].append(test_score)

    def get_average_grade(self):
        """метод, возвращающий средний балл студента по всем предметам.
        """

        total_sum = 0
        count = 0

        for item in self._subject.values():
            total_sum += sum(item['grade'])
            count += len(item['grade'])

        return total_sum / count if count != 0 else 0

    def get_subjects(self):
        """метод, возвращающий список всех предметов, по которым есть информация у студента.
        """
        text = []
        for key in self._subject.keys():
            if len(self._subject[key]['grade']) > 0 or len(self._subject[key]['test_score']):
                text.append(key)
        return f'Предметы: {", ".join(text)}'

    def add_grade(self, subject, grade):
        if subject in self._subject.keys():
            self._subject[subject]["grade"].append(grade)

    def add_test_score(self, subject, test_score):
        if subject in self._subject.keys():
            self._subject[subject]["test_score"].append(test_score)

    def get_average_test_score(self, subject):
        total_sum = 0
        count = 0 
        if subject in self._subject:
            total_sum += sum(self._subject[subject]['test_score'])
            count += len(self._subject[subject]['test_score'])
        return total_sum / count if count != 0 else 0
    
    def get_subject(self):
        text = []
        for key in self._subject.keys():
            if len(self._subject[key]['grade']) > 0 or len(self._subject[key]['test_score']):
                text.append(key)
        return f'Предметы: {", ".join(text)}'
    
    def __str__(self):
        return f'Студент: {self._name}\n{self.get_subject()}'



def get_average_grades(students):
    """принимает список студентов и выводит информацию о средних баллах для каждого студента. """
    for st in students:
        print(st.get_average_grade())


def get_subject_average(students,subject ):
    """принимает список студентов и название предмета, и выводит информацию о среднем балле по этому предмету для каждого студента.
    """
    for st in students:
        print(st.get_average_test_score(subject))
    

def get_top_student(students, subject):
    """принимает список студентов и название предмета, и выводит информацию о студенте с наивысшим средним баллом по этому предмету.
    """
    pass

if __name__=="__main__":
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)
