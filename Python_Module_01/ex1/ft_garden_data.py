
class Plant:
    name: str
    age: int
    height: int
    def __init__(self, name: str = None, height: int = None, age: int = None) -> None:
        name = name
        if age and height and age > 0 and height > 0:
            self.name = name
            self.age = age
            self.height = height
        pass
    def show(self) -> None:
        print(self.name + ':', str(self.height) + 'cm,', str(self.age) + ' days old')
        return

def ft_garden_intro() -> None:
    rose = Plant('Rose', 25, 30)
    sunflower = Plant('Sunflower', 80, 45)
    cactus = Plant('Cactus', 15, 120)
    print('=== Garden Plant Registry ===')
    rose.show()
    sunflower.show()
    cactus.show()

def main() -> int:
    ft_garden_intro()

if __name__ == "__main__":
    main()