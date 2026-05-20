def ft_plot_area() -> None:
    print('Enter lenght: ', end='')
    lenght: int = int(input().strip().replace(" ", ""))
    if (lenght.is_integer() == False) :
        print(f'This "{lenght}" is not an integer value')
        exit(1)

    print('Enter width: ', end='')
    width: int = int(input().strip().replace(" ", ""))
    if (width.is_integer() == False) :
        print(f'This "{width}" is not an integer value')
        exit(1)
    print('Plot area:', lenght * width)


# def main():
#     ft_plot_area()

# main()