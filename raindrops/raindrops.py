def raindrops(number, tuple_raindrop=((3,'Pling'), (5,'Plang'), (7, 'Plong'))):
    to_return = [sound for sound,factor in tuple_raindrop if number % factor == 0]
    if to_return:
        return ''.join(to_return)
    return str(number)
