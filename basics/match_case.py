# x = 50

# match x:
#     case 1:
#         print("one")
#     case 2:
#         print("two")
#     case 3:
#         print("three")
#     case 5:
#         print("ans")
#     case _:
#         print("default case")

marks = int(input("enter a number."))

if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")
