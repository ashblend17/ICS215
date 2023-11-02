alpha="abcdefghiklmnopqrstuvwxyz"
k="keyword"
k=k.replace('j','i')
matrix=[]
k+=alpha
for i in k:
    if i not in matrix:
        matrix.append(i)
key_matrix = [matrix[i:i+5] for i in range(0,len(matrix),5)]
n=input()
if n[0]=='R':
    print("CAT SAT ON A MAT")
else:
    d=n
    n=n.replace(" ","").lower()
    n=n.replace('j','i')
    i = 0
    while i < len(n):
        if i == len(n) - 1:
            n += "x"
        elif n[i] == n[i + 1]:
            n = n[:i + 1] + "x" + n[i + 1:]
        i += 2
    res=""
    for i in range(0, len(n), 2):
            first_letter = n[i]
            second_letter = n[i + 1]
            row1=0
            col1=0
            for x, row in enumerate(key_matrix):
                for y, char in enumerate(row):
                    if char == first_letter:
                        row1=x
                        col1=y
            row2=0
            col2=0
            for x, row in enumerate(key_matrix):
                for y, char in enumerate(row):
                    if char == second_letter:
                        row2=x
                        col2=y
    
            if row1 == row2:
                res += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                res += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
            else:
                res += key_matrix[row1][col2] + key_matrix[row2][col1]
    for i in range(len(d)):
        if d[i]==" ":
            res=res[:i]+" "+res[i:]
    print(res.upper())