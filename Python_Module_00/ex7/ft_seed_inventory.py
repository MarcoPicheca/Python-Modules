def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None :
    if not seed_type or not unit :
        print('Need more params!')
        return
    type_unit: list[str] = ['packets', 'grams', 'area']
    print_unit: str = ''
    if unit in type_unit :
        match unit:
            case 'packets':
                print_unit = f'{quantity} packets available'
            case 'grams':
                print_unit = f'{quantity} grams total'
            case 'area':
                print_unit = f'covers {quantity} square meters'
            case _:
                print('Unknown unit type')
                return
    print(seed_type.capitalize(), 'seeds:', print_unit)

# def main():
#     ft_seed_inventory('carrot', 0,  'area')

# main()
