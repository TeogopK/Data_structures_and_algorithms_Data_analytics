# Упражнение 3

# Алгоритми за сортиране

## Миналия път разгледахме

- Видове сложности
- Правила за пресмятане на Big O
- Изчисляване на сложности

## Задачи, които решавахме:

- [Two Sum](https://leetcode.com/problems/two-sum/) - решение [тук](https://github.com/TeogopK/SDA-solved/tree/main/Leetcode/sem_01/two_sum)
- [Plus One](https://leetcode.com/problems/plus-one/) - решение [тук](https://github.com/TeogopK/SDA-solved/tree/main/Leetcode/sem_01/plus_one)
  
Решения от [домашно 1](https://hackerrank.com/contests/sda-ad-hw-1-2023) - [тук](https://github.com/TeogopK/SDA-solved/tree/main/2023-2024/hw1).
  
## Въпроси от миналия път/ домашното

- :)

## Днес ще разгледаме

- бавни алгоритми за сортиране
  - Bubble sort
  - Selection sort
  - Insertion sort
- бързи алгоритми за сортиране
  - Merge sort
  - Quick sort 
- други
  - Counting sort

## Bubble sort (Метод на мехурчето)

- *O(N<sup>2</sup>)* сложност по време
- *О(1)* сложност по памет
- *N * (N - 1) / 2* брой размени в най-лошия случай
- [стабилен](https://en.wikipedia.org/wiki/Category:Stable_sorts) сортиращ алгоритъм

След всяка итерация на *i*, най-големият елемент "изплува" чрез последователни размени на съседни елементи.

```python
arr = [9, 4, 3, 2, 6, 7, 1, 8, 5]
N = len(arr)

for i in range(N - 1):
    for j in range(0, N - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Selection sort (Метод на пряката селекция)

- *O(N<sup>2</sup>)* сложност по време
- *О(1)* сложност по памет
- *N - 1* брой размени в най-лошия случай
- **не** е стабилен сортиращ алгоритъм

Търси се индексът на най-малкия елемент на всяка итерация.

```python
arr = [9, 4, 3, 2, 6, 7, 1, 8, 5]
N = len(arr)

for i in range(N - 1):
    min_index = i

    for j in range(i + 1, N):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[min_index], arr[i] = arr[i], arr[min_index]

print(arr) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Предпочитан пред Bubble sort поради по-малкото на брой размени, но за сметка на това не е стабилен. 

## Insertion sort (Метод на картоиграча)

- *O(N<sup>2</sup>)* сложност по време
- *О(1)* сложност по памет
- стабилен сортиращ алгоритъм

Всеки елемент се тегли като карта с гърба надолу. Търси се мястото му в ръката, като се изместват по-големите стойности с една позиция надясно.

```python
arr = [9, 4, 3, 2, 6, 7, 1, 8, 5]
N = len(arr)

for i in range(1, N):
    key = arr[i]

    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

[Подходящ](https://www.toptal.com/developers/sorting-algorithms) за малки масиви, и почти сортирани масиви. Това се дължи на ранното приключване на вътрешния цикъл при правилно поставено число (Best case сложността на алгоритъма е *O(N)*).

---

| \\ | Bubble sort | Selection sort | Insertion sort |
| --- | --- | --- | --- |
| Best case | *O(N)* | *O(N<sup>2</sup>)* | *O(N)* |
| Average case | *O(N<sup>2</sup>)* | *O(N<sup>2</sup>)* | *O(N<sup>2</sup>)* |
| Worst case | *O(N<sup>2</sup>)*  | *O(N<sup>2</sup>)* | *O(N<sup>2</sup>)* |
| Памет | *O(1)* | *O(1)* | *O(1)* |
| Стабилен | да | не | да |

## Merge sort (Сортиране със сливане)

- *O(NlogN)* сложност по време
- *О(N)* сложност по памет
- стабилен сортиращ алгоритъм
  
