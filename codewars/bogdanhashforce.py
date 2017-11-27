import hashlib
from itertools import islice
shakey = 'e6fb06210fafc02fd7479ddbed2d042cc3a5155e'  # res = 'code'
z_hash = '395df8f7c51f007019cb30201c49e884b46b92fa'
zv_hash = '29ce0a95c5081c4dfe49e8b9d22463bc8120ae1d'
zzz_hash = '40fa37ec00c761c7dbb6ebdee6d4a260b922f5f4'
aaac_hash = '00b25f15212ed225d3389b5f75369c82084b3a76'
aaabc_hash = 'ef34c4e68d0b585a83b6d4876c0c25b30f775b52'
def password_cracker(hash=shakey):
    # nahuy etot pep. Array of letters with .encode already applied
    arraz = [b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i', b'j', 
            b'k', b'l', b'm', b'n', b'o', b'p', b'q', b'r', b's', b't', 
            b'u', b'v', b'w', b'x', b'y', b'z']
    number_of_letters = 26
    # Check if it's only one letter
    for first_letter in islice(arraz, 0, number_of_letters):
        if hashlib.sha1(first_letter).hexdigest() == hash:
            return first_letter.decode()
    # Only Two?
    for first_letter in islice(arraz, 0, number_of_letters):
        for second_letter in islice(arraz, 0, number_of_letters):
            word = first_letter + \
                   second_letter
            if hashlib.sha1(word).hexdigest() == hash:
                return word.decode()
    # Only Three?
    for first_letter in islice(arraz, 0, number_of_letters):
        for second_letter in islice(arraz, 0, number_of_letters):
            for third_letter in islice(arraz, 0, number_of_letters):
                word = first_letter + \
                       second_letter + \
                       third_letter
                # print (hashlib.sha1(word).hexdigest())
                if hashlib.sha1(word).hexdigest() == hash:
                    return word.decode()
    # Only Four?
    for first_letter in islice(arraz, 0, number_of_letters):
        for second_letter in islice(arraz, 0, number_of_letters):
            for third_letter in islice(arraz, 0, number_of_letters):
                for fourth_letter in islice(arraz, 0, number_of_letters):
                    word = first_letter + \
                    second_letter + \
                    third_letter + \
                    fourth_letter
                    if hashlib.sha1(word).hexdigest() == hash:
                        return word.decode()
    # Only Five?
    for first_letter in islice(arraz, 0, number_of_letters):
        for second_letter in islice(arraz, 0, number_of_letters):
            for third_letter in islice(arraz, 0, number_of_letters):
                for fourth_letter in islice(arraz, 0, number_of_letters):
                    for fifth_letter in islice(arraz, 0, number_of_letters):
                        word = first_letter + \
                        second_letter + \
                        third_letter + \
                        fourth_letter + \
                        fifth_letter
                        if hashlib.sha1(word).hexdigest() == hash:
                            return word.decode()
print(password_cracker(aaabc_hash))
