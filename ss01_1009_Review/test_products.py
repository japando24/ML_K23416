from ss01_1009_Review.product import Product
from ss01_1009_Review.products import ListProduct

lp=ListProduct()
lp.add_product(Product(100,"Product 1",200,10))
lp.add_product(Product(200,"Product 2",10,15))
lp.add_product(Product(150,"Product 3",80,8))
lp.add_product(Product(300,"Product 4",50,20))
lp.add_product(Product(250,"Product 5",150,17))
print("List of Products:")
lp.print_products()

# lp.desc_sort_products()
# print("List of Products after descending sort:")
# lp.print_products()

# lp.desc_sort_products_2()
# print("List of Products after descending sort:")
# lp.print_products()

# lp.desc_sort_products_3()
# print("List of Products after descending sort:")
# lp.print_products()

