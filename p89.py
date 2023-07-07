try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)

except:
    print("an errot occured ZeroDivisonError")

else:
    print("noo error in the code")


finally:
    print("this is an Exmape of exception handleing")
