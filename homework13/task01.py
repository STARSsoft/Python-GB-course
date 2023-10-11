'''
Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError,
 которое выбрасывается при некорректных значениях ширины и высоты, как при создании объекта, так и при установке их через сеттеры.
'''
class NegativeValueError(Exception):
    def __init__(self, par,val):
        self.par_ = par
        self.val = val

    def __str__(self):

        return f"{self.par_} должна быть положительной, а не {self.val}"

class Rectangle:
    def __init__(self, width, height=None) -> None:

        if width<0:
            raise NegativeValueError("Ширина",width)
        if height<0:
            raise NegativeValueError("Высота",height)
        else:
            self._width = width
            self._height = height if height else width

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height

    @width.setter
    def width(self,value):
        if value<0 :
          raise NegativeValueError("Ширина",value)
        else:self._width=value

    @height.setter
    def height(self,value):
        if value<0 :
          raise NegativeValueError("Высота",value)
        else:self._height=value

    def area(self):
        return int(self._width*self._height)

    def perimeter(self):
        return int(2*(self._width+self._height))


    def __str__(self):
        """метод для получения строкового представления прямоугольника. Возвращает строку с информацией о ширине и высоте прямоугольника."""
        return f"Прямоугольник со сторонами {self._width} и {self._height}"
    
    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"
    

if __name__=="__main__":
    r = Rectangle(5, -3)