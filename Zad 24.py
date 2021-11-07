a=0
for i in range(1,10):
    a=a+1
    if i>5:
        a=a-2
    sign=""
    for y in range(1,a+1):
        sign=sign+" *"
    print(sign)