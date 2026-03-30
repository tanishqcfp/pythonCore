#sort
# listt = list(map(int,input("enter a number").split()))
# 5,2,9,1
# n = len(listt)

# for i in range(n):
#     for j in range(n-i-1):
#         if listt[j] < listt[j+1]:
#             listt[j],listt[j+1] = listt[j+1],listt[j]

# # print(listt)

# # partial sort
# k=1
# for i in range(k+1):
#     for j in range(0,k-i):
#         if listt[j] > listt[j+1]:
#             listt[j],listt[j+1] = listt[j+1],listt[j]

# print(listt)


#remove duplicate
lst = [1,2,2,3,1]

res = []

for num in lst:
    found = False
    for x in res:
        if x == num:
            found = True
            break
    if not found:
        res.append(num)
print(res)

#second largest
lst = [10, 20, 4, 45, 99]

first = second = float('-inf')

for num in lst:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print(second)

#move zero to end
lst = [0, 1, 0, 3, 12]

res = []

for num in lst:
    if num != 0:
        res.append(num)

for num in lst:
    if num == 0:
        res.append(num)

print(res)

#first non repeating
lst = [4, 5, 1, 2, 0, 4]

freq = {}

for num in lst:
    freq[num] = freq.get(num, 0) + 1

for num in lst:
    if freq[num] == 1:
        print(num)
        break