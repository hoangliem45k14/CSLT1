Duoi2 = 0.00
Tu3den12 = 14.00
Khachkhac = 23.00
Tu65trolen = 18.00

Gioihan1 = 2
Gioihan2 = 12
Gioihan3 = 64

Tong = 0

Nhap = input("Nhap vao tuoi cua khach (De trong de ket thuc): ")
while Nhap != "":
    Tuoi = int(Nhap)
    if Tuoi <= Gioihan1:
        Tong = Tong + Duoi2
    elif Tuoi <= Gioihan2:
        Tong = Tong + Tu3den12
    elif Tuoi <= Gioihan3:
        Tong = Tong + Khachkhac
    else:
        Tong = Tong + Tu65trolen
    Nhap = input("Nhap vao tuoi cua khach (De trong de ket thuc): ")
print("Tong tien cua nhom do la $",Tong,sep='')