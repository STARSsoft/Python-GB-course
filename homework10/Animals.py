
"""
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.


Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.

"""

class Animal:
    type_="Empty"
    def __init__(self,name,age):
        self.name=name
        self.__age=age
        self.spec=None
        
        
    def show_info(self):
        return f"{self.name}, {self.__age}, {self.type_} - {self.get_spec()}"
       
    def get_spec(self):
        return self.spec
    
class Fish(Animal):
    def __init__(self, *args, **kwargs):
        self.type_="Рыба"
        super().__init__(*args, **kwargs)
        self.spec=self.swim()

    def swim(self):
        return "плавает"

class Bird(Animal):
    def __init__(self, *args, **kwargs):
        self.type_="Птыц"
        super().__init__(*args, **kwargs)
        self.spec=self.fly()
    def fly(self):
        return "летает"

class Mammal(Animal):
    def __init__(self, *args, **kwargs):
        self.type_="Млекопитающие"
        super().__init__(*args, **kwargs)
        self.spec=self.run()

    def run(self):
        return  "бегает"
    
if __name__=="__main__":
    p1=Bird("Arа",5)
    p2=Mammal("Vasya",8)
    p3=Fish("Chi",2)
    print (p1.show_info())
    print (p2.show_info())
    print (p3.show_info())