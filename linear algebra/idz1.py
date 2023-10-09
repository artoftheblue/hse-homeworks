import numpy as np

def tr(item):
    return int(item.trace())

def t(item):
    return item.transpose()

A = np.matrix([[-5, 4, 3],
               [0, 0, 6]])
B = np.matrix([[-5, 3, -4],
               [-5, 1, 7]])
C = np.matrix([[4, 4],
               [4, 5]])
D = np.matrix([[4, 0],
               [0, 9]])

A_T = t(A)
B_T = t(B)
tr1_1 = A_T * A
tr1 = tr(tr1_1)
DB = D * B
DBBT = DB * B_T
s1 = tr1 * DBBT
BA_T = B * A_T
AB_T = A * B_T
BAABT = 7 * BA_T + 7 * AB_T
tr2_1 = BAABT * D
ABBAT = -7 * AB_T + 4 * BA_T
tr2_2 = D * ABBAT
tr2 = tr(tr2_1 + tr2_2)
AandB = A + B
ATminusBT = A_T - B_T
AAA = (AandB) * (ATminusBT)
s2 = tr2 * AAA
C2 = C * C
CD = C * D
D2 = D * D
s3 = -9 * C2 - 18 * CD - 9 * D2
final = s1 + s2 + s3

data = [A_T, B_T, tr1_1, tr1, DB, DBBT, s1, BA_T, AB_T, BAABT, tr2_1,
             ABBAT, tr2_2, tr2, AandB, ATminusBT, AAA, s2, C2,
             CD, D2, s3, final]
string = '''A_T, B_T, tr1_1, tr1, DB, DBBT, s1, BA_T, AB_T, BAABT, tr2_1, ABBAT, tr2_2, tr2, AandB, ATminusBT, AAA, s2, C2, CD, D2, s3, final'''.split(", ")

#for i in range(len(data)):
#    print(f"{string[i]}=\n{data[i]}\n")


C = np.matrix([[1, 8, -8],
               [0, 1, -8],
               [0, 0, 1]],dtype=object)
J = np.matrix([[-1, 1, 0],
               [0, -1, 1],
               [0, 0, -1]],dtype=object)
D = np.matrix([[1, -8, -56,],
               [0, 1, 8],
               [0, 0, 1]],dtype=object)
A = C * J * D
prev = np.matrix([[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]],dtype=object)
for i in range(1,2023):
    prev += J ** i
print(prev)

A_ = [[-60, -9, -25, 18],[-9,-58,12, 21],[-25, 12,-8,-12],[18,21,-12,10]]
B = [[0, 19, -11, -10],[-19, 0, 30, -31],[11, -30, 0, 42],[-10, 31, -42, 0]]
B = [[1, 8, -8],[0, 1, -8],[0,0,1]]
A = [[1, -8,-56],[0,1,8],[0,0,1]]

C = [[1, 8, -8],[0, 1, -8],[0, 0, 1]]
D = [[1, -8, -56],[0, 1, 8],[0, 0, 1]]
J = [[1, -1011, 1022121],[0,1,-1011],[0,0,1]]
print(np.matrix(C)*np.matrix(J))
leng = 3
for i in range(leng):
    temp = ""
    for j in range(leng):
        temp2 = ""
        for k in range(leng):
            temp2 += f"{C[i][k]}*{J[k][j]}+"
        temp2 += "&"
        temp += temp2
    temp += "\\\\\n"
        
    print(temp)
            
