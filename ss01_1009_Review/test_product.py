from ss01_1009_Review.product import Product

p1=Product(100,"Thuoc Lao",4,20)
#Xuat p1 ra man hinh
print(p1)
p2=Product(200,"Thuoc Tri Hoi Nach",5,30)
#Một ô nhớ có từ 2 người qly trơ lên p=> Alias (nếu ko ai qly thi thu hoi)
p1=p2
print("Thông tìnuar")
print (p1)

p1.name="""Thuoc tang tuong"""
print("Thông tin cua p2")
print(p2)                                                                                                                                                       