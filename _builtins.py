#all()
def all_(iterable):
    if len(iterable) == 0:
        return True
    else:
        for i in iterable:
            if i:
                continue
            return False
        return True
#divmod()
def divmod_(a,b):
    c=a-(a//b)
    d=(a-c)//b
    return d,c
#pow()
def pow_(a,b):
    if b==1:
        return a
    else:
        return b*pow_(a,b-1)
#any()
def any_(iterable):
    if len(iterable) == 0:
        return False
    else:
        for i in iterable:
            if i:
                return True
        return False
#sum()
def sum_(iterable):
    plus=0
    for i in iterable:
        plus+=i
    return plus
#len()
def len_(iterable):
    plus=0
    for i in iterable:
        plus+=1
    return plus
#filter()
def filter_(iterable,func=lambda a :-1):
    for i in iterable:
        if func(i):
            yield i
#range()
def range_(*,start=0,step=1,stop=None):
    if stop is None:
        raise TypeError("range() needs a keyword-only argument 'stop'")
    c=start-step
    for i in __import__("itertools").count(start):
        c+=step 
        if c >= stop:
            break
        yield c
    return
#map()
def map_(iterable,func=lambda a :-1):
    for i in iterable:
        yield func(i)
#enumerate()
def enumerate_(iterable,start=0):
    m=[]
    for i in iterable:
        m.append((((list(iterable).index(i))+start),i))
    return m
#abs()
def abs_(num):
    return num if num > 0 else -num
#round()
def round_(num):
    m=__import__("math").ceil(num)
    l=int(num)
    if m-num > l-num:
        return l
    return m
#min()
def min_(iterable):
    min=iterable[0]
    for i in iterable:
        if min>i:
            min=i
    return min
def max_(iterable):
    max=iterable[0]
    for i in iterable:
        if max<i:
            max=i
    return max
            