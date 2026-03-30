# Frequency Count
lst = [1,1,2,3,4,4]

freq = {}

for num in lst:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)

# Find Duplicates
lst = [1,2,2,3,1]

freq = {}

for num in lst:
    freq[num] = freq.get(num,0)+1


for k,v in freq.items():
    if freq.get(k) > 1:
        print(k)

#first repeating number
lst = [1,2,2,3,1]

seen = set()

for num in lst:
    if num in seen:
        print(num)
        break
    seen.add(num)

#reverse dict
d = {"a": 1, "b": 2}

rev = {}

for k, v in d.items():
    rev[v] = k

print(rev)