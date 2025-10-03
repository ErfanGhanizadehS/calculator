def show_menu():
    print("menu:\n"
          "1)Ability performance:\n"
          "2)Sum performance:\n"
          "3)Show performance:\n"
          "4)Remove item:\n"
          "5)Exit:\n"
          )
    choose = int(input("Please enter your number:"))
    print("=" * 70)
    return choose


list_of_pow = []
list_of_sum = []


def pow_performance():
    number_1 = float(input("Please enter first number:"))
    number_2 = float(input("Please enter second number:"))
    result = number_1 ** number_2
    list_of_pow.append(result)
    print("=" * 70)
    return result


def sum_performance():
    number_1 = float(input("please enter first number:"))
    number_2 = float(input("please enter second number:"))
    result = number_1 + number_2
    list_of_sum.append(result)
    print("=" * 70)
    return result


def show_list():
    print("your list of ability is:", list_of_pow)
    print("your list of sum is:", list_of_sum)
    print("=" * 70)


def remove_item():
    print("1)the list of ability is:", list_of_pow)
    print("2)the list of sum is:", list_of_sum)
    select = int(input("please input number 1 or 2:"))

    if select == 1:
        remove = float(input("please enter the item that you want to remove:"))
        for remove in list_of_pow:
            list_of_pow.remove(remove)
            print("Item removed successfully!")
    elif select == 2:
        remove = float(input("please enter the item that you want to remove:"))
        for remove in list_of_sum:
            list_of_sum.remove(remove)
            print("Item removed successfully!")
    else:
        print("invalid option!!!")

    print("=" * 70)
