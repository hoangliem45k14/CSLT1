Nhap = input("Nhap vao 8 bit:(Nhan enter de ket thuc) ")
while Nhap != "":
    if Nhap.count("0") + Nhap.count("1") !=8 or len(Nhap) !=8:
        print("Day khong phai la day 8 bit, hay thu lai")
    else:
        kiemtra = Nhap.count("1")
        if kiemtra % 2 == 0:
            print("Bit chan le nen la 0")
        else:
            print("Bit chan le nen la 1")
    Nhap = input("Nhap vao 8 bit:(Nhan enter de ket thuc) ")