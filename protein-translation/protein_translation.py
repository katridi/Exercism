import re

my_dict = {'AUG': 'Methionine',
           'UUU': 'Phenylalanine',
           'UUC': 'Phenylalanine',
           'UUA': 'Leucine',
           'UUG': 'Leucine',
           'UCU': 'Serine',
           'UCC': 'Serine',
           'UCA': 'Serine',
           'UCG': 'Serine',
           'UAU': 'Tyrosine',
           'UAC': 'Tyrosine',
           'UGU': 'Cysteine',
           'UGC': 'Cysteine',
           'UGG': 'Tryptophan',
          }

stop_pattern = ['UAA', 'UAG', 'UGA']

def proteins(strand):
    result = re.search('|'.join(stop_pattern), strand)
    index = result.start() if result else len(strand)

    return [my_dict.get(x.group()) for x in re.finditer(r'\w{3}', strand[:index])]

