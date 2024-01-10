# Упражнение 14

# Минимално покриващо дърво

## Миналия път разгледахме

- Алгоритъм на Дейкстра
- Алгоритъм на Белман-Форд

## Въпроси от миналия път

- :)

Решения от [контролно 5](https://www.hackerrank.com/contests/test5-sda2023-2024-ad123) - [тук](/Exams/exam_05).

## Днес ще разгледаме

- Минимално покриващо дърво (Minimum spanning tree)
- Алгоритъм на Прим (Prim)
- Алгоритъм на Крускал (Kruskal)
  
## Покриващо дърво (Spanning tree) на граф

- Дърво е свързан ацикличен насочен граф.
- Покриващо дърво на граф е дърво, подграф на дадения граф, което свързва всички възли на графа.
- Покриващото дърво на граф *G(V, E)* съдържа *V* на брой върха и *V - 1* ребра.
- Добавянето на ребро към покриващо дърво, ще създаде граф с цикъл.
- Премахването на ребро от покриващо дърво, ще създаде граф с две несвързани компоненти.
- Покриващо дърво на несвързан граф не е дефинирано.

![Spanning trees of a graph example](media/spanning_trees.png)

## Минимално покриващо дърво (Minimum spanning tree)

- Минимално покриващо дърво на претеглен ненасочен граф е покриващото дърво на графa с минимална сума на ребрата.
- Възможно е да съществува повече от 1 МПД (MST) за даден граф.
  
![Multiple Minimum spanning trees of a graph example](media/minimum_spanning_trees.png)

## Алгоритъм на Прим (Prim's algorithm)

- Намира минимално покриващо дърво на граф.
- Започва от даден връх и добавя реброто с най-малка тежест до съседен връх, който все още не е част от дървото.
- Сложността по време зависи от структурата за извличане на реброто с най-малка тежест.
- При използването на *Binary Heap* сложността е *O(E\*logV)*.

```python
def prim(start, V, graph):
    visited = set()
    pq = [(0, start)]
    mst_weight = 0
    
    while len(visited) != V:
        current_weight, current_vertex = heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        mst_weight += current_weight
        
        for neighb, weight in graph[current_vertex]:
            if neighb in visited:
                continue
                            
            heappush(pq, (weight, neighb))
    
    return mst_weight

prim(5, 5, graph) # 13
```

Пример при започване от *връх 5*:

![Prim's algorithm creating a MST of a graph, step by step example.](media/prims_algorithm_example.png)

## Алгоритъм на Крускал (Kruskal's algorithm)
![Alt text](media/mst_vs_dijkstra.png)
- Намира минимално покриващо дърво на граф.
- Сортира ребрата по минимална тежест, като на всяка стъпка добавя реброто с най-малка тежест, което няма да създаде цикъл в графа.
- Сложност по време *O(E\*logE)* заради сортирането на всички ребра.
- При *dense* граф, когато *Е = V<sup>2</sup>*, *O(ElogE) = O(ElogV<sup>2</sup>) = O(2ElogV) = O(ElogV)*
- 

![Kruskal's algorithm creating a MST of a graph, step by step example.](media/kruskals_algorithm_example.png)


## Задачи за упражнение

- [Prim's (MST) : Special Subtree](https://www.hackerrank.com/challenges/primsmstsub/problem)

Решения на задачите: [тук](/Tasks/tasks_14)