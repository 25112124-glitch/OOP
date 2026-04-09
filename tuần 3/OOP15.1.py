import math
class point():
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def input_point(self):
        self.x = int(input("nhap x: "))
        self.y = int(input("nhap y: "))
    def hien_thi(self):
        print(f"({self.x}, {self.y})")
class circle():
    def __init__(self,center: point):
        self.center = center
        self.radius = int(input("nhap ban kinh: "))
    def point_in_circle(self,point):
        khoang_cach = math.sqrt((point.x - self.center.x)**2 + (point.y - self.center.y)**2)
        if khoang_cach <= self.radius:
            return True
        else:
            return False
class rectangle():
        def __init__(self):
            self.top_left = point()
            self.top_left.input_point()
            self.wide = int(input("nhap chieu rong: "))
            self.height = int(input("nhap chieu cao: "))
        def rect_in_circle(self,circle: circle):
            top_right = point(self.top_left.x + self.wide, self.top_left.y)
            bottom_left = point(self.top_left.x, self.top_left.y - self.height)
            bottom_right = point(self.top_left.x + self.wide, self.top_left.y - self.height)
            if (circle.point_in_circle(top_right) and 
                circle.point_in_circle(bottom_left) and 
                circle.point_in_circle(bottom_right)):
                print("Hình chữ nhật nằm hoàn toàn trong đường tròn")
            else:
                print("Hình chữ nhật không nằm hoàn toàn trong đường tròn")
        
        def rect_in_circle_overlap(self, circle: circle):
            top_right = point(self.top_left.x + self.wide, self.top_left.y)
            bottom_left = point(self.top_left.x, self.top_left.y - self.height)
            bottom_right = point(self.top_left.x + self.wide, self.top_left.y - self.height)
            if (circle.point_in_circle(top_right) or 
                circle.point_in_circle(bottom_left) or 
                circle.point_in_circle(bottom_right)):
                print("Hình chữ nhật chồng lấn với đường tròn")
            else:
                print("Hình chữ nhật không chồng lấn với đường tròn")

def menu():
    mycircle = []
    while True:
        print("1. Create a circle ")
        print("2. Point in circle")
        print("3. Rectangle in circle")
        print("4. Rect_in_circle_overlap")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            center = point()
            center.input_point()
            new_circle = circle(center)
            mycircle.append(new_circle)
        elif choice == 2:
            point1 = point()
            point1.input_point()
            latest_circle = mycircle[-1]  
            if latest_circle.point_in_circle(point1):
                print("Điểm nằm trong đường tròn")
            else:
                print("Điểm không nằm trong đường tròn")
        elif choice == 3:
            rect1 = rectangle()
            rect1.rect_in_circle(latest_circle)
        elif choice == 4:
            another_point = point()
            another_point.input_point()
            another_circle = circle(another_point)
            mycircle.append(another_circle)
            new_rect = rectangle()
            new_rect.rect_in_circle_overlap(another_circle)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

menu()







