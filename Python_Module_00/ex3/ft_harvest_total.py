def ft_harvest_total() -> None:
    print('Day 1 harvest: ', end='')
    day_1: int = int(input().strip().replace(" ", ""))
    if (day_1.is_integer() == False) :
        print(f'This "{day_1}" is not an integer value')
        exit(1)
    print('Day 2 harvest: ', end='')
    day_2: int = int(input().strip().replace(" ", ""))
    if (day_2.is_integer() == False) :
        print(f'This "{day_2}" is not an integer value')
        exit(1)
    print('Day 3 harvest: ', end='')
    day_3: int = int(input().strip().replace(" ", ""))
    if (day_3.is_integer() == False) :
        print(f'This "{day_3}" is not an integer value')
        exit(1)
    print('Total harvest:', day_1 + day_2 + day_3)


# def main():
#     ft_harvest_total()

# main()