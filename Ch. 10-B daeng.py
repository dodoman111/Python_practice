Ch.10-B
#1
def f1(n):
    for i in range(1,n+1):
        print(*list(range(1,i+1)))

#2
def f2(n):
    for i in range(1,n+1):
        print(*list(range(int((i-1)*i/2+1),int(i*(i+1)/2+1))))

#3
def f3(n):
    for i in range(1,n+1):
        print(*list(range(int((i-1)*i/2+1),int(i*(i+1)/2+1))))
    for i in range(n+1,0,-1):
        print(*list(range(int((i-1)*i/2+1),int(i*(i+1)/2+1))))

#4  
def f4(n):
    count = 0
    for i in range(1,n+1):
        count += 1
        print(*list(range(count, count+i)))
        count = count+i-1
    for i in range(n-1,0,-1):
        count +=1
        print(*list(range(count, count+i)))
        count = count+i-1

#5
def f5(mat):
    for i in range(0,len(mat)):
        print(sum(mat[i]))

#6
def f6(mat):
    return sum(map(sum,mat))


#7           더  생각해보자
def f7(mat):
    cart =1
    for i in mat:
        for j in i:
            cart *= j
    print(cart)

#8
def f8(mat):
    for i in mat:
        print(*list(filter(lambda x : x%2==1, i)))

#9          더  생각해보자
def f9(mat1,mat2):
    a=[]
    r1 = len(mat1)
    for i in range(r1):
        c1 = len(mat1[i])
        resul=[]
        for j in range(c1):
            resul += [mat1[i][j]+mat2[i][j]]
        a.append(resul)
    return a

#10         더  생각해보자
def f10(mat1,mat2):
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

#11
def f11(mat):
    for i,v in enumerate(mat):
        for i2,v2 in enumerate(v):
            if i == i2:
                if v2 !=1:
                    return False
            elif v2 !=0:
                return False
    return True

#12         더  생각해보자
def f12(rows,cols):
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



