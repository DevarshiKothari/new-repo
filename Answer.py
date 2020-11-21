from collections import defaultdict

def fun1():
    return 0

def subs(s):
    n=len(s)
    x=len(set(list(s)))
    d=defaultdict(fun1)
    c=0
    low=0
    high=n
    y=-1

    for j in range(n):
        d[s[j]]=d[s[j]]+1
        if d[s[j]]==1:
            c=c+1
        if c==x:
            while d[s[low]]>1:
                if d[s[low]]>1:
                    d[s[low]]=d[s[low]]-1
                low=low+1

            y=j-low+1
            if high>y:
                high=y
                z=low

    return len(str(s[z:z+high]))


s=input()
print(subs(s))
