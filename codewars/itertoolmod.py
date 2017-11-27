import hashlib
import time
from itertools import islice

shakey= 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'
shakey = 'e6fb06210fafc02fd7479ddbed2d042cc3a5155e'  # res = 'code'
z_hash = '395df8f7c51f007019cb30201c49e884b46b92fa'
zv_hash = '29ce0a95c5081c4dfe49e8b9d22463bc8120ae1d'
zzz_hash = '40fa37ec00c761c7dbb6ebdee6d4a260b922f5f4'
aaac_hash = '00b25f15212ed225d3389b5f75369c82084b3a76'
aaabc_hash = 'ef34c4e68d0b585a83b6d4876c0c25b30f775b52'

def password_cracker222(hash):
    start_time = time.time()
    arr = [b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i', b'j',
             b'k', b'l', b'm', b'n', b'o', b'p', b'q', b'r', b's', b't',
             b'u', b'v', b'w', b'x', b'y', b'z']
    
    for c1 in islice(arr, 0, 26):
        for c2 in islice(arr, 0, 26):
            for c3 in islice(arr, 0, 26):
                for c4 in islice(arr, 0, 26):
                    for c5 in islice(arr, 0, 26):
                        
                            if hashlib.sha1(c5).hexdigest() == hash:
                                end_time = time.time()
                                print(end_time - start_time)
                                return c5.decode()
                        
                            if hashlib.sha1(c4 + c5).hexdigest() == hash:
                                end_time = time.time()
                                print(end_time - start_time)
                                return (c4 +c5).decode()
                        
                            if hashlib.sha1(c3+ c4 + c5).hexdigest() == hash:
                                end_time = time.time()
                                print(end_time - start_time)
                                return (c3+ c4 + c5).decode()
                        
                            if hashlib.sha1(c2+ c3+ c4 + c5).hexdigest() == hash:
                                end_time = time.time()
                                print(end_time - start_time)
                                return (c2+ c3+ c4 + c5).decode()
                       
                            if hashlib.sha1(c1+c2+ c3+ c4 + c5).hexdigest() == hash:
                                end_time = time.time()
                                print(end_time - start_time)
                                return (c1+c2+ c3+ c4 + c5).decode()

    return ''
    
    print (password_cracker222(zzz_hash))
