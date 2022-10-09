class Node(object):
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
    def connect(self, other):
        if not isinstance(other, Node):
            raise TypeError
        self.next=other
    def search(self, index):
        if not isinstance(index, int):
            raise TypeError
        elif index<0:
            raise IndexError
        i=0
        s=self
        while i!=index:
            i+=1
            s=s.next
            if s==None:
                raise IndexError
        return s.data