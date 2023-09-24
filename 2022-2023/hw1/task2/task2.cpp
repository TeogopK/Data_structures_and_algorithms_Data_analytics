#include <iostream>
#include <vector>

int main()
{
    int N;
    std::cin >> N;

    std::vector<int> prices;

    int num;
    for (int i = 0; i < N; i++)
    {
        std::cin >> num;
        prices.push_back(num);
    }

    int maxProfit = 0;
    for (int i = 0; i < N - 1; i++)
    {
        if (prices[i] < prices[i + 1])
        {
            maxProfit += prices[i + 1] - prices[i];
        }
    }

    std::cout << maxProfit;
}