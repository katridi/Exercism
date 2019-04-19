def distance(strand_a, strand_b): 
    check_length(strand_a, strand_b)
    return sum([l2 != l1 for l1,l2 in zip(strand_a, strand_b)])

def check_length(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Sequences must have equal lenght')