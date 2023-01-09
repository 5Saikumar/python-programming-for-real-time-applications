def sai(x,y):
    if len(x)!=len(y):
        return False
    for i in range(len(x)):
        count=0
        if x.count(x[i])!=y.count(y[i]):
            return False
    return True
print(sai("fool","poor"))
print(sai("foal","poor"))
print(sai("too","bar"))
print(sai("toto","yaya"))
