#include <stdio.h>
int main (){
    int n, i,j, sum=0;
    printf("Input the order of matrix:\n");
    scanf("%d", &n);
    int matrix_1[n][n];
    int matrix_2[n][n];
    int num =0; 

    printf("Enter the elements of matrix_1:\n");
    for (i=0;i<n;i++)
    {
        for (j=0;j<n;j++)
        {
            scanf("%d ",&matrix_1[i][j]);
        }
        printf("\n");

    }
     for (i=0;i<n;i++)
    {
        for (j=0;j<n;j++)
        {
            printf("%d ", matrix_1[i][j]);
        }
        printf("\n");

    }


    for (i=0;i<n;i++)
    {
        
        
     sum = sum+matrix_1[i][i] ;

        
    }
    printf("%d", sum);
    

    
}