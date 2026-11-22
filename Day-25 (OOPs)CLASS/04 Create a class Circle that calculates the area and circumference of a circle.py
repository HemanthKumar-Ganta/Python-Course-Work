class Circle:
    def area(self,radius):
        s = 3.14 * radius ** 2
        print(f"Area of the circle is : {s}")
    def circumference(self,radius):
        t = 2 * 3.14 * radius
        print(f"Circumference of a circle is : {t}")
radius =float(input("enter radius of a circle :"))
c = Circle()
c.area(radius)
c.circumference(radius)
