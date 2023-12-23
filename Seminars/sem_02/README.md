# Упражнение 2

# Сложност на алгоритми

## Миналия път разгледахме

- Защо е важно СДА-то?
- HackerRank демо
- Обектите в Python
- Bigint 
- List comprehension
- GIL (Global Interpreter Lock)

## Задачи, които решавахме:

- [Съквартиранти](https://www.hackerrank.com/contests/sda-hw-1-2022/challenges/1-410) - решение [тук](https://github.com/TeogopK/SDA-solved/tree/main/2022-2023/hw1/task1)
- [Casino Royale](https://www.hackerrank.com/contests/sda-hw-2-2022/challenges/1-146-1) - решение [тук](https://github.com/TeogopK/SDA-solved/tree/main/2022-2023/hw2/task1)
  
Решенията на задачи от час и други ще намерите в [репото](https://github.com/TeogopK/SDA-solved) с решения.
  
## Днес ще разгледаме
- Видове сложности
- Правила за смятане на Big O изрази
- Основи при изчисляване на сложности

## Въпроси от миналия път

- copy() vs deepcopy()
- using filter()

## Copy vs Deepcopy

Присвояване на стойността на масив чрез *оператор =*, без използването на *copy()*. Промени в бащата/ детето, водят до промени **и в бащата, и в детето**:

```python
father = [i for i in range(5)]
child = father

father.insert(2, 99) # same with child.insert()

print("Father: ", father)   # [0, 1, 99, 2, 3, 4]
print("Child: ", child)     # [0, 1, 99, 2, 3, 4]
```

Родителят и детето **са един и същи** обект:

```python
print(id(child) == id(father) # True
```

---

Копиране на масив чрез метода *copy()*. Промени в бащата **не се отразяват** на промени в детето. Обратното също е вярно.

```python
father = [i for i in range(5)]
child = father.copy()

father.insert(2, 99)

print("Father: ", father)   # [0, 1, 99, 2, 3, 4]
print("Child: ", child)     # [0, 1, 2, 3, 4]
```

Родителят и детето **са два различни** обекта:

```python
print(id(child) != id(father) # True
```

---

Копиране на масив, съдържащ **съставни** обекти (масив от mutable objects) чрез използване на метод *copy()*. Промени в съставен обект на бащата **водят до промени и в детето**.

```python
from copy import copy

inner_list = [4, 5]

father = [1, 2, 3, inner_list]
child = copy(father)

father[3].append(6) # equals inner_list.append(6)

print("Father: ", father)   # [1, 2, 3, [4, 5, 6]]
print("Child: ", child)     # [1, 2, 3, [4, 5, 6]]
```

Детето и бащата **са два различни** обекта, но **съставните части си остават същите** при използването на *copy()*.

```python
print(id(child) != id(father)) # True
print(id(child[3]) == id(father[3])) # True
```

---

Копиране на масив, съдържащ **съставни** обекти (масив от mutable objects) чрез използване на метод *deepcopy()*. Промени в съставен обект на бащата **не водят** до промени в детето.

```python
from copy import deepcopy

inner_list = [4, 5]

father = [1, 2, 3, inner_list]
child = deepcopy(father)

father[3].append(6)

print("Father: ", father)   # [1, 2, 3, [4, 5, 6]]
print("Child: ", child)     # [1, 2, 3, [4, 5]
```

Детето и бащата **са два различни** обекта, и **съставните части са различни обекти** при използването на *deepcopy()*.

```python
print(id(child) != id(father)) # True
print(id(child[3]) == id(father[3])) # True
```

## Filter()

*Filter()* се нуждае от аргумент функция, по която да се извърши филтрирането. (В Python функциите притежават способността да бъдат подавани, като аргумент на функция - [First-class citizen](https://en.wikipedia.org/wiki/First-class_citizen))

Това може да е наша дефинирана функция:

```python
arr = [i for i in range(10)]

def check_if_even(x):
    return x % 2 == 0

even_arr = list(filter(check_if_even, arr))
print(even_arr) # [0, 2, 4, 6, 8]
```

Или може да е *анонимна* функция, така наречените *ламбда изрази*:

```python
arr = [i for i in range(10)]

even_arr = list(filter(lambda x: x % 2 == 0, arr))
print(even_arr) # [0, 2, 4, 6, 8]
```

## Видове сложности:
- константа - *O(1)*
- логаритмична - *О(logN)*
- линейна - *O(N)*
- енлог - *O(NlogN)*
- квадратична - *O(N<sup>2</sup>)*
- кубична - *O(N<sup>3</sup>)*
- експоненциална - *O(c<sup>N</sup>)*

Ред на нарастване на времето:

>*1 < logN < sqrtN < N < NlogN < N<sup>2</sup> < N<sup>3</sup> < 2<sup>N</sup> < 3<sup>N</sup> < N! < N<sup>N</sup>*


## Правила за смятане на Big O изрази:

- константите, които са множители не влияят.
  > *O(100N) = O(N)*

- влияе само най-бързо растящата функция, при сбор от множители.
  > *О(N<sup>2</sup> + NlogN + N + 1) = O(N<sup>2</sup>)*

- при произведение от множители, влияят всички функции.
  > *O(N<sup>2</sup> log<sup>3</sup>N) не може да бъде опростено.

- основата на логаритъма не влияе.
  > *O(log<sub>2</sub>N) = O(log<sub>3</sub>N)*

    Изписва се просто *O(logN)*.
    Това не важи за степента на логаритмична функция (горния пример).
    
---

Примери:
- *О(2N) = O(N) = O(10000N)*
- *O(10000000) < O(logN)*
- *O(N + M)*

При невъзможност да се определи коя функция е по-голяма *N* или *М*, изразът *O(N + M)* не може да бъде опростен.


## Колко разлика оказва сложността? (практичен пример)

Нека имаме 2 компютъра. Компютър А е най-бързият за времето си със производителност 10 милиарда операции в секунда. Компютър Б е обикновен компютър и изчислява 10 милиона операции в секунда.

Задачата на компютрите е да сортират масив с 10 милиона елемента. 

Машина А използва Insertion sort със сложност *2N<sup>2</sup>*. Машина Б използва Мerge sort със сложност *50NlogN*.

За колко време всяка машина ще се справи със задачата?

Суперкомпютър А:
- S<sub>1</sub> = 2N<sup>2</sup> стъпки, за N = 10<sup>7</sup>
- V<sub>1</sub> = 10<sup>10</sup> стъпки/ сек
- => t<sub>1</sub> = 20000 сек. = ~5.5 ч.

Компютър Б:
- S<sub>2</sub> = 50NlogN стъпки, за N = 10<sup>7</sup>
- V<sub>2</sub> = 10<sup>7</sup> стъпки/ сек
- => t<sub>2</sub> = ~1163 сек. = ~20 мин.

Въпреки разликата в производителността и константите в алгоритмите (*2 и 50*), резултатите са коренно различни.

Още по-съществена разлика се наблюдава при увеличаване на големината на масива 10 пъти. При N = 100 милиона числа, компютър **А** отнема **23 дни**, а компютър **Б** - **4 часа**.


## Основи при изчисляване на сложности

*O(1)* - връщането на константа:
  
```python
def get_Pi():
    return 3.14
```

*O(1)* - връщането на елемент от масив:
  
```python
def get_5th_element(arr):
    return arr[5]
```

---

*O(N)* - еднократно обхождане на масив с големина *N*.

```python
for el in arr:
    print(el)
```

*O(N<sup>2</sup>)* - обхождане на масив с големина *N* *N* пъти (чрез вложен цикъл). Обхождане на матрица с размер *NxN*.

```python
for i in range(N):
    for j in range(N):
        print(i, j)
```

---

*O(2<sup>N</sup>)* - Намиране на *N*-тото число от редицата на Фибоначи. Всяко извикване на функцията, създава 2 нови деца, всяко от които 2 свои деца и т.н.

```python
def fibonacci(N):
    if N <= 1:
        return N
    return fibonacci(N-1) + fibonacci(N-2)
```


*O(logN)* - Намиране на колко двойки се съдържат в числото *N*. На всяко рекурсивно извикване, числото намаля 2 пъти.

```python
def count_deuces(N, count = 0):
    if N <= 1:
        return count
    
    count += 1
    return count_deuces(N // 2, count)
```

---

*O(N + M)* - обхождане на масив с големина *N* и масив с големина *M*.

```python
def brothers(N, M):
    for i in range(N):
        print(i)

    for j in range(M):
        print(j)
```

## Задачи за упражнение (в [LeetCode](https://leetcode.com/))

- [Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [Two Sum](https://leetcode.com/problems/two-sum/)
- [Plus One](https://leetcode.com/problems/plus-one/)
- [Rotate Image](https://leetcode.com/problems/rotate-image/)

Решения на задачите: [тук](/Tasks/tasks_02)
