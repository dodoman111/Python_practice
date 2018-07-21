hw_team1_2_DaeHwan_2018-06-30

#1
def f1(n):
	for i in range(n):
		for j in range(i+1):
			print(j+1,end='')
		print('')

#2
def f2(n):
	count = 1
	for i in range(n):
	   for j in range(i+1):
		   print(count, end='')
		   count = count+1
	   print("")

#3
def f3(n):
        resul =[]
        count = 0
        for i in range(1,n+1):
                a=[]
                for j in range(1,i+1):
                        count = count+1
                        a += [count]
                resul += [a]
                
        for i in range(n-2,-1,-1):
                resul += [resul[i]]
        
        for i in range(0,len(resul)):
                for j in range(0,len(resul[i])):
                        print(resul[i][j], end='')
                print('')
                
#4
def f4(n):
    count =0
    an = 0
    for i in range(1,2*n):
            if i <= n:  
                    for j in range(1,i+1):
                            count = count +1
                            print(count,end='')
            else:
                    an += 1
                    for k in range(1,n-an+1):
                            count = count+1
                            print(count,end='')
            print('')
		
#5
def f5(matrix):
    for row in matrix:
        sum = 0
        for ele in row:
            sum = sum + ele
        print(sum)
		   
#6
def f6(matrix):
    for row in range(len(matrix)):
        for col in range(len(row)):
            if row == col:
                print(matrix[row][col])

#7
def f7(matrix):
    for i in range(len(matrix)):
        sum=0
        for j in range(len(matrix[i])):
            sum = sum+matrix[i][j]
        print(sum)

#8
def f8(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum = sum+matrix[i][j]
    return sum

#9
def f9(mat):
    row = len(mat)
    total = 1
    for i in range(row):
        for j in range(len(mat[i])):
            total = total*mat[i][j]
    return total
	
#10
def f10(mat):
    for row in mat:
        for col in row:
            if col%2 == 1:
                print(col,end='')
        print('')
        
#11
def f11(mat1,mat2):
    a=[]
    r1 = len(mat1)
    for i in range(r1):
        c1 = len(mat1[i])
        resul=[]
        for j in range(c1):
            resul += [mat1[i][j]+mat2[i][j]]
        a.append(resul)
    return a

#12
def f12(mat1,mat2):
    mat1_row = len(mat1)
    mat1_col = len(mat1[0])
    mat2_row = len(mat2[0]) 
    mat2_col = len(mat2[0])
    a=[]
    for i in range(mat1_row):
        result =[]
        for k in range(mat2_col):
            sum = 0
            for j in range(mat1_col):
                sum += (mat1[i][j]*mat2[j][k])
            result +=[sum]
        a.append(result)
    return a

#13
def f13(mat):
    row = len(mat)
    col = len(mat[0])
    for i in range(row):
        for j in range(col):
            if i==j:
                if mat[i][i] ==1:
                    result = True
                else: return False
            else:
                if mat[i][j]==0:
                    result = True
                else: return False
    return result

#14
def f14(rows,cols):
    prime =[]
    for i in range(rows):
        a = []
        for j in range(cols):
            a +=[1]
        prime +=[a]
        
    for i in range(rows):
        for j in range(cols):
            count = 0
            if i <rows-1 and prime[i+1][j]:
                count += 1
            if 0<i and prime[i-1][j]:
                 count += 1
            if j<cols-1 and prime[i][j+1]:
                count += 1
            if j>0 and prime[i][j-1]:
                count += 1
            prime[i][j] = count
    return prime
