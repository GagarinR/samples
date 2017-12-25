import hashlib
from pprint import pprint
from itertools import permutations, islice, count, permutations, product
arraz = 'abcdefghijklmnopqrstuvwxyz'
# zv_hash = '29ce0a95c5081c4dfe49e8b9d22463bc8120ae1d'

# word_encoded = hashlib.sha1(b'test').hexdigest()
# print(word_encoded)
# # print(word_encoded)

# # cur_hash = hashlib.sha1(word_encoded).hexdigest()
# pprint(dir(hashlib))
# pprint(dir(hashlib.sha1(b'asdf').update().__doc__))
# a = 'abc'
# print('permutations:')
# for i in permutations(a, 2):
# 	print(i)
# print("combinations_with_replacement:")
# for i in combinations_with_replacement(a, 2):
# 	print(i)


# a = hashlib.sha1(b'tes')
# print(type(a))
# print(a.hexdigest())
# print('updated')
# a.update(b't')
# print(a.hexdigest())

# print("test")

arraz = 'abcdefghijklmnopqrstuvwxyz'
m = [i for i in arraz]
print (m)
for comb in product(arraz, repeat=2):
    print (''.join(comb))