#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void Insertion_sort(int arr[],int n){
    int i, key, j; 
    for (i = 1; i < n; i++) { 
        key = arr[i]; 
        for (j=i-1;j >= 0 && arr[j] > key;j--) 
            arr[j + 1] = arr[j]; 
        arr[j + 1] = key; 
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
    
    Insertion_sort(arr,n);
    print(arr,n);  
    return 0;
}
