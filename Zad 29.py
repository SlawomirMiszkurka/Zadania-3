a=int(input("Enter number: "))
QT=0
SUM=0
MEAN=0
while a!=0:
    SUM=SUM+a
    QT=QT+1
    a=int(input("Enter number: "))
MEAN=SUM/QT
print(f"RESULT: Quantity={QT}, Sum={SUM}, Mean={MEAN}")