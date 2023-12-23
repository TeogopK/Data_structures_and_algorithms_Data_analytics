# Упражнение 6

# Стек и опашка

## Миналия път разгледахме

- Едносвързан списък
- Двойносвързан списък
- Вграден списък в Python

## Въпроси от миналия път/ домашното

- :)

Решения от [контролно 2](https://www.hackerrank.com/contests/sda-2023-2024-ad-2ws3e) - [тук](https://github.com/TeogopK/SDA-solved/tree/main/Exams/exam_02).

Решения от [домашно 4](https://hackerrank.com/contests/sda-ad-hw-4-2023) - [тук](https://github.com/TeogopK/SDA-solved/tree/main/Homeworks/hw4).

## Днес ще разгледаме

- Стек
- Опашка

## Stack (Стек)

- Реализация чрез **едносвързан** списък, на който пазим единствено главата - най-горния елемент. 
- Операциите са *pushfront()* и *popfront()* - *O(1)* сложност по време.
- *LIFO* - Last In First Out.

## Queue (Опашка)

- Реализация чрез **едносвързан** списък, на който пазим опашката и главата. 
- Операциите са *pushback()* и *popfront()* - *O(1)* сложност по време.
- *FIFO* - First In First Out.

## Имплементации в Python

### Обикновен списък (list)

- Подходящ само за стек, поради *О(1)* добавяне и премахване на елемент от края, но *O(N)* в началото.
- Предимство: *О(1)* достъп до произволен елемент.

### Deque

- Подходящ и за стек, и за опашка, поради константно добавяне/ премахване на елемент от началото и края.
- Също притежава свойството *О(1)* *random access*.

### Queue/ LifoQueue

- [Синхронни](https://docs.python.org/3/library/queue.html) колекции от модула *queue*.
- Могат да бъдат използвани като обикновена опашка и стек, но не им е там силата.
- Създадени са за многонишково програмиране.

Примерни имплементации на стек и опашка със свързан списък в [playground-а](playground_06.ipynb).

## Задачи за упражнение

- [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare)
- [Baseball Game](https://leetcode.com/problems/baseball-game)
- [Valid Parentheses](https://leetcode.com/problems/valid-parentheses)
- [Welcome to the Jungle](https://www.hackerrank.com/contests/practice-4-sda/challenges/welcome-to-the-jungle)

- [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls)
- [Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch)

Решения на задачите: [тук](https://github.com/TeogopK/SDA-solved/tree/main/Seminar/sem_06)