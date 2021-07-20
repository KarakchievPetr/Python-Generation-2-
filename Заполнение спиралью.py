# put your python code here
s = input().split()
n, m = int(s[0]), int(s[1])
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append("0")

s = 0
n1, n2, n3, n4 = 0, 0 ,0 ,0
flag1 =0 
while s < m*n:
    if flag1 == 0:
        for i1 in range(n1,m-n1-1):
            s+=1
            matrix[n1][i1] =str(s).ljust(3)
        flag1 = 1
        n1+=1
    elif flag1 == 1:
        for i2 in range(n2,n-n2-1):
            s+=1
            matrix[i2][m-n2-1] =str(s).ljust(3)
            if s>= m*n:
                break
        flag1 = 2
        n2+=1 
    elif flag1 == 2:
        for i3 in range(m-n3-1,n3,-1):
            s+=1
            matrix[n-n3-1][i3] =str(s).ljust(3)
        flag1 = 3
        n3+=1

    elif flag1 == 3:
        for i4 in range(n-n4-1,n4,-1):
            s+=1
            matrix[i4][n4] =str(s).ljust(3)

        flag1 = 0
        n4+=1
    print(s)
for i in matrix:
    print(" ".join(i))         