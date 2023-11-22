# Упражнение 8

# Балансирани дървета

## Миналия път разгледахме

- Двоични дървета за търсене 
- Алгоритми за обхождане на дървета

## Въпроси от миналия път/ домашното/ конт??ро#@лното

- :x

Решения от [домашно 6](https://hackerrank.com/contests/sda-ad-hw-6-2023) - [тук](https://github.com/TeogopK/SDA-solved/tree/main/Homeworks/hw6).

## Днес ще разгледаме

- Балансирани дървета за търсене
  - AVL tree 
  - Red-Black tree 

## AVL tree (АВЛ дърво)

- Самобалансиращо се двоично дърво за търсене.
- Разликата във височината на лявото и дясното поддърво за всеки възел е по-малка или равна 1.
- Гарантирана *O(logN)* сложност в най-лошия случай при търсене, добавяне и триене на елемент.
- Балансиране е нужно при добавянето или триене на елемент, когато се наруши свойството за разлика във височините.

![AVL tree operations GIF](https://upload.wikimedia.org/wikipedia/commons/f/fd/AVL_Tree_Example.gif)

## Red-Black tree (Червено-черно дърво)

- Отново гарантира *O(logN)* сложност в най-лошия случай при търсене, добавяне и триене на елемент.
- Операциите добавяне и триене на елемент не изискват толкова често балансиране, поради по-малката строгост в поддържането на баланс спрямо AVL дърво.

Свойства:
- Коренът е винаги черен.
- Всяко листо е черно (NIL leaf).
- Децата на червен възел са винаги черни.
- Всеки директен път от корен на поддърво до всяко листо (NIL leaf) минава през равен брой черни възли.

Следствие:
- Родителят на червен възел е винаги черен.
- Връх с един наследник е винаги червен.

![Example of Red-Black tree](https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Red-black_tree_example_with_NIL.svg/1920px-Red-black_tree_example_with_NIL.svg.png)

## Сравнение на структурите спрямо сложност по време

| операция | масив | свързан списък | сортиран масив | двоично наредено дърво | балансирано дърво |
| --- | --- | --- | --- | --- | --- |
| търсене | *O(N)* | *O(N)* | *O(logN)* |  *O(N)* | *O(logN)* |
| добавяне | *O(N)* | *O(N)* | *O(N)* |  *O(N)* | *O(logN)* |
| триене | *O(N)* | *O(N)* | *O(N)* |  *O(N)* | *O(logN)* |


## Имплементации в Python

Няма вградено балансирано двоично дърво за търсене в Python.
Структурите *set* и *dict* използват *Hash table*, която ще учим в следващи упражнения.

Аналогът на *set* и *dict* в C++ са *unordered_set* и *unordered_map*. Те също използват Хеш таблица. В C++ съществуват *ordered* варианти на горните колекции, които подреждат елементите/ ключовете по-големина. Така е нужно *inorder* обхождане, което е присъщо на балансираните дървета.

Примерна имплементация [AVL Tree](https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/avl_tree.py) и [Red-Black Tree](https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/red_black_tree.py).

## Задачи за упражнение

- [Volleyball Friends](https://www.hackerrank.com/contests/sda-hw-8/challenges/volleyball-friends)
- [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii)
- [Count Number of Bad Pairs](https://leetcode.com/problems/count-number-of-bad-pairs)
- [MacBook Cafes](https://www.hackerrank.com/contests/si-practice-7/challenges/brand-new)

Решения на задачите: [тук](https://github.com/TeogopK/SDA-solved/tree/main/Seminar/sem_08)