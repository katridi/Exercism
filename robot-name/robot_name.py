from random import choice, randint, seed

import string

class Robot(object):
    
    def make_uname(self):
        return self.two_random_letters() + self.three_random_digit()
    
    def __init__(self):
        self.unique_names = set()
        self.name = self.make_uname()
        if self.name not in self.unique_names:
            self.unique_names.add(self.name)
        else:
            self.reset()
        
    def reset(self):
        seed(17)
        self.name = self.make_uname()
    
    def two_random_letters(self):
        return ''.join([choice(string.ascii_uppercase) for x in range(2)])
   
    def three_random_digit(self):
        return ''.join([str(randint(0,9)) for x in range(3)])
