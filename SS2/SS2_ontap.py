#  Cú pháp Lớp và Đối tượng
class Student: 
    # hàm khởi tạo
    def __init__(self, name, age, gender, grade, school):
        # gán giá trị nhận vào để làm thuộc tính 
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = grade
        self.school = school
        
    # Phương thức của lớp
    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Grade:", self.grade)
        print("School:", self.school)
        
        
# # Tạo đối tượng Student hs1
# hs1 = Student("Hieu",27, "Nam", "NCT-C4K-PTI25-HB", "MindX")
# print(hs1.name)
# print(hs1.age)
# hs1.show_info()


class HCN:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
        
        
    # Phương thức
    def tinh_chu_vi(self):
        return 2* (self.chieu_rong + self.chieu_dai)
    
    def tinh_dien_tich(self):
        return self.chieu_rong * self.chieu_dai
    
# # khởi tạo đối tượng HCN1
# hcn1 = HCN(5, 3)
# print(hcn1.tinh_chu_vi())
# print(hcn1.tinh_dien_tich())
        
