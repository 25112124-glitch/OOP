import math
class point():
    __x = int
    __y = int
    def diem_x(self):
        return self.__x
    def diem_y(self):
        return self.__y
    def hien_thi(self):
        print("Toa do diem la: (", self.__x, ",", self.__y, ")")
    def luu_diem(self, x, y):
        self.__x = x
        self.__y = y
    def tao_diem(self,ten):
        self.__x = int(input("Nhap x: "))
        self.__y = int(input("Nhap y: "))
        print("Diem ", ten, " la: (", self.__x, ",", self.__y, ")")
    def diem_doi(self,ten):
        print("Toa do diem ", ten, " la: (", self.__x, ",", self.__y, ")")
    def tinh_khoang_cach_den_O(self, ten):
        khoang_cach_den_O=math.sqrt(self.__x**2 + self.__y**2)
        print("Khoang cach tu diem ", ten, " den O la: ", '{:.2f}'.format(khoang_cach_den_O))
    def tinh_khoang_cach__tu_A_den_B(self, A, B):
        khoang_cach_AB=math.sqrt((A.diem_x()-B.diem_x())**2 + (A.diem_y()-B.diem_y())**2)
        print("Khoang cach tu diem A den diem B la: ", '{:.2f}'.format(khoang_cach_AB))

A = point()
A.luu_diem(3, 5)
A.hien_thi()
B = point()
B.tao_diem("B")
C = point()
C.luu_diem(B.diem_x()*(-1), B.diem_y()*(-1))
C.diem_doi("C")
B.tinh_khoang_cach_den_O("B")
A.tinh_khoang_cach__tu_A_den_B(A, B)
