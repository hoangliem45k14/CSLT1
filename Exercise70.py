
thongbao=str(input("Vui long nhap thong bao can ma hoa: "))
KhoaK=int(input("Nhap khoang cach dich chuyen cac chu cai\n(Nhap so duong de dich sang trai, so am de dich sang phai): ")) 
ketqua=""
for chucai in thongbao:
    if chucai >="a" and chucai <= "z":
        
        pos=ord(chucai)-ord("a")
        pos=(pos+KhoaK) %26                    
        chucaimoi=chr(pos + ord('a'))
        ketqua = ketqua+ chucaimoi
    elif chucai >="A" and chucai <= "Z":
        
        pos=ord(chucai)-ord("A")
        pos=(pos+KhoaK) %26                     
        chucaimoi=chr(pos + ord('A'))
        ketqua = ketqua+chucaimoi
        
    else:
        ketqua = ketqua+ chucai
print ("Ma hoa Caesar la:", ketqua)