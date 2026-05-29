
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

def ft_garden_security() -> None:
    print('=== Garden Security System ===')
    # rose = Plant('Rose', 25, 30)
    # oak = Plant('Oak', 200, 365)
    # cactus = Plant('Cactus', 5, 90)
    sunflower = Plant('Sunflower', 80, 45)
    fern = Plant('Fern', 15, 120)

    # TEST
    fern.set_age(20)
    fern.set_age(0)
    fern.set_age(-20)
    sunflower.set_height(30.57)
    sunflower.set_height(0.57)
    sunflower.set_height(-30.57)
    print(f'sunflower age {sunflower.get_age()}')
    print(f'sunflower age {sunflower.get_height()}')

def main() -> int:
    ft_garden_security()

if __name__ == "__main__":
    main()
