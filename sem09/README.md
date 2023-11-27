# Упражнение 9

# Приоритетна опашка

## Миналия път разгледахме

- AVL балансирано двоично дърво

## Въпроси от миналия път/ домашното

- Какво е Heap Sort от упражнение 3?

Решения от [домашно 7](https://hackerrank.com/contests/sda-ad-hw-7-2023) - [тук](https://github.com/TeogopK/SDA-solved/tree/main/Homeworks/hw7).

## Днес ще разгледаме

- Пирамида (Heap)
- Пирамидално сортиране (Heap sort)
- Приоритетна опашка (Priority queue)

## Heap (Пирамида)

- Дървовидна структура от данни.
- Подрежда елементите спрямо естествената им наредба*.
- При Min heap най-малкият елемент е коренът.
- Всеки възел е по-малък по стойност от децата си.
- Всяко ниво на дървото без последното е задължително запълнено.
- Структурата може да се реализира чрез масив.
  
### Функции:
- Константен достъп до най-малкия елемент - корена.
- Логаритмична сложност за добавяне и премахване на елемент.
- Не предоставя възможност за ефикасно търсене на случаен елемент.
- **Не е** задължително обхождането в широчина/ дълбочина да изведе елементите в сортиран ред.
- Премахването на корена до изчерпване на елементите **ще изведе** елементите в сортиран ред.

### Имплементация с масив



## Heap Sort (Пирамидално търсене)



## Priority Queue (Приоритетна опашка)




## Имплементации в Python

Съществуват две готови имплементации *heapq* и *queue.PriorityQueue*.

### heapq

- [Модулът](https://docs.python.org/3/library/heapq.html) работи върху *list* структура.
- Може да превърне *list* в *Min heap* чрез *heappify()* за ***O(N)*** време без използването на допълнителна памет. 
- Масив превърнат в *Heap* **не е** сортиран! Всеки елемент трябва да бъде изваден за логаритмично време.
- Предоставя възможност за добавяне на елемент (*heappush()*) и премахване на най-малкия елемент (*heappop()*) с логаритмична сложност.

```python
import heapq

h = [7, 3, 4, 9, 6]
heapq.heapify(h)

print(h[0]) # 3
heapq.heappush(h, 5)

while h:
    print(heapq.heappop(h)) # 3, 4, 5, 6, 7, 9
```

### queue.PriorityQueue

- Модулът [*queue*](https://docs.python.org/3/library/queue.html) предоставя синхронни опашки, които са [*thread safe*](https://en.wikipedia.org/wiki/Thread_safety).
- Използва *heapq* структурата отдолу.
- Предоставя възможност за добавяне на елемент (*put()*) и премахване на най-малкия елемент (*get()*) с логаритмична сложност.

```python
from queue import PriorityQueue

pq = PriorityQueue()
arr = [7, 3, 4, 9, 6]

for el in arr:
    pq.put(el)

print(pq.queue[0]) # 3
pq.put(5)

while not pq.empty():
    print(pq.get())  # 3, 4, 5, 6, 7, 9
```

Примерна имплементация на Priority Queue в [playground-а](playground_09.ipynb).

## Задачи за упражнение

- [Jesse and Cookies](https://www.hackerrank.com/challenges/jesse-and-cookies/problem)
- [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array)
- [Maximal Score After Applying K Operations](https://leetcode.com/problems/maximal-score-after-applying-k-operations)
- [Banitsa Shop](https://www.hackerrank.com/contests/sda-hw-8-2021/challenges/fullstack-developer)
- [Find the Running Median](https://www.hackerrank.com/challenges/find-the-running-median/problem)

Решения на задачите: [тук](https://github.com/TeogopK/SDA-solved/tree/main/Seminar/sem_09)