n = 23
count = 0
i=1
for i in range (1,n):
    if n%i == 0:
        count+=1

if count > 2:
    print("Not a Prime")
else:
    print("Prime")
