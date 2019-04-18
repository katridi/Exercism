def distance(strand_a, strand_b): 
    s = 0
    check_lenght(strand_a, strand_b)
    for l1,l2 in zip(strand_a, strand_b):
        if l2 != l1:
            s += 1
    return s

def check_lenght(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Sequences must have equal lenght')