#Ch4-a_(Daehwan)_18-06-22

#1.
def f1_odd(L):
	count = 0
	for i in L:
		if i%2 ==1:
			count = count+1
	print(count)

def f1_even(L):
	  count = 0
	  for i in L:
		  if i%2==0:
			  count = count +1
	  print(count)


#2.
def f2_o(L):
	for i in L:
		if i%2 ==1:
			print(i)

def f2_e(L):
	for i in L:
		if i%2 ==0:
			print(i)

#3.
def f3_o(L):
	sum = 0
	for i in L:
		if i%2 ==1:
			sum = sum +i
	print(sum)

def f3_e(L):
	sum = 0
	for i in L:
		if i%2 ==0:
			sum = sum +i
	print(sum)

#4.
def f4(lst):
        c = len(lst)
        sum = 0
        for i in range(0,c):
                if lst[i]%2==1:
                        sum = sum + i
        return sum



#5.
def f5(lst):
	  for i in range(0,len(lst)):
		  lst[i] = lst[i] **2
	  return lst
	
#6.
def f6(lst):
	  C = len(lst)
	  maxx = lst[0]
	  for i in range(1,C):
		  if lst[i] > maxx:
			  maxx = lst[i]
	  return maxx
#7.
def f7(lst):
        sum = 0
        count = 0
        c=len(lst)
        for i in range(0,c):
                sum = sum + lst[i]
                count = count + 1
        return(sum/count)
	

#8.
def f8(a,b,n):
	  for i in range(a,b+1):
		  if i%n ==0:
			  print(i)

#9.
def f9(w,h):
	  for i in range(h+1):
		  print('*'*w)

#10.
def f10(n):
	  for i in range(1,n+1):
		  print('*'*i)

#11.
def f11(lst):
	  c =len(lst)-1
	  for i in range(0,c):
		  if lst[i]>lst[i+1]:
			  resul = True
		  else:
			  resul = False
			  break
			
	  return resul

#12.
def f12(lst):
	  c =len(lst)-1
	  for i in range(0,c):
		  if lst[i] < 0:
			  resul = True
		  elif lst[i] >=0:
			  resul = False
			  break
	  return resul

#13.
def f13(lst,tar):
	c = len(lst)
	for i in range(c-1,-1,-1):
		if lst[i]==tar:
			return i
			break
#14.
def f14(lst):
	  c = len(lst)
	  for i in range(o,c):
		  if lst[i] < 0 :
			  resul = lst[i]
		  else:
			  resul = 0
	  return resul
#15.
def f15(lst):
	c = len(lst)
	sum = 0
	for i in range(0,c,2):
		sum = sum + lst[i]
	return sum
#16.
def f16(n):
	for i in range(n,0,-1):
		print('*'*i)

#17.
def f17(lst):
	c = len(lst)
	for i in range(c-1,-1,-2):
		a = lst[i]
		print(a)

#18.
def f18(n):
	fac = 1
	for i in range(n,0,-1):
		fac = fac * i
	return fac

#19.
def f19(lst):
	c = len(lst)
	for i in range(0,c):
		print(f18(lst[i]))

#20.
def f20(lst):
	c = len(lst)
	for i in range(0,c):
		for j in range(lst[i],-1,-1):
			print(j,end='')
			if j ==0:
				print()

#21.
def f21(lst1,lst2):
	c = len(lst1)
	d=[]
	for i in range(0,c):
		d.append(lst1[i]+lst2[i])
	print(d)

#22.
def f22(n):
	for i in range(1,n+1):
		if i%2==0 or i%3==0:
		      print(i)

#23.
def f23(lst):
	c = len(lst)
	max = lst[0][0]
	for i in range(0,c):
		d = len(lst[i])
		for j in range(0,d):
			if lst[i][j] > max:
				max = lst[i][j]
	return max

#24.
def f24(lst):
	c = len(lst)
	for i in range(0,c-1):
		for j in range(0,c-1):
			if lst[j] < lst[j+1]:
				lst[j],lst[j+1] = lst[j+1],lst[j]
				
	print(lst[1])

#25.
def f25(n):
	if n < 10:
		return n
	else:
		while n !=0:
			n = n //10
			if n // 10 < 1:
				break
		return n


#26.
def f26_max(lst):
        c = len(lst)
	max = lst[0]
	for i in range(0,c):
		if max <=lst[i]:
		      max = lst[i]
	return max

def f26(lst):
	c = len(lst)
	for i in range(0,c):
		a = f26_max(lst[i])
		print(a)
