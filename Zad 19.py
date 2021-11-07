wiek=int(input("Podaj wiek psa:"))
psie=0
for y in range(1,wiek+1):
    if y<=2:
        psie=psie+10.5
    else:
        psie=psie+4
print(f"Pies ma {psie} w psich latach")