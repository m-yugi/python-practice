
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

yugi=node(0)
def new_node(n):
    gani=node(n)
    ran=yugi
    if yugi:
        yugi=gani
    else:
        while ran.next:
            ran=ran.next
        ran.next=gani
    return yugi
def display():
    temp = yugi
    if temp is None:
        print("list is empty")
    else:
        while temp:
            print(temp.data)
            temp = temp.next

yugi=new_node(1)
yugi.next=new_node(2)
yugi.next.next=new_node(3)
display()
