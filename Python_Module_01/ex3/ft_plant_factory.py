
class Plant:
    plant_name: str
    plant_age: int
    plant_height: float
    plant_growth: float = 0

    # age method
    def age(self, days: int) -> None:
        self.plant_age += days
    
    # grow method
    def grow(self, growth: float) -> None:
        self.plant_growth += growth
        self.plant_height += growth

    # show method
    # def show(self, growth) -> None:
    #     print(self.plant_name + ':', str(round(self.plant_height, 1)) + 'cm,', str(self.plant_age) + ' days old')
    #     days: range = range(1, 8)
    #     for day in days:
    #         self.age(1)
    #         self.grow(growth)
    #         print(f'=== Day {day} ===')
    #         print(self.plant_name + ':', str(round(self.plant_height, 1)) + 'cm,', str(self.plant_age) + ' days old')
        
    #     print(f'Growth this week: {self.plant_growth}')
    #     return
    def show(self) -> None:
        print('Created:', self.plant_name + ':', str(round(self.plant_height, 1)) + 'cm,', str(self.plant_age) + ' days old')
        return
    
    # istanza dell'oggetto
    # l'interprete ricerca prima nell'istanza e poi i metodi, quindi i nomi delle
    # cose (membri, variabili, attributi ecc ...) in un oggetto di python seguono questo 
    # principio di precedenza
    def __init__(self, name: str = None, height: float = None, age: int = None) -> None:
        if name and age and height and age > 0 and height > 0:
            self.plant_name = name
            self.plant_age = int(age)
            self.plant_height = float(height)
        self.show()
        pass

def ft_garden_intro() -> None:
    print('=== Plant Factory Output ===')
    rose = Plant('Rose', 25, 30)
    Oak = Plant('Oak', 200, 365)
    cactus = Plant('Cactus', 5, 90)
    sunflower = Plant('Sunflower', 80, 45)
    Fern = Plant('Fern', 15, 120)

def main() -> int:
    ft_garden_intro()

if __name__ == "__main__":
    main()
