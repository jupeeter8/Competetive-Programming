#include <iostream>

using namespace std;

void reverseArray(int a[], int size)
{
    int start = 0;
    int end = size - 1;

    while (start <= end)
    {
        int temp;
        temp = a[start];
        a[start] = a[end];
        a[end] = temp;
        start++;
        end--;
    }
}

int main()
{
    int a[] = {2, 5, 6, 2, 6, 10, 16};
    int size = sizeof(a) / sizeof(a[0]);

    cout << "Array before reversing\n";
    for (int i = 0; i < size; i++)
        cout << a[i] << " ";

    cout << "\n";

    reverseArray(a, size);

    cout << "Array after reversing\n";
    for (int i = 0; i < size; i++)
        cout << a[i] << " ";
}