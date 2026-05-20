def ft_count_harvest_recursive(count: int = 0, days: int = 0) :
    if (count == 0 and days == 0):
        print('Days since last watering: ', end='')
        days: int = int(input().strip().replace(" ", ""))
        if days < 0 :
            return
    count += 1
    if days > 0 and count <= days and count > 0 :
        print(f'Day {count}')
        ft_count_harvest_recursive(count, days)
    if days == count and count > 0 :
        print('Harvest time!')

# def main() :
#     ft_count_harvest_iterative()

# main()