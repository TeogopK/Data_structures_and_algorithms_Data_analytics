# Note this solution will not pass all tests 
#include <iostream>

int main()
{
    int N;
    std::cin >> N;

    int *numbers = new int[N];

    for (int i = 0; i < N; i++)
    {
        std::cin >> numbers[i];
    }

    int min_number = 1;
    for (int i = 0; i < N; i++)
    {
        if (numbers[i] == min_number)
        {
            min_number++;
            i = 0;
        }
    }
    std::cout << min_number;

    delete[] numbers;

    return 0;
}