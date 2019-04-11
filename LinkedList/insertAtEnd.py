__author__ = 'rdhek'

class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def Insert(head, data):
    if head:
        temp=head
        temp1=head
        while temp:
            temp1=temp
            temp=temp.next
        temp1.next=Node(data)
    else:
        head=Node(data)
    return head

def printList(head):
    if head:
        print head.data
        printList(head.next)


def Delete(head, position):
    temp=head
    temp1=head
    count=0
    if position==0:
        head=head.next
        del temp
        return head
    else:
        while temp and (count<position):
            temp1=temp
            temp=temp.next
            count=count+1
        temp1.next=temp.next
        del temp
        return head


head=Insert(None,2)
head=Insert(head,3)
head=Insert(head,4)
head=Delete(head,2)
printList(head)
