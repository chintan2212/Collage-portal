#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void swap(int *num1,int *num2){
    int tmp = *num1;
    *num1 = *num2;
    *num2 = tmp;
}

void Selection_sort(int arr[],int n){
    int i, j, min_; 
    for (i = 0; i < n-1; i++) { 
        min_ = i; 
        for (j = i+1; j < n; j++) 
            if (arr[j] < arr[min_]) 
                min_ = j; 
        swap(&arr[min_], &arr[i]); 
    } 
}

void print(int arr[],int n){
    for(int i=0;i < n;i++)
        printf("%d ",arr[i]);   
}

int main() {
    
    int n;
    scanf("%d", &n);
    int arr[n];
    
    if(n < 1 || n > 10000){
        printf("Size of array must be within [1,10000]");
        exit(0);
    }
    
    for(int i=0;i < n;i++){
        scanf("%d", &arr[i]);
        
        if(arr[i] < 1 || arr[i] > 1000000){
            printf("Number must be within [1,1000000]");
            exit(0);
        }
    }
    
    Selection_sort(arr,n);
    print(arr,n);
    return 0;
}
