from simple_calculater import *

while True:
    first_attempt = show_menu()

    if first_attempt == 1:
        first_performance = ability_performance()
        print("Result:", first_performance)
    elif first_attempt == 2:
        second_performance = sum_performance()
        print("Result:", second_performance)
    elif first_attempt == 3:
        show_list()
    elif first_attempt == 4:
        remove_item()
    elif first_attempt == 5:
        print("good bye!")
        break
    else:
        print("invalid number!!!")