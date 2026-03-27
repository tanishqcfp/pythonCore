#sort
listt = list(map(int,input("enter a number").split()))
# 5,2,9,1
n = len(listt)

for i in range(n):
    for j in range(n-i-1):
        if listt[j] < listt[j+1]:
            listt[j],listt[j+1] = listt[j+1],listt[j]

# print(listt)

# partial sort
k=1
for i in range(k+1):
    for j in range(0,k-i):
        if listt[j] > listt[j+1]:
            listt[j],listt[j+1] = listt[j+1],listt[j]

print(listt)


