#include <stdio.h>
#include <stdlib.h>
#define ROW 2
#define COLUMN 2
int sort_matrix(int arr[ROW][COLUMN])
{
    int minimum, i, j, temp, k, w, z = 0, q = 0 ;
    /* 
     i = row iterator
     j= column iterator
     temp = temporary Variable to swap the values
     k = iteration for row iterator i
     w = for storing the previous value of column iterator j;
     z = used as a temporary variable for storing k
     q = used as temporary variable for storing column iterator j

     */

    for(i = 0;i < ROW;i++)
        for(j = 0;j < COLUMN;j++)
        {
            temp = i;
            q = j;
            minimum = arr[i][j];
            w = j;
            for(k = i;k < ROW;k++)
            {

                for(;w < COLUMN;w++)
                if(arr[k][w] < minimum)
                {
                    minimum = arr[k][w];
                    z = k;
                    q = w;
                }
                w = 0;
            }
            if(arr[z][q] < arr[i][j])
            {
                temp = arr[i][j];
                arr[i][j] = minimum;
                arr[z][q] = temp;
            }
        }

    printf("\nSorted Matrix: \n");
    for(i = 0; i < ROW; i++)
    {
        for(j = 0;j < COLUMN;j++)
            printf("%d ",arr[i][j]);
        printf("\n");
    }
    
    return 0;
}

int main()
{
    int arr[ROW][COLUMN] = {{4,3},{2,1}};
    sort_matrix(arr);
    return 0;
}