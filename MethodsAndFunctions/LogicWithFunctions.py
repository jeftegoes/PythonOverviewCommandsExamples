def even_check(number: int):
    return number % 2 == 0


print(f"1: {even_check(20)}")
print(f"2: {even_check(21)}")


def check_event_list(num_list: list[int]):
    for number in num_list:
        if (number % 2 == 0):
            return True
        else:
            pass

    return False


def return_event_list(num_list: list[int]):
    even_list: list[int] = []

    for number in num_list:
        if (number % 2 == 0):
            even_list.append(number)
        else:
            pass

    return even_list


print(f"3: {check_event_list([1,3,5])}")
print(f"4: {check_event_list([2, 4, 5])}")
print(f"5: {return_event_list([2, 4, 5])}")
print(f"6: {return_event_list([1,3,5])}")
