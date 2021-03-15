def source_code(n):	
    return f"""# Taken from: https://www.rosettacode.org/wiki/Create_an_HTML_table#Python

import random
random.seed(983475092375093475098234759082346)
 
def rand9999():
    return random.randint(1000, 9999)
 
def tag(attr='', **kwargs):
    for tag, txt in kwargs.items():
        return '<{{tag}}{{attr}}>{{txt}}</{{tag}}>'.format(**locals())

def print(*args, **kwargs):
    pass

n = {n}
if __name__ == '__main__':
    header = tag(tr=''.join(tag(th=txt) for txt in ',X,Y,Z'.split(','))) + '\\n'
    rows = '\\n'.join(tag(tr=''.join(tag(' style="font-weight: bold;"', td=i)
                                    + ''.join(tag(td=rand9999())
                                              for j in range(3))))
                     for i in range(1, n))
    table = tag(table='\\n' + header + rows + '\\n')
    print(table)

"""
