#include <iostream>

const int COUNT_NUMS = 1000000;

int arr[COUNT_NUMS];
int sorted[COUNT_NUMS];

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    int N;
    std::cin >> N;

    for (int i = 0; i < N; i++)
    {
        std::cin >> arr[i];
    }

    int j = 0;
    for (int i = 0; i < N; i++)
    {
        if (arr[i] % 2 == 0)
        {
            sorted[j] = arr[i];
            j++;
        }
    }

    for (int i = 0; i < N; i++)
    {
        if (arr[i] % 2 != 0)
        {
            sorted[j] = arr[i];
            j++;
        }
    }

    for (int i = 0; i < N; i++)
    {
        std::cout << sorted[i] << "\n";
    }

    return 0;
}