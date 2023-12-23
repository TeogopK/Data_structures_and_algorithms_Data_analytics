#include <iostream>
#include <string>

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    size_t Q;
    std::cin >> Q;

    size_t length;
    std::string arr;
    
    for (size_t i = 0; i < Q; i++)
    {
        std::cin >> length >> arr;
        
        int count = 0;
        for (size_t j = 0; j < length - 1; j++)
        {
            if (arr[j] == arr[j + 1])
            {
                count++;
            }
        }

        std::cout << count << "\n";
    }

    return 0;
}