#2x+3y=18
#5x+1y=19
#x=3,y=4



# a1,b1,c1,a2,b2,c2 = map(int,input().split())
# det = a1*b2 - b1*a2
# if det==0:
#     print("Lines are parallel")
# else:
#     x = (c1*b2 - b1*c2)/det
#     y = (a1*c2 - c1*a2)/det
#     print("Solution is x={} and y={}".format(x,y))

# a1,b1,c1,a2,b2,c2 = map(int,input().split())
# b1 = b1*a2
# c1 = c1*a2
# b2 = b2*a1
# c2 = c2*a1
# a1 = a1*a2
# a2 = a1
# if b1-b2==0:
#     print("The lines are parallel")
# else:
#     y = (c1-c2)/(b1-b2)
#     x = (c1 - b1*y)/(a1)
#     print("Solution is x={} and y={}".format(x,y))

#10x+15y=90
#10x+2y=38
#x=3,y=4


# import numpy as np
# a = np.zeros((2,3))
# x = np.zeros(2)
# for i in range(2):#taking input of augmented matrix
#     for j in range(3):
#         a[i][j] = float(input())
# rat = a[1][0]/a[0][0]
# for k in range(3):
#     a[1][k]-=(rat*a[0][k])
# x[1] = a[1][2]/a[1][1]#finding the last variable because in matrix that can be caluclated only
# x[0] = (a[0][2]-x[1]*a[0][1])/a[0][0]
# print('\nSolution : %f and %f' %(x[0],x[1]))

import numpy as np
a = np.zeros((2,3))
x = np.zeros(2)
for i in range(2):#taking input of augmented matrix
    for j in range(3):
        a[i][j] = float(input())
rat1 = a[1][0]/a[0][0]
for k in range(3):
    a[1][k]-=(rat1*a[0][k])
rat2 = a[0][1]/a[1][1]
for k in range(3):
    a[0][k]-=(rat2*a[1][k])
x[1] = a[1][2]/a[1][1]
x[0] = a[0][2]/a[0][0]
print('\nSolution : %f and %f' %(x[0],x[1]))