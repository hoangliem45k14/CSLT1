pi=3
Dau=1
print(float(pi))
for Nhan in range(2,29,2):
    SoChia=Nhan*(Nhan+1)*(Nhan+2)
    pi=pi+Dau*(4/SoChia)
    Dau=Dau*-1
    print(pi)