'''
Question: 
Given the head of a singly linked list, reverse the list, and return the reversed list.

'''

def reverseList(self, head):
    new_list = None
    current = head

    while current:
        next_node = current.next
        current.next = new_list
        new_list = current
        current = next_node
    
    return new_list
