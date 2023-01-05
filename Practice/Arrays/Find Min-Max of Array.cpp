// Finding the minimun and maximum of an array

// Approach 1: Check for the min and max in the currently traversed array
// iniialize min and max to be first element of the array a[0]
// Currently the size of array is 1 so min and max = that element
// Traverse to the next element, size of array becomes 2, compare
// min and max to a[1]. Keep traversing, increasingly adding a new element to
// the array

#include <iostream>

using namespace std;

void findMinMax(int a[], int size)
{
    // Set min and max to the only element of array
    int min = a[0];
    int max = a[0];

    // Traverse the arrya, each iteration adds a new element to the array
    int i = 1;
    for (i; i < size; i++)
    {
        if (a[i] > max)
            max = a[i];
        else if (a[i] < min)
            min = a[i];
    }

    cout << "Max element of array is " << max << " Min element of array is " << min << endl;
}

int main()
{
    int a[] = {11, 5, 2, 8, 12, 5, 4};

    int size = sizeof(a) / sizeof(a[0]);
    findMinMax(a, size);
    return 0;
}