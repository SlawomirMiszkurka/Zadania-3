x=int(input("Podaj kwotę w PLN: "))
kwota=x
pięć=0
dwa=0
jeden=0
while x>0:
    if x>=5:
        pięć=pięć+1
        x=x-5
    elif x>=2:
        dwa=dwa+1
        x=x-2
    elif x>=1:
        jeden=jeden+1
        x=x-1
print(f"Kwota {kwota} w bilonie:")
print(f"5zł - {pięć}szt.")
print(f"2zł - {dwa}szt.")
print(f"1zł - {jeden}szt.")