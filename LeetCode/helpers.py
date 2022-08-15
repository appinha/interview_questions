# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return (str(self.val))

    def __getitem__(self, key):
        currentNode = self
        while key:
            key -= 1
            currentNode = currentNode.next
        return currentNode

class LinkedList:
    def generate(input: list):
        head = ListNode(input[0])

        currentNode = head
        for value in input[1:]:
            newNode = ListNode(value)
            currentNode.next = newNode
            currentNode = newNode

        return head

    def print(head: ListNode):
        result = '['

        currentNode = head
        while currentNode:
            result += str(currentNode.val) + ', '
            currentNode = currentNode.next

        print(result[:-2] + ']')

    def len(head: ListNode):
        currentNode = head
        count = 0
        while currentNode:
            count += 1
            currentNode = currentNode.next
        return count
