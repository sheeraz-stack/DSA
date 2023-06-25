#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Implement a stack using a list in Python. Include the necessary methods such as push, pop, and isEmpty.


# In[18]:


def create_stack():
    stack = list()           
    return stack

def Isempty(stack):
    return len(stack) == 0

def push(stack, n):
    stack.append(n)
    print("pushed item: " + n)

def pop(stack):
    if (Isempty(stack)):
        return "stack is empty"
    else:
        return stack.pop()

def show(stack):
    print("The stack elements are:")
    for i in stack:
        print(i)
        
stack = create_stack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
push(stack, str(40))
print("popped item: " + pop(stack))
show(stack)


# In[ ]:


Implement a queue using a list in Python. Include the necessary methods such as enqueue, dequeue, and isEmpty.


# In[19]:


from collections import deque  

def create_stack():  
    stack = deque()    
    return stack 
  
def push(stack, item):
    stack.append(item)

def pop(stack):
    if(stack):
        print('Element popped from stack:')
        print(stack.pop())
    else:
        print('Stack is empty')
    
def show(stack):
    print('Stack elements are:')
    print(stack)
    
new_stack=create_stack()
push(new_stack,25)
push(new_stack,56)
push(new_stack,32)
show(new_stack)

pop(new_stack)
show(new_stack)

