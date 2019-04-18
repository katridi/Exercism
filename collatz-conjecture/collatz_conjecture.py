def collatz_steps(number):
    check_input(number)
    steps = 0
    while number > 1 :
        if number % 2 == 0:
            number /= 2
        else:
            number =  3 * number + 1
        steps += 1
    return steps
    
def check_input(number):
    if number <= 0:
        raise ValueError('Value must be greater than zero')