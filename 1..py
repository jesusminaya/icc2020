true=false=0
texto=input("Ingrese: ")
for i in range(len(texto)-1,-1,-1):
    if texto[i] == texto[len(texto)-1-i]:
        true+=1
    else:
        false+=1
if true> false:
    print("True")
else:
    print("False")