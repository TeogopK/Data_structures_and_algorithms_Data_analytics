#include <iostream>
#define MAX_NUM 1000000

int numbers[MAX_NUM];
int checkList[MAX_NUM + 1];

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    int N;
    std::cin >> N;

    for (int i = 0; i < N; i++)
    {
        std::cin >> numbers[i];
    }

    for (int i = 0; i < MAX_NUM + 1; i++)
    {
        checkList[i] = 0;
    }

    for (int i = 0; i < N; i++)
    {
        if (numbers[i] > 0 && numbers[i] < MAX_NUM + 1)
        {
            checkList[numbers[i] - 1] = 1;
        }
    }

    for (int i = 0; i < MAX_NUM + 1; i++)
    {
        if (checkList[i] == 0)
        {
            std::cout << i + 1;
            break;
        }
    }

    return 0;
}