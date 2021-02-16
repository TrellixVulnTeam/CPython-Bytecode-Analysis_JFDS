n = 1310719
min_n = 1
def source_code(n):	
    return f"""# Taken from: https://www.rosettacode.org/wiki/Self_numbers#Python

class DigitSumer :
    def __init__(self): 
        sumdigit = lambda n : sum( map( int,str( n )))
        self.t = [sumdigit( i ) for i in range( 10000 )]
    def __call__ ( self,n ):
        r = 0
        while n >= 10000 :
            n,q = divmod( n,10000 )
            r += self.t[q]
        return r + self.t[n] 
 
 
def self_numbers ():
    d = DigitSumer()
    s = set([])
    i = 1
    while 1 :
        n = i + d( i )
        if i in s :
            s.discard( i )
        else:
            yield i
        s.add( n )
        i += 1

def print(*args, **kwargs):
    pass

n = {n}

import time
p = 100
t = time.time()
for i,s in enumerate(self_numbers(), 1):
    if i <= 50 : 
        print(s, end=" ")
        if i == 50 : print()
    if i == p :
        print( '%7.1f sec  %9dth = %d'%( time.time()-t,i,s ))
        p *= 10
    if i == n:
        break

"""
