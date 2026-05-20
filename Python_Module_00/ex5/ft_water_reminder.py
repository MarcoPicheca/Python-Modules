def ft_water_reminder() -> None :
    print('Days since last watering: ', end='')
    days: int = int(input().strip().replace(" ", ""))
    if days > 2 :
        print('Water the plants!')
    else :
        print('Plants are fine')

# def main():
#     ft_water_reminder()

# main()