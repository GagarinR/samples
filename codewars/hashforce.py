import hashlib

shakey= 'e6fb06210fafc02fd7479ddbed2d042cc3a5155e'# res = 'code'

def password_cracker(hash):

    arraz = 'abcdefghijklmnopqrstuvwxyz'
    for c in range(26):

       for cu in range(26):
            for cur in range(26):
                for current in range(26):

                    #print c, cu, cur, current, i
                    for i in arraz:
                        if hashlib.sha1(i.encode('utf-8')).hexdigest() == hash:
                                return str(i)

                        if c == 1:

                            # print arraz[current] +i
                            if hashlib.sha1((arraz[current] +i).encode('utf-8')).hexdigest() == hash:
                                return str(arraz[current] +i)
                        if c == 2:
                            # print arraz[cur] + arraz[current] + i
                            if hashlib.sha1((arraz[cur] + arraz[current] + i).encode('utf-8')).hexdigest() == hash:
                                return str(arraz[cur] + arraz[current] + i)
                        if c == 3:
                            # print arraz[cu] + arraz[cur] + arraz[current] + i
                            if hashlib.sha1((arraz[cu] + arraz[cur] + arraz[current] + i).encode('utf-8')).hexdigest() == hash:
                                return str(arraz[cu] + arraz[cur] + arraz[current] + i)
                        if c == 4:
                            # print arraz[c] + arraz[cu] + arraz[cur] + arraz[current] + i
                            if hashlib.sha1((arraz[c] + arraz[cu] + arraz[cur] + arraz[current] + i).encode('utf-8')).hexdigest() == hash:
                                return str(arraz[c] + arraz[cu] + arraz[cur] + arraz[current] + i)
    return ''
    
    print (password_cracker(shakey))
