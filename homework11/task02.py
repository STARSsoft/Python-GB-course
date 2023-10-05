'''
Разработайте программу для хранения и управления текстовыми и числовыми записями.
Вам нужно создать класс Archive, который будет представлять архив и реализовывать следующую функциональность:

Класс Archive должен иметь следующие атрибуты:

archive_text (list): Список архивированных текстовых записей.
archive_number (list): Список архивированных числовых записей.
text (str): Текущая текстовая запись, которую нужно добавить в архив.
number (int или float): Текущая числовая запись, которую нужно добавить в архив.
Класс Archive должен реализовать шаблон Singleton, чтобы гарантировать, что существует только один экземпляр архива.

Класс Archive должен иметь метод __init__(self, text: str, number: int | float), который принимает текстовую и числовую запись и сохраняет их как текущие записи для добавления в архив.

Класс Archive должен реализовать методы
__str__(self) и __repr__(self), чтобы можно было получить строковое представление текущих записей и архива.

Пример

На входе:

archive1 = Archive("Запись 1", 42)
archive2 = Archive("Запись 2", 3.14)
На выходе:

Text is Запись 1 and number is 42. Also ['Запись 1'] and [42]
Text is Запись 2 and number is 3.14. Also ['Запись 1', 'Запись 2'] and [42, 3.14]
'''

class Archive:
    instanse=None
    archive_text=[]
    archive_number=[]

    text=None
    number=None

    def __new__(cls,*args,**kwargs ):
        if cls.instanse is None:
            cls.instanse=super().__new__(cls)
        return cls.instanse
    
    def __init__(self, text: str, number ):

        if self.text: self.archive_text.append(self.text)
        if self.number: self.archive_number.append(self.number)
        
        self.text=text
        self.number=number
        

    def __str__(self):
        str_=""
        str_=f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"
        return str_
    
    def __repr__(self) -> str:
        str_=f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"
        return str_

if __name__=="__main__":
    archive1 = Archive("Запись 1", 42)
    print(archive1)
    archive2 = Archive("Запись 2", 3.14)
    print(archive2)

