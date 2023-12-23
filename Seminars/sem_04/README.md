# Упражнение 4

# Алгоритми за търсене

## Миналия път разгледахме

- Бавни алгоритми за сортиране
- Бързи алгоритми за сортиране
- Сортиране с броене
  
## Въпроси от миналия път/ домашното/ контролното

- Кой сортиращ алгоритъм използва методът *sort()* в Python?

Решения от [домашно 2](https://hackerrank.com/contests/sda-ad-hw-2-2023) - [тук](/Homeworks/hw_02).

Решения от [контролно 1](https://www.hackerrank.com/contests/sda-ad-2022-2023-3ewsxf) - [тук](/Exams/exam_01).

# Tim sort

- хибриден алгоритъм - комбинира Merge sort и Insertion sort
- *O(NlogN)* сложност по време
- *О(N)* сложност по време в най-добрия случай
- *О(N)* сложност по памет
- стабилен сортиращ алгоритъм

Масивът се разделя на парчета. Всяко парче се сортира с Insertion sort. След това парчетата се съединяват чрез Merge операцията от Merge sort.

[Примерна](https://github.com/TheAlgorithms/Python/blob/master/sorts/tim_sort.py) имплементация:

```python
def timsort(arr):
    return sorted(arr)
```

Реалната имплементация използва по-сложни [техники](https://en.wikipedia.org/wiki/Timsort).

## Днес ще разгледаме

- Linear search
- Binary search
- Ternary search
- Jump search
- Exponential search


## Linear search (Линейно търсене)

- работи за сортирани **и** несортирани данни
- *O(N)* сложност по време
- подходящ за малък брой заявки при несортирани данни

Всеки елемент от масива се сравнява последователно с търсения.

```python
def linear_search(arr, X):
    for i in range(len(arr)):
        if arr[i] == X:
            return i
    
    return -1

arr = [9, 4, 3, 2, 6, 7, 1, 8, 5]
X = 6

print(linear_search(arr, X)) # 4
```

## Binary search (Двоично търсене)

- работи **само** за сортирани данни
- *O(logN)* сложност по време
- подходящ за много наброй заявки

Сравнява се средния елемент с търсения. Ако търсеният елемент е по-малък, разглежда се масива отляво на средния елемент. Ако търсеният е по-голям, разглежда се масива отдясно на средния. Стъпките се повтарят до намиране на елемента.

```python
def binary_search(arr, X):
    left = 0
    right = len(arr) - 1

    Xi = 0

    while left <= right:
        mid = left + (right - left) // 2

        if X <= arr[mid]:
            right = mid - 1
            Xi = mid
        else:
            left = mid + 1

    return Xi

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
X = 60

Xi = binary_search(arr, X)
print(Xi) # 5
```

## Ternary search (Тристранно търсене)

- работи за сортирани и параболични данни
- *O(log<sub>3</sub>N)* сложност по време
- подходящ за [намиране](https://cp-algorithms.com/num_methods/ternary_search.html) на единствен максимум/ минимум на функция

Сравняват се двата средни елементи с търсения. Ако търсеният елемент е по-малък от първия среден, разглежда се масива отляво на първия среден елемент. Ако търсеният е между двата средни, разглежда се втората третина от масива. Ако търсеният е по-голям от втория среден елемент - разглежда се масива отдясно на втория среден елемент. Отново стъпките се повтарят до намиране на елемента.

```python
def ternarySearch(arr, key, l, r):
    if r >= l:
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3 

        if arr[mid1] == key:
            return mid1
         
        if arr[mid2] == key:
            return mid2

        if key < arr[mid1]:
            return ternarySearch(arr, key, l, mid1 - 1)
        elif key > arr[mid2]:
            return ternarySearch(arr, key, mid2 + 1, r)
        else:
            return ternarySearch(arr, key, mid1 + 1, mid2 - 1)
    return -1

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
X = 60

Xi = ternarySearch(arr, X, 0, len(arr) - 1)
print(Xi) # 5
```

## Jump search (Търсене със скоци)

- работи **само** за сортирани данни
- [оптималният скок](https://www.wolframalpha.com/input?i=Argmin+of+f%28x%29+%3D+n%2Fx+%2B+x%2C+x+%3E+0%2C+n+%3E+0+for+x) е *sqrt(N)* (за минимален общ брой сравнения)
- *O(sqrt(N))* сложност по време
- [по-бавен](https://www.symbolab.com/solver/limit-calculator/%5Clim_%7Bx%5Cto%5Cinfty%7D%5Cleft(%5Cfrac%7Blnx%7D%7B%5Csqrt%7Bx%7D%7D%5Cright)?or=input) от Binary search ([*O(log(N))* < *O(sqrt(N))* < *O(N)*](https://www.wolframalpha.com/input?i=plot+log%28n%29%2C+sqrt%28n%29+from+1+to+1000))

Търсеният елемент се сравнява последователно с елементи на позиции, кратни на стъпката (корен от N). Когато търсеният елемент стане по-малък от елемента на K-та стъпка, се извършва линейно търсене в интервала (K-1)-ва стъпка до K-та стъпка.

Jump search прави 1 връщане назад в масива, докато при Binary search има най-много *logN* връщания. При нужда от ограничаване на връщанията Jump search е предпочитан пред Binary search въпреки по-голямата сложност по време. Точно поради тази причина не се извършва двоично търсене в намерения интервал.

```python
import math

def jumpSearch(arr, X):
    N = len(arr)
    block_size = int(math.sqrt(N))

    step = block_size
    prev = 0
    while arr[min(step, N) - 1] < X:
        prev = step
        step += block_size
        if prev >= N:
            return -1

    while arr[prev] < X:
        prev += 1

        if prev == min(step, N):
            return -1
     
    if arr[prev] == X:
        return prev
     
    return -1

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
X = 50

Xi = jumpSearch(arr, X)
print(Xi) # 4
```

## Exponential search (Експоненциално търсене)

- работи **само** за сортирани данни
- [*O(logi)*](https://en.wikipedia.org/wiki/Exponential_search#Performance) сложност по време, където *i* е позицията на числото
- подходящ при търсене на елементи, намиращи се в началото на масива (*i < N*)

Търсеният елемент се сравнява последователно с елементи на позиции, степени на двойката (2<sup>K</sup>). Когато търсеният елемент стане по-малък от елемента на К-та степен, се извършва двоично търсене в интервала 2<sup>K-1</sup>-ва позиция до 2<sup>K</sup>-та позиция.

```python
def exponential_search(arr, X):
    N = len(arr)

    i = 1
    while i < N and arr[i] <= X:
        i = i * 2

    left = i // 2
    right = min(i, N-1)
     
    return binary_search(arr, X, left, right)

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
X = 60

Xi = exponential_search(arr, X)
print(Xi) # 5
```

## Задачи за упражнение

- [Search Insert Position](https://leetcode.com/problems/search-insert-position)
- [First Bad Version](https://leetcode.com/problems/first-bad-version)
- [Perfect Printer](https://www.hackerrank.com/contests/sda-homework-3/challenges/challenge-2674/problem)
- [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array)
- [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix)

- [Safe Sort](https://www.hackerrank.com/contests/si-practice-2/challenges/task-1-1-1)

Решения на задачите: [тук](https://github.com/TeogopK/SDA-solved/tree/main/Seminar/sem_04)