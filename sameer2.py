class lib:
    def __init__(self):
        self.book=[]
        self.writer=[]
        self.price=[]
        self.flag=[]
    def add(self,book,writer,price,flag):
        self.book.append(book)
        self.writer.append(writer)
        self.price.append(price)
        self.flag.append(flag)
    def display(self,n):
        print(self.book[n-1])
        print(self.writer[n-1])
        print(self.price[n-1])
        if(self.flag[n-1]):
            print("in library")
        else:
            print("sold")
    def book_given_author(self,name):
        for i in range(len(self.writer)):
            if(name==self.writer[i]):
                print(self.book[i])
    def name_book(self,n):
        print(self.book[n-1])
    def count_book(self):
        print(len(self.book))
    def print_book(self):
        for i in self.book:
            print(i)
vit=lib()
flag=True
while(flag):
    print("1. Add book information \n"
          "2. Display book information\n"
          "3. List all books of given author\n"
          "4. List the title of specified book\n"
          "5. List the count of books in the library\n"
          "6. List the books in the order of accession number\n"
          "7 Exit\n")
    res=int(input("please select an option\n"))
    if(res==1):
        print("please enter the name of the book")
        book=input()
        print("please enter the name of the writer")
        name=input()
        print("please enter the price of the book")
        price=int(input())
        vit.add(book,name,price,True)
    elif(res==2):
        n=int(input("please enter the accession number book you want to see"))
        vit.display(n)
    elif(res==3):
        print("please enter the name of the writer you want to search")
        name=input()
        vit.book_given_author(name)
    elif(res==4):
        n=int(input("please enter the accession number you want to see the name of"))
        vit.name_book(n)
    elif(res==5):
        vit.count_book()
    elif(res==6):
        vit.print_book()
    elif(res==7):
        flag=False
    else:
        print("please enter the valid input")