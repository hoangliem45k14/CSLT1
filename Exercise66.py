# Vì không tìm thấy nội dung bài 51 nên nhóm em xin quy đổi điểm theo bảng điểm đại học DUE
Dem=0
S=0
while True:
    DiemChu=input('Nhập điểm chữ (để trống để kết thúc): ')
    if not DiemChu:
        break
    DiemChu_DiemSo={'A+': 4.0, 'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F': 0.0}
    DiemSo=DiemChu_DiemSo.get(DiemChu, 0.0)
    Dem+=1
    S+=DiemSo
if Dem==0:
    print('Không có điểm nào được nhập')
else:
    print('Điểm trung bình là:',round(S/Dem,1))