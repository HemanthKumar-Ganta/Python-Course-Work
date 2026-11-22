class Book:
    def set_title(self,title):
        self.title = title
        print(f"Title of the book : {title}")
    def set_author(self,author):
        self.author = author
        print(f"The author of the book : {author}")
    def set_publication_year(self,publication_year):
        self.publication_year = publication_year
        print(f"Publication year of the book : {publication_year}")
    def display(self):
         print(f"Title of the book : {self.title}")
         print(f"The author of the book : {self.author}")
         print(f"Publication year of the book : {self.publication_year}")
t = input("enter title of the book:")
a = input("enter author of the book:")
p = int(input("enter publication of year:"))
b = Book()
b.set_title(t)
b.set_author(a)
b.set_publication_year(p)
b.display()