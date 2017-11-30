class Calculator(object):

    def make_calc(self, spltstr):
        def __init__(self):
            self.final = []
        # print(spltstr)
        calc_devide = lambda x, y: x / y
        calc_mul = lambda x, y: x * y
        calc_sum = lambda x, y: x + y
        calc_sub = lambda x, y: x - y

        for i2, i in enumerate(spltstr):

            if i == '/':

                res = [int(calc_devide(int(spltstr[i2 - 1]), int(spltstr[i2 + 1])))]
                first_p = [spltstr[i] for i in range(0, i2 - 1)]
                last_p = [spltstr[i] for i in range(i2 + 2, len(spltstr))]
                lst = first_p + res + last_p
                self.final = lst
                return self.make_calc(lst)
        
        
        for i2, i in enumerate(spltstr):

            if i == '*':
                res = [int(calc_mul(int(spltstr[i2 - 1]), int(spltstr[i2 + 1])))]
                first_p = [spltstr[i] for i in range(0, i2 - 1)]
                last_p = [spltstr[i] for i in range(i2 + 2, len(spltstr))]
                lst = first_p + res + last_p
                self.final = lst
                return self.make_calc(lst)
        
        
        for i2, i in enumerate(spltstr):

            if i == '+':
                # print(spltstr, i, i2)
                res = [int(calc_sum(int(spltstr[i2 - 1]), int(spltstr[i2 + 1])))]
                first_p = [spltstr[i] for i in range(0, i2 - 1)]
                last_p = [spltstr[i] for i in range(i2 + 2, len(spltstr))]
                lst = first_p + res + last_p
                self.final = lst
                return self.make_calc(lst)
        
        
        for i2, i in enumerate(spltstr):

            if i == '-':
                
                res = [int(calc_sub(int(spltstr[i2 - 1]), int(spltstr[i2 + 1])))]
                first_p = [spltstr[i] for i in range(0, i2 - 1)]
                last_p = [spltstr[i] for i in range(i2 + 2, len(spltstr))]
                lst = first_p + res + last_p
                self.final = lst
                return self.make_calc(lst)
                
        # print (final)
        #input("")
        if self.final == [7]:
            print ("this is final", self.final)
            return '!!!!!!!!!Final == 7, But try to return 7))))))!!!!!!!'



    def evaluate(self, string):
        spltstr = string.split(" ")
        return self.make_calc(spltstr)

print (Calculator().evaluate('2 / 2 + 3 * 4 - 6'))
