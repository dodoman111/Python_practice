##################  <PART A>    #################

#################sieve를 위한 함수 생성###############
def sift(lst,k):
	i = 0
	while i < len(lst):
		if lst[i] != 0 and lst[i]%k==0:
			lst[i] = None
		i = i+1
	return lst


def sieve_p26(n):
	numlist = list(range(2,n+1))
	primes=[]
	for i in range(0,len(numlist)):
                if numlist[i] != None:
                        primes.append(numlist[i])
                        sift(numlist,numlist[i])
	return primes

def sieve_p28(n):
	numlist = list(range(2,n+1))
	primes=[]
	i = 0
	while (i+2)<=math.sqrt(n):
            if numlist[i] != None:
                primes.append(numlist[i])
                sift(numlist,numlist[i])
            i = i+1
        temp_list=[]
        for i in range(0,len(numlist)):
            if numlist[i] != None:
                temp_list.append(numlist[i])
        numlist = temp_list
        return primes +numlist

################## 성능평가 sieve_p26 ##################

import time
start = time.clock()

sieve_p26(100)
    
end = time.clock()
duration = end-start


################# 성능평가 sieve_p28 ##################

import time
start = time.clock()
sieve_p28(100)
end = time.clock()
duration = end-start
print(duration)


##################  <PART B>    #################
def IsPrime_dumb(n):
	if n<2:
		return False
	for factor in range(2,n):
		if n%factor ==0:
			return False
	return True


def IsPrime_better(n):
	if n<2:
	    return False
	if n==2:
            return True
        if n%2==0:
            return False
	for factor in range(3,n,2):
            if n%factor==0:
                return False
        return True

def IsPrime_best(n):
	if n<2:
	    return False
	if n==2:
            return True
        if n%2==0:
            return False
	maxfactor = round(n**0.5)
	for factor in range(3,maxfactor+1,2):
            if n%factor==0:
                return False
        return True

###################################################

import time
start = time.clock()
for i in range(1,100):
	if IsPrime_dumb(i):
		print(i)
end = time.clock()
duration = end-start
print(duration)

###################################################

import time
start = time.clock()
for i in range(1,100):
	if IsPrime_better(i):
		print(i)
end = time.clock()
duration = end-start
print(duration)

###################################################

import time
start = time.clock()
for i in range(1,100):
	if IsPrime_best(i):
		print(i)
end = time.clock()
duration = end-start

print(duration)
