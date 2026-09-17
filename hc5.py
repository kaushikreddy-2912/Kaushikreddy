n = int(input())
if n%2 != 0:
    print("weird")
elif n%2==0 and 2<=n<=5 :
    print("Not Weird")
elif n%2==0 and 6<=n<=20 :
    print("weird")
elif n%2==0 and n>20:
    print("Not Weird")
else :
    print("Invalid number")