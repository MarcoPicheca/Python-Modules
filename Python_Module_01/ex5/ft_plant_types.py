
class Plant:
    _name: str = ''
    _age: int = 0
    _height: float = 0

    # SETTERS
    def set_age(self, age: int) -> None:
        if age < 0:
            return print(f'{self._name}: Error, age can\'t be negative\nAge update rejected\n')
        self._age = age
        print(f'Age updated: {self._age} days')
        print(f'Current state: {self._name}: {self._height}cm, {self._age} days old')
    def set_height(self, height: float) -> None:
        if height < 0:
            return print(f'{self._name}: Error, height can\'t be negative\nHeight update rejected\n')
        self._height = height
        print(f'Height updated: {self._height}cm')
        print(f'Current state: {self._name}: {self._height}cm, {self._age} days old')

    # GETTERS
    def get_age(self) -> int:
        return self._age
    def get_height(self) -> float:
        return self._height
    def get_name(self) -> float:
        return self._name
    
    # METHODS
    def show(self) -> None:
        print(self._name + ':', str(round(self._height, 1)) + 'cm,', str(self._age) + ' days old')
        return
    
    def age(self, days: int) -> None:
        self._age += days
    
    def grow(self, growth: float) -> None:
        self._growth += growth
        self._height += growth
    
    # CONSTRUCTOR
    def __init__(self, name: str, age: int, height: float):
        if age < 0:
            return print(f'{self._name}: Error, age can\'t be negative\nAge update rejected')
        if height < 0:
            return print(f'{self._name}: Error, height can\'t be negative\nHeight update rejected')
        self._name = name
        self._age = age
        self._height = height
        print(f'Plant created: {self._name}: {self._height}cm, {self._age} days old')
    pass

# NB super() method
class Flower(Plant) :
    # colur attr and bloom() method
    _color: str

    def __init__(self, name: str, age: int, height: float, color: str):
        super().__init__(name, age, height)
        self._color = color
        super().show()
        print(' Color:', self._color)

    def bloom(self):
        super().show()
        print(' Color:', self._color)
        print(f'{self._name} is blooming beautifully')
    pass

class Tree(Plant) :
    # trunk_diameter attr produce_shade() method
    pass

class Vegetable(Plant) :
    # harvest attr and nutritional_value attributes
    pass