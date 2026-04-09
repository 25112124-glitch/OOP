class SieuNhan():
    __ten = str()
    __vu_khi = str()
    __mau_sac = str()
    def thong_tin_A(self):
        return self.__ten
    def thong_tin_B(self):
        return self.__vu_khi
    def thong_tin_C(self):
        return self.__mau_sac
    def nhap_thong_tin(self, tengoi):
        self.__ten = input("Nhập tên " + tengoi + ": ")
        self.__vu_khi = input("Nhập vũ khí của " + tengoi + ": ")
        self.__mau_sac = input("Nhập màu sắc của " + tengoi + ": ")
    def hien_thi_thong_tin(self):
        print("Tên:", self.__ten)
        print("Vũ khí:", self.__vu_khi)
        print("Màu sắc:", self.__mau_sac)

sieu_nhan_A = SieuNhan()
sieu_nhan_A.nhap_thong_tin("Sieu nhân A")
sieu_nhan_B = SieuNhan()
sieu_nhan_B.nhap_thong_tin("Sieu nhân B")
sieu_nhan_A.hien_thi_thong_tin()
sieu_nhan_B.hien_thi_thong_tin()

