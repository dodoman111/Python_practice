Ch14-A
#1
def f1(lst):
    for i in range(len(lst)):
        if lst[i] >=0:
            if lst[i]**0.5 - int(lst[i]**0.5) = 0:
                return lst[i]
    return -1

#2
def f2(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] >=0:
            if lst[i]**0.5 - int(lst[i]**0.5) = 0:
                count += 1
    return count

#3
def second_largest(values):
    a = sorted(values, reverse = True)
    return a[1]

#4
def digit(num,pos):              #n자리수에 위치한 숫자 값 찾기
    return (num//10**(pos-1))%10

def num_in_french(num):
    ones_list = ['zero','un','deux','trois','quatre','cinq','six','sept','huit','neuf','dix','onze','douze','treize','quatorze','quinze','seize','dix-sept','dix-huit','dix-neuf']
    tens_list = ['','dix','vingt','trente','quarante','cinquante','soixante','soixante','quatre-vingt','quatre-vingt']
    if num < 20:
        return ones_list[num]
    if num == 100:
        return 'cent'
    if num >= 70 and num <80:
        a,b = digit(num,2),digit(num,1)
        if b ==1:
            return tens_list[a]+' et '+ones_list[b+10]
        return tens_list[a]+'-'+ones_list[b+10]
    if num >= 80 and num <=99:
        a,b = digit(num,2),(num-80)
        if b == 0:
            return tens_list[a]+'s'
        elif digit(b,1) ==1:
            return tens_list[a]+'-'+ones_list[b]
        return tens_list[a]+'-'+ones_list[b]
    if num >= 20 and num < 70 :
        if digit(num,1) ==0:
            return tens_list[digit(num,2)]
        elif digit(num,1) ==1:
            return tens_list[digit(num,2)] +' et '+ones_list[digit(num,1)]   
        else :
            return tens_list[digit(num,2)] +'-'+ones_list[digit(num,1)]

def print_French(lo,hi):
    for i in range(lo,hi+1):
        print(i,num_in_french(i))


Ch14-B
#1
def count_matches(some_list,value):
    if some_list ==[]:
        return 0
    if some_list[0] == value:
        return 1 + count_matches(some_list[1:],value)
    else:
        return count_matches(some_list[1:],value)

#2
def double_each(some_list):
    a =[]
    if some_list ==[]:
        return a
    return a + [some_list[0]]*2 + double_each(some_list[1:])

#3
a = 0
def sums_to(nums,k):
    global a
    if nums ==[]:
        if a == k:
            return True
        else : return False
    else:
        a = nums[0] + a
        return sums_to(nums[1:],k)

#4
def is_reverse(string1,string2):
    if string1 == '' and string2 == '':
        return True
    if string1 !='' and string2 !='' and string1[0] == string2[-1]:
        return is_reverse(string1[1:],string2[:-1]) 
    else: 
        return False

#5
def sort_repeated(L):
    a = set()
    for j in L:
        if L.count(j) > 1:
            a.add(j)
    return list(a)

#6
def make_Dict_number(lst):          #신버전
    d = {}
    for k in sorted(lst):
        d[k] = lst.count(k)
    return d


def make_Dict_number(lst):          #구버전
    s  ={}
    L = sorted(lst) +['']
    count  = 1
    for i in range(len(L)-1):
        if L[i] == L[i+1]:
            count += 1
        else :  
            s[L[i]] = count
            count = 1
    return s

----------get()쓰지 않은 버전----------
def mostFrequent(lst):
    a =[]
    d = make_Dict_number(lst)
    maxv = max(d.values())
    for i in d.keys():
        if d[i] == maxv:
            a.append(i)
    print(*a)
    
-------------get() 쓴 버전-------------
def mostFrequent(lst):
    a =[]
    d = make_Dict_number(lst)
    maxv = max(d.values())
    for i in d.keys():
        if d.get(i) == maxv:
            a.append(i)
    print(*a)

#7
def histogram(letters):
    answer={}
    for i in range(len(letters)):
        answer[list(letters.values())[[i]]=list(letters.values()).count(list(letters.values()[i])
    return answer
