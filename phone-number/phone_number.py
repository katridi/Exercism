import re


class Phone(object):
    
    def __init__(self, phone_number):
        
        self.number = self.is_number_valid(phone_number)
        
        self.area_code = self.is_area_code_valid(self.number[:3])
        
        self.exchange_code = self.is_exchange_code_valid(self.number[3:6])
    
    def is_number_valid(self, number):
        
        this_number = "".join(re.findall(r'\d+', number))
        #more or less than 9 or 11 digits respectively
        if len(this_number) < 9 or len(this_number) > 11:
            raise ValueError('Something is wrong in input format.')
        #1 is first?       
        if len(this_number) == 11:
            if this_number[0] == "1":
                return this_number[1:]
            else:
                raise ValueError('Something is wrong in input format.')
        return this_number
    
    
    def is_area_code_valid(self, area):
        if area[0] == "0" or area[0] == "1":
            raise ValueError('Something is wrong in input format.')
        return area
    
    def is_exchange_code_valid(self, code):
        if code[0] == "0" or code[0] == "1":
            raise ValueError('Something is wrong in input format.')
        return code
        
    
    
    def pretty(self):
        return ("({0}) {1}-{2}".format(self.area_code, self.exchange_code, self.number[6:]))
