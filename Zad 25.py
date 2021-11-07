a=int(input("Wprowadź a:"))
b=int(input("Wprowadź b:"))
for i in range (1,a+1):
    sign=""
    for x in range (1,b+1):
        if i==1 or x==1 or i==a or x==b:
            sign = sign +"*"
        else:
            sign =sign+" "
    print(sign)
    
