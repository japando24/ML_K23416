class ListProduct:
    def __init__(self):
        self.products = []
    def add_product(self, p):
        self.products.append(p)
    def print_products(self):
        for p in self.products:
            print(p)
    #Sap xep SP theo don gia giam dan
    #C1: Hai vong lap
    #C2: khong vong lap
    def desc_sort_products(self):
        for i in range (0,len(self.products)):
            for j in range(i+1,len(self.products)):
                pi=self.products[i]
                pj=self.products[j]
                if pi.price < pj.price:
                    self.products[j]=pi
                    self.products[i]=pj

# Sắp xếp giảm dần theo price (không dùng 2 vòng lặp lồng nhau)
    def desc_sort_products_2(self):
        result = []
        while self.products:
            # Tìm phần tử lớn nhất
            max_p = max(self.products, key=lambda p: p.price)
            result.append(max_p)
            self.products.remove(max_p)
        self.products = result
#-------------------------
    def _recursive_sort(self, products): #QC
        if not products:
            return []
        # Tìm sản phẩm có giá lớn nhất
        max_p = max(products, key=lambda p: p.price)
        products.remove(max_p)
        # Đệ quy cho phần còn lại
        return [max_p] + self._recursive_sort(products)

        # Sắp xếp sản phẩm giảm dần theo price bằng đệ quy (không for, không while, không sort)
    def desc_sort_products_3(self): #NQ
        def quicksort(lst):
            if len(lst) <= 1:
                return lst
            pivot = lst[0]
            left = [x for x in lst[1:] if x.price >= pivot.price]
            right = [x for x in lst[1:] if x.price < pivot.price]
            return quicksort(left) + [pivot] + quicksort(right)

        self.products = quicksort(self.products)

