a = [1,2]
b = a
b[1] = 3

print(a)
print(b) #both changes cz list is mutable and can change 

a = 10
b = a
b = 20

print(a)
print(b) # only b changes a will remain same as int is immutable in nature