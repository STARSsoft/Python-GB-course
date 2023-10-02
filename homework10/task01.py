'''
Доработаем задания 5-6. Создайте класс-фабрику.
- Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
- Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

'''

import random

from Animals import Animal, Bird, Fish, Mammal

class Factory:
    count=0
    list_=[]
    def create_(self, type_, name_, age):

        if type_ == "Bird":
            p1= Bird(name_, age)
        if type_ == "Fish":
            p1= Fish(name_, age)
        if type_ == "Mammal":
            p1= Mammal(name_, age)
        self.list_.append(p1)
        self.count+=1
    
    def get_list_(self):
        str_=""
        for item in self.list_:
            str_=str_+f"{item.show_info()}\n"
        return str_
    
    def get_animal(self,numb):
          return self.list_[numb]


if __name__=="__main__":
    vars_=["Bird","Fish","Mammal"]
    names_=["Ara","Boo","Vasya","Rey","Sonya","Tayson","Casper","Koko"]
    Fac=Factory()

    for _ in range(10):
        type_=random.choice(vars_)
        name_=random.choice(names_)
        Fac.create_(type_,name_,random.randint(1,8))
    print(Fac.get_list_())
    some_animal:Animal=Fac.get_animal(2)
    print(some_animal.show_info())
