def ft_count_harvest_iterative() -> None:
    print('Days since last watering: ', end='')
    days: range = range(int(input().strip().replace(" ", "")))
    for day in days :
        print(f'Day {day + 1}')
    print('Harvest time!')

# def main() :
#     ft_count_harvest_iterative()

# main()