# class PersistenStackEasyMode:
#
#     def __init__(self, values: list=[], cur_val_idx: int=0):
#         self.values: list = values
#         self.cur_val_idx: int = cur_val_idx
#
#     def push(self, val: int) -> object:
#         if len(self.values) > 0:
#             self.cur_val_idx += 1
#         self.values.insert(self.cur_val_idx,val)
#         return PersistenStackEasyMode(self.values, self.cur_val_idx)
#
#     def pop(self):
#         return self.cur_val_idx, self.values[self.cur_val_idx]
#
# stack1: PersistenStackEasyMode = PersistenStackEasyMode()
# stack1: PersistenStackEasyMode = stack1.push(1)
# stack1 = stack1.push(2)
#
# value3, stack3 = stack1.pop()
# print(value3)
# print(stack3)
#
# print("=============")
#
# class Node:
#     def __init__(self, value, prev=None):
#            self.value = value
#            self.prev = prev
#
# class PersistentStack:
#     def __init__(self, head=None):
#             self.head = head
#
#     def push(self, val):
#         # This creates a new PersistentStack with a new node (object) and sets the prev value on the object to the previous head
#         return PersistentStack(Node(val, self.head))
#
#     def pop(self):
#         if self.head is None:
#             raise IndexError("Nothing in the stack but pancakes")
#         return self.head.value, PersistentStack(self.head.prev)
#
# stack = PersistentStack()
# stack = stack.push(1)
# stack = stack.push(2)
# stack = stack.push(3)
# print(stack.head.value)
#
# value2, stack2 = stack.pop()
# print(value2)
# print(stack.head.value)


# Linked List
class Node:

    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev

class PersistemtStack:

    def __init__(self, head=None):
        self.head = head

    def push(self, value):
        return PersistemtStack(Node(value, self.head))

    def pop(self):
        return self.head.value, PersistemtStack(self.head)

stack = PersistemtStack()
stack = stack.push(1)
stack = stack.push(2)
print(stack.head.value)
hval, sval = stack.pop()
print(hval)
print(sval.head.value)

#################
from random import randint


class PersistentSomething:

    def __init__(self):
        self.val_lst = []
        self.val_idx = {}

    def insert(self, value):
        # If we care about blocking duplicate
        if value in self.val_lst:
            return False
        self.val_lst.insert(value)
        self.val_idx[value] = len(self.val_lst)
        return True

    def remove(self, value):
        if value not in self.val_lst:
            return False
        # Get values index
        vidx: int = self.val_idx[value]
        # Get the last item in the list
        last_val = self.val_lst[-1]
        # Set the two indexes
        self.val_idx[last_val] = vidx
        self.val_idx[value] = last_val
        self.val_lst.pop()
        del self.val_idx[value]
        return True

    def get_random(self):
        if len(self.val_lst) < 1:
            raise Exception
        return self.val_lst[randint(0,len(self.val_lst))-1]