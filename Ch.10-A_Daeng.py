Ch. 10-A
#1
def f1(lst):
    return len(list(filter(lambda x :x%2==1,lst)))

#2
def f2(lst):
    return list(filter(lambda x :x%2==1,lst))

#3
def f3(lst):
    return sum((filter(lambda x :x%2==1,lst)))

#4
def f4(lst):
    sum=0
    for idx,val in enumerate(lst):
        if val %2 ==1:
            sum +=idx
    return sum

#5
def f5(lst):
    return list(map(lambda x : x**2,lst))

#6
def f6(lst):
    return max(lst)

#7
def f7(lst):
    return sum(lst)/len(lst)

#8
def f8(a,b,n):
    lst = list(range(a,b+1))
    lst = list(filter(lambda x: x%n==0,lst))
    for i in lst:
        print(i)

#9
def f9(w,h):
    for i in range(h):
        print(*list(map(lambda x : '*'* x, [w])))

#10
def f10(n):
    lst = list(range(1,n+1))
    for i in lst:
        print('*'*i)

#11
def f11(lst):
    if lst == sorted(lst,reverse=True):
        return True
    else : return False
    
#12
def f12(lst):
    if max(lst)<0:
        return True
    else: return False

#13
def f13(lst,tar):
    a = list(enumerate(lst))
    for i in range(len(a)-1,-1,-1):
        if a[i][1] == tar:
            return i

#14
def f14(lst):
    for i,v in enumerate(reversed(lst)):
        if v < 0:
            return(len(lst)-i-1)

#15
def f15(lst):
    sum = 0
    for i,v in enumerate(lst):
        if i % 2 ==0:
            sum += v
    return sum

#16
def f16(n):
    for i in range(n,0,-1):
        print('*'*i)

#17
def f17(lst):
    a = reversed(lst)
    for i in a:
        if i %2 ==0:
            print(i)

#18
def f18(n):
    if n ==0:
        return 1
    return n*f18(n-1)

#19
def f19(mat):
    for i in range(0,len(mat)):
        print(sum(mat[i]))

#20
def f20(mat):
    for i,v in enumerate(mat):
        print(mat[i][i])

#21
def f21(lst):
    a = list(map(lambda x : f18(x),lst))
    for i in a:
        print(i)

#22
def f22(lst):
    for i in lst:
        print(*list(range(i,-1,-1)))

#23
def f23(lst1,lst2):
    a =[]
    for i,v in enumerate(lst1):
        for i2,v2 in enumerate(lst2):
            if i == i2:
                a.append(v+v2)
    print(a)

#24
def f24(n):
    nn = range(2,n+1)
    a = list(filter(lambda x: x%2==0 or x%3==0,nn))
    for i in a:
        print(i)

#25
def f25(lst):
    print(max(max(*lst)))

#26
def f26(lst):
    a = sorted(lst)
    print(a[-2])

#27 흠......
def f27(n):
    while n>=10:
        n = n//10
    print(n)

#28
def f28(lst):
    for i in lst:
        print(max(i))
