Ch 7-A_Daeng

#1
def f1(lst):
    if lst == []:
        return 0
    return lst[0] + f1(lst[1:])

#2
def f2(n):
    if n == 1:
        return 1
    if n%2==0:
        return 1+ f2(n//2)
    else:
        return 1+ f2(3*n+1)

#3
def f3(lst):
    if lst ==[]:
        return 0
    else: 
        print(lst[-1])
        lst = f3(lst[:-1])

#4
def f4(lst):
    if lst == []:
        return 0
    if lst[0]%2==1:
        print(lst[0]*3)
    lst = f4(lst[1:])

#5
def f5(lst):
    if lst ==[]:
        return 
    if lst[-1] %2 == 1:
        print(lst[-1]*3)
    else:
        print(lst[-1])
    lst = f5(lst[:-1])

#6
def f6(lst):
    if lst == []:
        return lst
    if type(lst[0]) == list:
        return f6(lst[0]) + f6(lst[1:])
    else:
        return [lst[0]]+ f6(lst[1:])

#7  문제뭐임

    
#8
def f8(s):
    if s == '':
        return True
    if s[0] == s[-1]:
        return f8(s[1:-1])
    else:
        return False

#9
def f9(n):
    if n ==0:
        return 1
    return n*f9(n-1)

#10
def f10(lst):
    if lst ==[]:
        return 0
    return 1+f10(lst[1:])

#11
def f11(lst):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) ==0:
        return 
    else: return f11(lst[1:])
------------------------------
def f11(lst):
    return lst[-1]
    
#12
def f12(n):
    if n == 0:
        return
    print(n) 
    n = f12(n-1)

#13
def f13(n):
    if n ==0:
        return 0
    return 1+f13(n//10)

#14
def f14(lst):
    if lst ==[]:
        return
    if lst[0]%2==1:
        return lst[0]
    else:
        return f14(lst[1:])

#15
def f15(lst):
    if lst ==[]:
        return 0
    if lst[0]%2==1:
        return lst[0]+f15(lst[1:])
    else:
        return f15(lst[1:])

#16
def f16(lst):
    if lst ==[]:
        return lst
    if lst[0]%2 ==1:
        return [lst[0]]+f16(lst[1:])
    else:
        return f16(lst[1:])

#17
def f17(lst):
    if len(lst)==2:
        return lst[0]
    return f17(lst[1:])

#18
def f18(a,b):
    if b ==0:
        return a
    return f18(b,a%b)

#19
def f19(lst1, lst2):
    lind, rind = 0, 0
    resul = []
    while lind < len(lst1) and rind < len(lst2):
        if lst1[lind] < lst2[rind]:
            resul.append(lst1[lind])
            lind += 1
        else:
            resul.append(lst2[rind])
            rind += 1

    resul += lst1[lind:]
    resul += lst2[rind:]
    return resul

---------------------------------------------------
이건 왜..오류가...
def f19(lst1,lst2):
    if lst1 ==[] and lst2 ==[]:
        return lst
    if lst1[0]>=lst2[0]:
        return [lst2[0]]+f19(lst1,lst2[1:]))
    else:
        return [lst1[0]]+f19(lst1[1:],lst2))

#20
def f20(lst):
    if len(lst) == 1:
        return lst
    mid = int(len(lst) / 2)
    lst1 = f20(lst[:mid])
    lst2 = f20(lst[mid:])
    return f19(lst1, lst2)
