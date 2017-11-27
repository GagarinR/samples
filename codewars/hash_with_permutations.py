# does not work with worda that have duplicate letters, for example, 'test'
import hashlib
from itertools import permutations

# zv_hash = '29ce0a95c5081c4dfe49e8b9d22463bc8120ae1d'
# p_hash = '516b9783fca517eecbd1d064da2d165310b19759'
zsdcb_hash ='ad5c7127070d698aa8fe4aa27d612a8cf62c6db9'
test_hash = 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'
def password_cracker(hash):
    arraz = 'abcdefghijklmnopqrstuvwxyz'
    count_of_variants = 0
    lst = [permutations(arraz, i) for i in range(1, 6)]
    print(len(lst))
    for perm_object in lst:
        for word in perm_object:
            count_of_variants += 1
            # print(word)
            word_encoded = ''.join(word).encode('utf-8')
            # print(word_encoded)
            cur_hash = hashlib.sha1(word_encoded).hexdigest()
            # print(cur_hash)
            if cur_hash == hash:
                return word_encoded.decode()
    return ''

print(password_cracker(test_hash))