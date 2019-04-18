def is_armstrong(number):
    return number == sum([int(x) ** len(str(number)) for x in str(number)])
