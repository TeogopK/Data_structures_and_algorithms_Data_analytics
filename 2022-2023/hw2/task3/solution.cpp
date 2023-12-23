#include <iostream>
#include <string>

std::string str;
const int MAX_SIZE = 256;
int chars[MAX_SIZE];

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::cin >> str;

    for (size_t i = 0; i < MAX_SIZE; i++)
    {
        chars[i] = 0;
    }

    for (size_t i = 0; i < str.size(); i++)
    {
        chars[str[i]]++;
    }

    for (size_t i = 0; i < str.size(); i++)
    {
        if (chars[str[i]] == 1)
        {
            std::cout << i << " ";
        }
    }

    return 0;
}
