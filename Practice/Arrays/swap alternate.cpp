#include <iostream>

using namespace std;

void swap_a(int a[], int size)
{

    int i = 0;
    int temp;
    while (i + 1 < size)
    {
        temp = a[i + 1];
        a[i + 1] = a[i];
        a[i] = temp;
        i = i + 2;
    }
}

int main()
{
    int n;
    cin >> n;
    int a[n];
    int i;
    for (i = 0; i < n; i++)
        cin >> a[i];

    swap_a(a, n);

    for (i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}