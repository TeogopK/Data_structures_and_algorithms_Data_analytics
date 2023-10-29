#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>

typedef std::pair<std::string, int> name;
name list[1000000];

bool comparator(name &name1, name &name2)
{
    return name1.second == name2.second ? name1.first < name2.first : name1.second > name2.second;
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    int N;
    std::cin >> N;

    for (int i = 0; i < N; i++)
    {
        std::cin >> list[i].first;
    }
    for (int i = 0; i < N; i++)
    {
        std::cin >> list[i].second;
    }

    sort(std::begin(list), std::end(list), comparator);

    for (int i = 0; i < N; i++)
    {
        std::cout << list[i].first << " " << list[i].second;
        if (i != N - 1)
        {
            std::cout << "\n";
        }
    }

    return 0;
}