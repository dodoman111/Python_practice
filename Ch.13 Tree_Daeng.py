#Ch. 13-A

#21
def f21(tree):
    if tree ==[]:
        return 0
    else:
        if tree[1]<tree[2]:
            return 1+ f21(tree[2])
        else:
            return 1+ f21(tree[1])

-----------------------------------------------
def f21(tree):
    if tree ==[]:
        return 0
    else:
        return 1+ max(f21(tree[1]),f21(tree[2]))
    
#22
def f22(tree):
    if tree ==[]:
        return 0
    else:
        return 1+f22(tree[1])+f22(tree[2])

#23
def f23(tree):
    if tree ==[]:
        return 0
    else:
        return tree[0]+f23(tree[1])+f23(tree[2])

#24
def f24(tree):
    if tree ==[]:
        return
    f24(tree[1])
    print(tree[0])
    f24(tree[2])

#25
def f25(tree):
    if tree ==[]:
        return -1
    if tree[1] ==[] and tree[2]==[]:
        return tree[0]
    
    return f25(tree[1])
---------------------------------------------
def f25(tree):
    if tree ==[]:
        return -1
    if min(tree[1],tree[2]) == []:
        return tree[0]

    return f25(tree[1])
