class Rectangle:

    def area(self,length,breadth):
        print(f"area of rectangle {length* breadth}")
    def perimeter(self,length,breadth):
        print(f"perimeter of rectangle {2*(length + breadth)}")
length = int(input("enter the length :"))
breadth = int(input("enter breadth :"))
r = Rectangle()
r.area(length,breadth)
r.perimeter(length,breadth)
              

