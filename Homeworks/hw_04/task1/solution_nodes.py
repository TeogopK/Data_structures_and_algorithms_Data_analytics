#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeDuplicates(head_node):
    current = head_node
    
    while(current):
        if current.next and current.next.data == current.data:
            current.next = current.next.next
        else:
            current = current.next
            
    return head_node