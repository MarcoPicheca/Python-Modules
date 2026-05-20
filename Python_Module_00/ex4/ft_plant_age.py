def ft_plant_age() -> None:
    print('Enter plant age in days: ', end='')
    plant_age: int = int(input().strip().replace(" ", ""))
    if plant_age.is_integer() == False :
        print(f'This "{plant_age}" is not a valid age')
        exit(1)
    if plant_age > 60:
        print('Plant is ready to harvest!')
    else :
        print('Plant needs more time to grow.')


# def main():
#     ft_plant_age()

# main()