s=0
while True:
    Gia=input('Nhập giá (hoặc bỏ trống để kết thúc):')
    if not Gia:
        break
    floatGia=float(Gia)
    SoTien=floatGia*100
    SoDu=SoTien%5
    if SoDu<2.5:
        SoTien=SoTien-SoDu 
    else:
        SoTien=SoTien+(5-SoDu)
    s=s+SoTien
print('So tien phai thanh toan bang tien mat:',s)