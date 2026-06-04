class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_list(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next

    def delete_list(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        if temp == self.head:
            self.head = temp.next
        else:
            prev.next = temp.next
    print()

    def

ll= LinkedList()
ll.add_list(30)
print("Cetak Linked List")
ll.display()
ll.add_list(50)
ll.add_list(70)
print("Cetak Linked List")
ll.display()
ll.delete_list(30)
print("Cetak Linked List")
ll.display()