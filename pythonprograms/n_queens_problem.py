def source_code(n):	
    return f"""# Taken from: https://www.rosettacode.org/wiki/N-queens_problem#Python

from itertools import permutations

def print(*args, **kwargs):
    pass

n = {n}
cols = range(n)
for vec in permutations(cols):
    if n == len(set(vec[i]+i for i in cols)) \\
         == len(set(vec[i]-i for i in cols)):
        print ( vec )

"""
