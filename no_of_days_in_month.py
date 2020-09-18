a = int(input())

if a in range(1,8):
    if a==2:
        print("28")
    elif a%2==0:
        print("30")
    else:
        print("31")
    
elif a in range(8,13):
    if a%2==0:
        print("31")
    else:
        print("30")

else:
    print("Error")
    
    
