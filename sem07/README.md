# Упражнение 6

# Стек и опашка

## Миналия път разгледахме

- Стек
- Опашка
- Опашка с 2 края (deque)

## Въпроси от миналия път/ домашното

- :)

Решения от [домашно 5](https://hackerrank.com/contests/sda-ad-hw-5-2023) - [тук](https://github.com/TeogopK/SDA-solved/tree/main/Homeworks/hw5).

## Днес ще разгледаме

- Дървета
- Двоични дървета
- Двоични дървета за търсене (BST)
- Алгоритми за обхождане на дървета

## Tree (Дърво)

- Нелинейна структура от данни, която се състои от възли, които имат наследници (подобно на свързания списък), но един възел, може да има няколко наследника и само 1 предшественик.
- Дървото се характеризира с липсата на цикли (Ацикличен свързан граф).
- Възли без наследници се наричат листа.
- Коренът на дървото е възелът без нито един предшественик.

## Binary Tree (Двоично дърво)

- Дърво, чиито възли имат най-много двама наследника. Най-често се обозначават ляв и десен (left, right).

## Binary Search Tree (Двоично дърво за търсене)

- Дефинира се рекурсивно по следния принцип:
1) Всяко листо е двоично дърво за търсене.
2) Всяко поддърво започващо от даден възел е двоично дърво за търсене, ако:
2.1) Най-големият елемент в лявото му поддърво е по-малък от стойността в дадения възел.
2.2) Най-малките елемент в дясното му поддърво е по-голям от стойността в дадения възел.
2.3) И лявото поддърво и дясното поддърво са двоични дървета за търсене.

## Имплементации в Python

Няма вградено двоични дърво за търсене в python... Ако искаме да ползваме такова ще трябва да си го напишем, но това не се препоръчва.


Примерни имплементации в [playground-а](playground_07.ipynb).

## Задачи за упражнение

- [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)
- [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/description/)
- [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/)
- [Same Tree](https://leetcode.com/problems/same-tree/)
- [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
- [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Решения на задачите: [тук](https://github.com/TeogopK/SDA-solved/tree/main/Seminar/sem_07)