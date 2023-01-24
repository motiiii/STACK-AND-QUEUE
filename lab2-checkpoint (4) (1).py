#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Задание1. Реализация stack'a c помощью списка

class Stack:
    def __init__(self):
        self.elements = []
        
    def push(self, element):
        "поместить элемент в стек"
        self.elements.append(element)
        return (f'Push {element} in the stack')

        
    def pop(self):
        "удалить вершину (возвращает  то значение, которое вытолкнули)"
        if self.isEmpty() == True :
            return None
        top = self.top()
        self.elements.pop()
        return top
    
    def top(self):
        "просмотреть вершину"
        if self.isEmpty() == True :
            return ('The top element is missing the stack is empty')
        return self.elements[-1]
    
    def isEmpty(self):
        "проверить на пустоту"
        if len(self.elements) == 0:
            return True
        else:
            return False
        
    def print(self):
        return print(self.elements)


# In[2]:


my_stack = Stack()

print(my_stack.push(1))
print(my_stack.push(2))
print(my_stack.push(3))
print(f'Pop {my_stack.pop()} from the stack')
print('Top element is', my_stack.top())
print('Stack is Empty:', my_stack.isEmpty())
my_stack.print()


# In[3]:


#Задание2.
def read_commands(stack, command):
    if command[0]=='1': #push
        el = command.split(',')[1]
        return print(stack.push(el))
    if command[0]=='2': #pop
        return print(f'Pop {stack.pop()} from the stack')
    if command[0]=='3': #top
        return print(stack.top())
    if command[0]=='4': #isEmpty
        return print('Stack is Empty:', stack.isEmpty())
    if command[0]=='5': #print
        return stack.print()
        


# In[5]:


filename = 'input.txt.txt'

with open(filename, "r") as file:
    for stroka in file:
        commands = stroka.split()
        stack = Stack()
        for command in commands:
            read_commands(stack, command) 
        print('_'*10)


# In[6]:


#Задание3.
import time
timefunct = []
with open(filename, "r") as file:
    for stroka in file:
        commands = stroka.split()
        stack = Stack()
        time_start = time.perf_counter()
        for command in commands:
            read_commands(stack, command) 
        t = time.perf_counter() - time_start
        timefunct.append(t)


# In[21]:


import pandas as pd
df = pd.DataFrame({
'Набор операций': ['первый', "второй", "третий"],
'время выполнения': [timefunct[0], timefunct[1],timefunct[2]]})
df


# In[7]:


#Задание4.
def calculate(inputs, stack):
    for x in inputs:
        if x in "+-*/^":
            if len(stack) < 2:
                print("ERROR")
                break
            b = int(stack.pop())
            a = int(stack.pop())
            if x == "+": res = a + b
            elif x == "-": res = a - b
            elif x == "*": res = a * b
            elif x == "^": res = a^b
            if x == '/':
                if b >0: res = a / b
                else: print('На 0 делить нельзя')
            stack.append(res)
        else: stack.append(x)

    if len(stack) == 1:
        print(stack[0])


# In[9]:


filename = 'input.txt.txt'
stack = []
with open(filename, "r") as file:
    for stroka in file:
        inputs = stroka.split()
        calculate(inputs, stack)


# In[10]:


#Задани1. Реализовать Очередь с помощью списка
class My_Queue: 
    def __init__(self): 
        self.queue = []
        
    def Enqueue(self, element):
        "вставка элемента"
        self.queue.append(element)
        return (f'Enqueue {element}')
    
    def Dequeue(self):
        "удаление элемента (Dequeue) (из задней части)"
        if len(self.queue) == 0:
            return None
        top = self.Top()
        self.queue.pop(0)
        return (f'Dequeue {top}')

    def Top(self):
        "просмотреть голову"
        if self.IsEmpty() == True :
            return ('The top element is missing the queue is empty')
        return self.queue[0]
    
    def IsEmpty(self):
        "проверка на пустоту"
        if len(self.queue) == 0:
            return True
        else:
            return False
        
    def Print(self):
        return print(self.queue)
    


# In[11]:


my_queue = My_Queue()

print(my_queue.Enqueue(1))
print(my_queue.Enqueue(2))
print(my_queue.Enqueue(3))
print(my_queue.Dequeue())
print('Head of queue is', my_queue.Top())
print('Queue is Empty:', my_queue.IsEmpty())
my_queue.Print()


# In[12]:


#с помощью стандартного класса Queue
from queue import Queue
que = Queue()
que.put('Apple')  #ставит элемент в очередь
que.put('Mango') 
que.put('Papaya') 
print(que.empty())  #проверяет, что очередь пуста,
print(que.get()) #удаляет и возвращает элемент из очереди
 


# In[13]:


#Задание2.
def read_commands2(queue, command):
    if command[0]=='1': # Enqueue
        el = command.split(',')[1]
        return print(queue.Enqueue(el))
    if command[0]=='2': #Dequeue
        return print(queue.Dequeue())
    if command[0]=='3': #Top
        return print(queue.Top())
    if command[0]=='4': #IsEmpty
        return print('Queue is Empty:', queue.IsEmpty())
    if command[0]=='5': #Print
        return queue.Print()


# In[15]:


filename = 'input.txt.txt
'

with open(filename, "r") as file:
    for stroka in file:
        queue = My_Queue()
        commands = stroka.split()
        for command in commands:
            read_commands2(queue, command) 
        print('_'*10)


# In[16]:


#Задание3.
def python_class(que, command):
    if command[0]=='1': # put
        el = command.split(',')[1]
        que.put(el)
        return print('put', el)
    if command[0]=='2': # get
        return print(que.get())
    if command[0]=='3': #Empty
        return print('Queue is Empty:', que.empty())
    
def my_realization(queue, command):
    if command[0]=='1': # Enqueue
        el = command.split(',')[1]
        return print(queue.Enqueue(el))
    if command[0]=='2': #Dequeue
        return print(queue.Dequeue())
    if command[0]=='3': #IsEmpty
        return print('Queue is Empty:', queue.IsEmpty())


# In[18]:


filename = 'input.txt.txt'
time_python_class = []
with open(filename, "r") as file:
    for stroka in file:
        que = Queue()
        commands = stroka.split()
        time_start = time.perf_counter()
        for command in commands:
            python_class(que, command)
        t = time.perf_counter() - time_start
        time_python_class.append(t)


# In[19]:


filename = 'input.txt.txt'
time_my_realization = []
with open(filename, "r") as file:
    for stroka in file:
        queue = My_Queue()
        commands = stroka.split()
        time_start = time.perf_counter()
        for command in commands:
            my_realization(queue, command)
        t = time.perf_counter() - time_start
        time_my_realization.append(t)


# In[27]:


import pandas as pd
df = pd.DataFrame({
'Набор операций': ['различными по длине', 'различными по длине', 'одинаковыми по длине, но различными по составу операций', 'одинаковыми по длине, но различными по составу операций '],
'время выполнения my_realization': [time_my_realization[0], time_my_realization[1], time_my_realization[2], time_my_realization[3]]
'время выполнения python_class': [time_python_class[0], time_python_class[1], time_python_class[2], time_python_class[3]]})
df

