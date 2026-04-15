class canbo:
    def __init__(self, ho_ten: str, tuoi: int, gioi_tinh: str, dia_chi: str):
        self.__hoten = ho_ten
        self.__do_tuoi = tuoi
        self.__gioitinh = gioi_tinh
        self.__diachi = dia_chi
    def get_thong_tin (self):
        return f"Họ và tên: {self.__hoten} \nTuổi: {self.__do_tuoi} \nGiới tính: {self.__gioitinh} \nĐịa chỉ: {self.__diachi}"

class congnhan (canbo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac: int):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__cap_bac = bac
    def get_thong_tin(self):
        thong_tin_chung_1 = super().get_thong_tin()
        return f"{thong_tin_chung_1} \nBậc: {self.__cap_bac}"
    
class kysu (canbo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao: str):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh = nganh_dao_tao
    def get_thong_tin(self):
        thong_tin_chung_2 = super().get_thong_tin()
        return f"{thong_tin_chung_2} \nNgành đào tạo: {self.__nganh}"

class nhanvien (canbo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec: str):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__congviec = cong_viec
    def get_thong_tin(self):
        thong_tin_chung_3 = super().get_thong_tin()
        return f"{thong_tin_chung_3} \nCông việc: {self.__congviec}"

class quan_ly_can_bo():
    def __init__(self):
        self.danhsach = []
    def them_can_bo (self):
        ho_ten = input("Nhập vào họ tên: ")
        tuoi = int (input("Nhập vào độ tuổi: "))
        gioi_tinh = input("Nhập giới tính: ")
        dia_chi = input ("Nhập địa chỉ: ")
        print ("1. Kỹ sư \n2. Công nhân \n3. Nhân viên ")
        can_bo = int ( input ("Nhập vào chức vụ cán bộ (1-3): "))
        if can_bo == 1:
            new_ky_su = kysu(ho_ten, tuoi, gioi_tinh, dia_chi, input ("Nhập vào ngành đào tạo: "))
            self.danhsach.append(new_ky_su)
            print ("===============")
            print(new_ky_su.get_thong_tin())
            print("Thêm cán bộ thành công!!")
        elif can_bo == 2:
            new_cong_nhan = congnhan(ho_ten, tuoi, gioi_tinh, dia_chi, input ("Nhập bậc: "))
            self.danhsach.append(new_cong_nhan)
            print ("===============")
            print(new_cong_nhan.get_thong_tin())
            print("Thêm cán bộ thành công!!")
        elif can_bo == 3:
            new_nhan_vien = nhanvien(ho_ten, tuoi, gioi_tinh, dia_chi, input ("nhập công việc: "))
            self.danhsach.append(new_nhan_vien)
            print ("===============")
            print(new_nhan_vien.get_thong_tin())
            print("Thêm cán bộ thành công!!")
    def tim_kiem (self):
        doi_tuong_can_tim = str(input("Nhập vào họ tên cán bộ cần tìm: "))
        for cb in self.danhsach:
            if doi_tuong_can_tim == cb._canbo__hoten:
                print ("============")
                print(cb.get_thong_tin())
                return 
    
    def hien_thi_danh_sach (self):
        print ("======DANH SÁCH======")
        if not self.danhsach:
            print("Danh sách trống!!")
            return
        for cb in self.danhsach:
            print ("============")
            print(cb.get_thong_tin())
    

ql = quan_ly_can_bo()
while True: 
    print ("========MENU========")
    print ("1. Thêm cán bộ")
    print ("2. Tìm kiếm theo họ tên")
    print ("3. Hiển thị danh sách")
    print ("4. Exit")
    choice = int(input("Nhập vào lựa chọn (1-4): "))
    if choice == 1:
        ql.them_can_bo()
    elif choice == 2:
        ql.tim_kiem()
    elif choice == 3:
        ql.hien_thi_danh_sach()
    elif choice == 4:
        print("Đang thoát...")
        break

