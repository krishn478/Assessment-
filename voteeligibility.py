a = input("enter name:")
b = int(input("enter age:"))
if b >= 18 :
    if  b >= 200:
        print("you are dead")
    elif b >= 18 & b < 200 :
        print("your are elgible to vote")
else:
    c = b - 18
    print("How many years left to vote is:", c)
    print("you are not ready to vote")
