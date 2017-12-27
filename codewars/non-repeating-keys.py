l = [{'acb': 0}, {'acb': 1}, {'ab': 2}, {'yxz': 3}, {'yxz': 5}, {'yx': 4}]
'тут ab и yx лишние'

from operator import itemgetter
from collections import Counter


def remove_non_repeating(lst):

    lst2 = [(key, value) for dictionary in lst for key, value in dictionary.items()]
    getKeys = itemgetter(0)
    counted_keys = (Counter(map(getKeys, lst2)))
    unique_keys = [key for key, value in counted_keys.items() if value == 1]
    for item in lst2:
        if item[0] in unique_keys:
            lst2.remove(item)
    return [{item[0]: item[1]} for item in lst2]

print(remove_non_repeating(l))