# Упражнение 5

# Свързан списък

## Миналия път разгледахме

- Binary search
- Ternary search
- Jump search
- Exponential search
- Двоично търсене върху функция

## Въпроси от миналия път/ домашното

- :)

Решения от [домашно 3](https://hackerrank.com/contests/sda-ad-hw-3-2023) - [тук](https://github.com/TeogopK/SDA-solved/tree/main/Homeworks/hw3).

## Днес ще разгледаме

- Едносвързан списък
- Двойносвързан списък
- Вграден списък в Python

## Singly linked list (Едносвързан списък)

Едносвързаният списък представлява поредица от възли, като всеки от тях съдържа информация за **данните** и **кой е следващият възел** в поредицата.

---

Класическата имплементация на възел от едносвързан списък:

```python
class Node:
    def __init__(self, data=0, next_=None):
        self.data = data
        self.next_ = next_ 
```

---

Тази структура може да се обвие в клас, който да представлява свързан списък:

```python
class LinkedList:
    def __init__(self, head=None):
        self.head = head 
```

---

Списъкът може да има не само глава, но и опашка:

```python
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head 
        self.tail = tail
```

---

Опашката дава възможност за добавяне на елемент за константно време в края на списъка:

```python
class LinkedList:
    # ...
    def push_back(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next_ = new_node
            self.tail = new_node
```

---

Добавяне на елемент в началото на списъка става за константно време:

```python
class LinkedList:
    # ...
    def push_front(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next_ = self.head
            self.head = new_node
```

---

Обхождане на свързан списък:

```python
class LinkedList:
    # ...
    def print(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next_
```

---

Изтриване на елемент в **началото** на списъка - **константна** сложност:

```python
class LinkedList:
    # ...
    def pop_front(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next_ 
```

---

Изтриване на елемент в **края** на списъка - **линейна** сложност:

```python
class LinkedList:
    # ...
    def pop_back(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next_ != self.tail:
                current = current.next_

            current.next_ = None 
            self.tail = current
```

## Двойносвързан списък

Всеки възел съхранява информация за елемента преди и след себе си.
Това позволява обхождане на списъка в обратна посока.

---

Класическата имплементация на възел от двойносвързан списък:

```python
class Node:
    def __init__(self, data, next_=None, prev=None):
        self.data = data
        self.next_ = next_
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head 
        self.tail = tail
```

Имплементациите на основните функции изискват правилно задаване на предишния елемент за разлика от тези на едносвързан списък.

---

Добавяне на елемент в началото на списъка - константно време:

```python
class DoublyLinkedList:
    # ...
    def push_front(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next_ = self.head
            self.head.prev = new_node
            self.head = new_node
```

---

Добавяне на елемент в края на списъка - константно време:

```python
class DoublyLinkedList:
    # ...
    def push_back(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next_ = new_node
            new_node.prev = self.tail
            self.tail = new_node
```

---

Премахване на елемент в началото на списъка - константно време:

```python
class DoublyLinkedList:
    # ...
    def pop_front(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next_ 
            self.head.prev = None
```

---

Премахване на елемент в края на списъка - **константно** време:

```python
class DoublyLinkedList:
    # ...
    def pop_back(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next_ = None
```

Получаваме предимството да премахнем последния елемент за константно време, но увеличаваме паметта, нужна за съхранението на структурата.

## Linked List или Array

Предимства на Linked List:
- константно време за добавяне в началото и края.
- константно време за добавяне на елемент на произволна позиция при наличие на указател*.
- не се заделя излишна памет за резервни клетки.

Недостатъци:
- произволен достъп до елемент на дадена позиция не е *O(1)*.*
- заделя се допълнителна памет за всеки указател към следващия елемент.

## Вграден списък в Python

В Python няма чиста имплементация на свързан списък. 

### Обикновен списък (list)

- Интерфейсът на обикновения списък позволява използването му като свързан списък.
- Най-големият недостатък е добавянето на елемент на произволно място в списъка, което е линейна операция.*

```python
llist = [i for i in range(1, 9)]

llist.append(99)
llist.insert(6, 66)

llist # [1, 2, 3, 4, 5, 6, 66, 7, 8, 99]
```

### Deque

- Имплементиран е чрез двойносвързан списък на С. 
- Интерфейсът му предоставя пълната функционалност на свързания списък при [познатите сложности](https://wiki.python.org/moin/TimeComplexity) на операциите. 
- Допълнително свойство на *Deque* е достъпването на произволен възел с константа сложност* както при масивите (*О(1) random access*).

```python
from collections import deque

dlist = deque([1,2,3])

dlist.pop()
dlist.append(33)

dlist.popleft()
dlist.appendleft(-1)

print(dlist) # deque([-1, 2, 33])
print(dlist[1]) # 2
```

Примерна имплементация на Singly Linked List и Doubly Linked List в [playground-а](playground_05.ipynb).


## Задачи за упражнение

- [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list)
- [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists)
- [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists)
- [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle)

- [Radio Transmitters](https://www.hackerrank.com/challenges/hackerland-radio-transmitters)

---
- [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list)
  
- [Linked List Random Node](https://leetcode.com/problems/linked-list-random-node)
  
- [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list)

Решения на задачите: [тук](https://github.com/TeogopK/SDA-solved/tree/main/Seminar/sem_05)