l=[9,3,54,23,65,19,23,33,41,70]
def sumsquare(l):
    odd=0
    even=0
    for i in l:
        if i%2==0:
            even=even+i**2
        else:
            odd=odd+i**2
    l=[odd,even]
    return(l)
print(sumsquare(l))
