class NhanVien():
    Luong_MAX = 50_000_000
    def __init__(self, ten_nhan_vien: str, luong_co_ban: float, he_so_luong: float):
        self.__tennhanvien = ten_nhan_vien
        self.__luongcoban = luong_co_ban
        self.__hesoluong = he_so_luong
        
    def get_tennhanvien (self):
        return self.__tennhanvien
    def get_luongcoban (self):
        return self.__luongcoban
    def get_hesoluong (self):
        return self.__hesoluong
    def in_thong_tin (self):
        print ("THÔNG TIN NHÂN VIÊN:")
        print ("Họ và tên nhân viên: ", self.__tennhanvien)
        print ("Lương cơ bản của nhân viên: ", self.__luongcoban)
        print ("Hệ số lương:", self.__hesoluong)
        print ("Lương của nhân viên:", self.__luongcoban * self.__hesoluong)
    def Tang_luong (self):
        he_so_tang = float(input("Nhập vào mức tăng hệ số:"))
        luong_tang = (self.__hesoluong + he_so_tang) * self.__luongcoban
        if (luong_tang > self.Luong_MAX):
            print ("Vượt quá mức lương cho phép! Không tăng!!")
            return False
        elif (luong_tang <= self.Luong_MAX):
            print ("THÔNG TIN NHÂN VIÊN:")
            print ("Họ và tên nhân viên: ", self.__tennhanvien)
            print ("Lương cơ bản của nhân viên: ", self.__luongcoban)
            print ("Hệ số lương:", self.__hesoluong)
            print ("Lương của nhân viên:", luong_tang)
            print("Lương đã được tăng!!")
            return True


nhanvien1 = NhanVien("Lại Minh Vũ", 2_000_000, 3.5)
nhanvien1.in_thong_tin()
nhanvien1.Tang_luong()



    
