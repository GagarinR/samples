lst = [12, 6, 77, 99, 1, 23, 55, 45, 33, 44, 21]
s = 100


def numbers_of_sum(numbers, target_sum):
    already_seen = set()
    result = []
    for number in numbers:
        second_number = target_sum - number
        if number in already_seen:
            result.append([second_number, number])
        else:
            already_seen.add(second_number)
    print(already_seen)
    return result


print(numbers_of_sum(lst, s))
