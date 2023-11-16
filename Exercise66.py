Dem=0
S=0
while True:
    DiemChu=input('Nhập điểm chữ (để trống để kết thúc): ')
    if not DiemChu:
        break
    DiemChu_DiemSo={'A+': 4.0, 'A': 4.0, 'A-': 3.7,'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0}
    DiemSo=DiemChu_DiemSo.get(DiemChu, 0.0)
    Dem+=1
    S+=DiemSo
if Dem==0:
    print('Không có điểm nào được nhập')
else:
    print('Điểm trung bình là:',round(S/Dem,1))
