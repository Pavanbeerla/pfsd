a=[1,2,3,4]
try:
    print(a[1])
    print(a[4])

except:
     print("check the array bounds")


else:
    print("there is no error")

finally:
    print("this is finally block")
