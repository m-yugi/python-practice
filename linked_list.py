from asyncio.windows_events import NULL
from operator import ne
from traceback import print_tb


class node:
    def __init__(self,val):
        self.val=val
        self.next=None
def display(root):
    while root is not None:
        print(root.val)
        root=root.next
root=node(1)
root.next=node(2)
root.next.next=node(3)
root.next.next.next=node(4)
display(root)